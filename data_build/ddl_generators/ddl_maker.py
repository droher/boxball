from pathlib import Path
from typing import Callable

from sqlalchemy import MetaData, Float
from sqlalchemy.dialects import postgresql, mysql
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.schema import CreateTable, CreateSchema

from ddl_generators.schemas import all_metadata

DEFAULT_CSV_PATH_PREFIX = Path("/data")
OUTPUT_PATH = Path("/ddl")

DdlString = str


def make_load_ddl(metadata: MetaData, dialect: Dialect) -> DdlString:
    ddl = []
    schema_ddl = str(CreateSchema(metadata.schema).compile(dialect=dialect))
    ddl.append(schema_ddl)
    for table_obj in metadata.tables.values():
        table_ddl = str(CreateTable(table_obj).compile(dialect=dialect))
        ddl.append(table_ddl)
    return ";\n".join(d for d in ddl) + ";\n"


def make_postgres_copy_ddl(metadata: MetaData) -> DdlString:
    copy_ddl_template = """
    ALTER TABLE {full_table_name} SET UNLOGGED;
    COPY {full_table_name}({column_names}) FROM PROGRAM '{cmd}' CSV;
    """
    csv_dir = DEFAULT_CSV_PATH_PREFIX.joinpath(metadata.schema)
    cmd_template = "zstd --rm -cd {csv_file}"
    ddl = []
    for table_obj in metadata.tables.values():
        table_name = table_obj.name
        column_names = ", ".join((c.name for c in table_obj.columns.values()
                                  if not(c.autoincrement is True)))
        csv_file = csv_dir.joinpath(table_name).with_suffix(".csv.zst")
        cmd = cmd_template.format(csv_file=csv_file)
        copy_ddl = copy_ddl_template.format(full_table_name=table_obj.fullname, cmd=cmd,
                                            column_names=column_names)
        ddl.append(copy_ddl)
    return "\n".join(ddl) + ";\n"


def make_mysql_copy_ddl(metadata: MetaData) -> DdlString:
    copy_ddl_template = """
    LOAD DATA INFILE '{csv_file}' INTO TABLE {full_table_name}
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    ({column_vars})
    SET {null_handlers};
    """
    csv_dir = DEFAULT_CSV_PATH_PREFIX.joinpath(metadata.schema)
    ddl = []
    for table_obj in metadata.tables.values():
        table_name = table_obj.name
        column_name_list = [c.name for c in table_obj.columns.values() if not(c.autoincrement is True)]
        # This bundle of joy below is to handle the fact that MySQL doesn't allow nulls
        # to be represented as blanks in CSV files, or floats to have an infinite value
        float_col_list = [c.name for c in table_obj.columns.values() if isinstance(c.type, Float)]
        null_handler_list = ["`{0}` = IF(@{0} = '', NULL, @{0})".format(c) for c in column_name_list
                             if c not in float_col_list]
        float_handler_list = ["`{0}` = IF(@{0} IN ('', 'inf'), NULL, @{0})".format(c) for c in float_col_list]

        column_vars = ", ".join("@{}".format(c) for c in column_name_list)
        null_handlers = ",\n".join(null_handler_list + float_handler_list)

        csv_file = csv_dir.joinpath(table_name).with_suffix(".csv")
        copy_ddl = copy_ddl_template.format(csv_file=csv_file, column_vars=column_vars,
                                            full_table_name=table_obj.fullname, null_handlers=null_handlers)
        ddl.append(copy_ddl)
    return "\n".join(ddl) + ";\n"


def build_ddl(target_name: str, dialect: Dialect, copy_func: Callable[[MetaData], str],
              *metadatas: MetaData) -> None:
    for metadatum in metadatas:
        output_file = OUTPUT_PATH.joinpath("{}.sql".format(target_name))
        with open(output_file, "a+") as f:
            f.write(make_load_ddl(metadatum, dialect))
            f.write(copy_func(metadatum))


if __name__ == "__main__":
    OUTPUT_PATH.mkdir(exist_ok=True)
    build_ddl("mysql", mysql.dialect(), make_mysql_copy_ddl, *all_metadata)
    build_ddl("postgres", postgresql.dialect(), make_postgres_copy_ddl, *all_metadata)
