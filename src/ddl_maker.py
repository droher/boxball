from sqlalchemy import MetaData, Table
from sqlalchemy.schema import CreateTable, CreateSchema
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.dialects import postgresql, sqlite

from src.retrosheet import metadata as retrosheet_metadata


def make_load_ddl(metadata: MetaData, dialect: Dialect) -> str:
    ddl = []
    schema_ddl = str(CreateSchema(metadata.schema).compile(dialect=dialect))
    ddl.append(schema_ddl)
    for table_obj in metadata.tables.values():
        table_ddl = str(CreateTable(table_obj).compile(dialect=dialect))
        ddl.append(table_ddl)
    return ";\n".join(d for d in ddl)


def make_postgres_copy_ddl(metadata: MetaData):
    copy_ddl_template = "COPY {full_table_name} FROM PROGRAM '{cmd}' FORMAT CSV;"
    cmd_template = "gunzip -c {table_name}.csv.gz"
    ddl = []
    for table_obj in metadata.tables.values():
        cmd = cmd_template.format(table_name=table_obj.name)
        copy_ddl = copy_ddl_template.format(full_table_name=table_obj.fullname, cmd=cmd)
        ddl.append(copy_ddl)
    return "\n".join(ddl)


print(make_load_ddl(retrosheet_metadata, sqlite.dialect()))