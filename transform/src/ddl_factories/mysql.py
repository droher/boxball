from typing import List
from sqlalchemy import MetaData, Float, Boolean, Column, Table, String, Text
from sqlalchemy.dialects import mysql
from sqlalchemy.engine.interfaces import Dialect

from src.target_ddl_factory import DdlString, TargetDdlFactory


# InnoDB row-size hard limit is 65535 bytes (excluding BLOB/TEXT). With the
# default utf8mb4 charset (4 bytes/char) that caps a single row's worth of
# in-row VARCHAR data at ~16K chars. Several retrosheet tables (bio, comment,
# park, roster, event) blow past that with 20+ String(1024) columns. Promote
# any String(N) where N >= this threshold to TEXT, which spills off-page and
# does not count against the row-size cap.
MYSQL_VARCHAR_TO_TEXT_THRESHOLD = 256


def _promoted_type(col: Column):
    if (isinstance(col.type, String)
            and not isinstance(col.type, Text)
            and col.type.length is not None
            and col.type.length >= MYSQL_VARCHAR_TO_TEXT_THRESHOLD
            and not col.primary_key):
        return Text()
    return col.type


class MySqlDdlFactory(TargetDdlFactory):

    @property
    def target_name(self) -> str:
        return "mysql"

    @property
    def dialect(self) -> Dialect:
        return mysql.dialect()

    @staticmethod
    def metadata_transform(metadata: MetaData) -> MetaData:
        # Build a fresh MetaData rather than mutating shared state — the
        # factory list iterates `all_metadata` once and downstream factories
        # (clickhouse, etc.) must see the original SQLAlchemy types.
        new_metadata = MetaData(schema=metadata.schema)
        for table in metadata.tables.values():
            new_cols = []
            for col in table.columns.values():
                new_cols.append(Column(
                    col.name,
                    _promoted_type(col),
                    primary_key=col.primary_key,
                    nullable=col.nullable,
                    autoincrement=col.autoincrement,
                ))
            Table(table.name, new_metadata, *new_cols)
        return new_metadata

    def make_copy_ddl(self, metadata: MetaData) -> DdlString:
        copy_ddl_template = """
        LOAD DATA INFILE '{csv_file}' INTO TABLE {full_table_name}
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        ({column_vars})
        SET {exps};
        """
        default_exp = "`{0}` = IF(@{0} = '', NULL, @{0})"
        float_exp = "`{0}` = IF(@{0} IN ('', 'inf'), NULL, @{0})"
        boolean_exp = "`{0}` = IF(@{0} = 'T', 1, IF(@{0} = 'F', 0, IF(@{0} = '', NULL, @{0})))"

        csv_dir = self.data_path_prefix.joinpath(metadata.schema)
        ddl = []
        for table_obj in metadata.tables.values():
            table_name = table_obj.name
            # This bundle of joy below is to handle the fact that MySQL doesn't allow nulls
            # to be represented as blanks in CSV files, or floats to have an infinite value,
            # or booleans to be represented by T/F
            cols: List[Column] = table_obj.columns.values()
            float_col_list = [float_exp.format(c.name) for c in cols
                              if isinstance(c.type, Float)]
            boolean_col_list = [boolean_exp.format(c.name) for c in cols
                                if isinstance(c.type, Boolean)]
            default_col_list = [default_exp.format(c.name) for c in cols
                                if not isinstance(c.type, (Boolean, Float))]
            column_vars = ", ".join("@{}".format(c.name) for c in cols)

            exps = ",\n".join(float_col_list + boolean_col_list + default_col_list)

            csv_file = csv_dir.joinpath(table_name).with_suffix(".csv")
            copy_ddl = copy_ddl_template.format(csv_file=csv_file, column_vars=column_vars,
                                                full_table_name=table_obj.fullname, exps=exps)
            ddl.append(copy_ddl)
        return "\n".join(ddl) + ";\n"
