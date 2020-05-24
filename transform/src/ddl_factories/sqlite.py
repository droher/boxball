from sqlalchemy import MetaData, Table, Boolean, Column, SmallInteger
from sqlalchemy.dialects import sqlite
from sqlalchemy.engine.interfaces import Dialect

from src.target_ddl_factory import DdlString, TargetDdlFactory


class SqliteDdlFactory(TargetDdlFactory):
    @property
    def target_name(self) -> str:
        return "sqlite"

    @property
    def dialect(self) -> Dialect:
        return sqlite.dialect()

    @staticmethod
    def metadata_transform(metadata: MetaData) -> MetaData:
        new_metadata = MetaData()
        for table in metadata.tables.values():
            # Need to namespace in the tablename because no schemas in sqlite
            table_name = "{}_{}".format(metadata.schema, table.name)
            # Remove dummy cols as no need for PKs (and we can't autoincrement anyway)
            # and change booleans to int to stop checks from generating in the ddl
            old_cols = [c for c in table.columns.values() if c.autoincrement is not True]
            new_cols = []
            for col in old_cols:
                typ = col.type if not isinstance(col.type, Boolean) else SmallInteger
                new_cols.append(Column(col.name, typ))

            Table(table_name, new_metadata, *new_cols)
        return new_metadata

    def make_copy_ddl(self, metadata: MetaData) -> DdlString:
        copy_ddl_template = ".import {csv_file} {table_name}"
        ddl = [".mode csv"]
        for table_obj in metadata.tables.values():
            table_name: str = table_obj.fullname
            namespace = table_name[:table_name.index("_")]
            model_name = table_name[table_name.index("_") + 1:]
            csv_dir = self.data_path_prefix.joinpath(namespace)
            csv_file = csv_dir.joinpath(model_name).with_suffix(".csv")
            copy_ddl = copy_ddl_template.format(table_name=table_name, csv_file=csv_file)
            ddl.append(copy_ddl)

            ddl.append(f"UPDATE {table_name} SET")
            set_statements = []
            for col in table_obj.columns.values():
                col_name = col.name
                null_case = f"{col_name}=NULLIF({col_name}, '')"
                set_statements.append(null_case)
                if isinstance(col.type, SmallInteger):
                    bool_case = f"{col_name}=CASE {col_name} WHEN 'T' THEN 1 WHEN 'F' THEN 0 ELSE {col_name} END"
                    set_statements.append(bool_case)
            set_statement = ",\n".join(set_statements) + ";"
            ddl.append(set_statement)
        return "\n".join(ddl)
