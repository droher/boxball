from pathlib import Path
from sqlalchemy import MetaData
from sqlalchemy.schema import CreateTable, CreateSchema
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.dialects import postgresql

from ddl_generators.schemas import all_metadata

CSV_PATH_PREFIX = Path("/data")

DdlString = str


def make_load_ddl(metadata: MetaData, dialect: Dialect) -> DdlString:
    ddl = []
    schema_ddl = str(CreateSchema(metadata.schema).compile(dialect=dialect))
    ddl.append(schema_ddl)
    for table_obj in metadata.tables.values():
        table_ddl = str(CreateTable(table_obj).compile(dialect=dialect))
        ddl.append(table_ddl)
    return ";\n".join(d for d in ddl) + ";\n"


def make_postgres_copy_ddl(metadata: MetaData, csv_dir: Path) -> DdlString:
    copy_ddl_template = "COPY {full_table_name}({column_names}) FROM PROGRAM '{cmd}' CSV;"
    cmd_template = "zstd --rm -cd {csv_path}"
    ddl = []
    for table_obj in metadata.tables.values():
        table_name = table_obj.name
        column_names = ", ".join((c.name for c in table_obj.columns.values()
                                  if not(c.autoincrement is True)))
        csv_path = csv_dir.joinpath(table_name).with_suffix(".csv.zst")
        cmd = cmd_template.format(csv_path=csv_path)
        copy_ddl = copy_ddl_template.format(full_table_name=table_obj.fullname, cmd=cmd,
                                            column_names=column_names)
        ddl.append(copy_ddl)
    return "\n".join(ddl) + ";\n"


def build_postgres_ddl(*metadatas: MetaData) -> None:
    for metadatum in metadatas:
        csv_path = CSV_PATH_PREFIX.joinpath(metadatum.schema)
        with open("/load.sql", "a") as f:
            f.write(make_load_ddl(metadatum, postgresql.dialect()))
            f.write(make_postgres_copy_ddl(metadatum, csv_path))


if __name__ == "__main__":
    build_postgres_ddl(*all_metadata)
