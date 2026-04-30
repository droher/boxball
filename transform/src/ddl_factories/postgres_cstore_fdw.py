from sqlalchemy import Column, MetaData, Table
from sqlalchemy.dialects import postgresql
from sqlalchemy.engine.interfaces import Dialect

from src.ddl_factories.postgres import PostgresDdlFactory
from src.target_ddl_factory import DdlString

CSTORE_SERVER = "cstore_server"
CSTORE_OPTIONS = {"compression": "pglz"}


class PostgresCstoreFdwDdlFactory(PostgresDdlFactory):
    """
    Same load semantics as Postgres, but tables become CREATE FOREIGN TABLE backed by
    cstore_fdw. Schemas flatten into table-name prefixes because foreign tables
    don't carry one through the FDW. Replaces the abandoned sqlalchemy_fdw shim
    by emitting CREATE FOREIGN TABLE DDL directly off SQLAlchemy column metadata.
    """

    @property
    def target_name(self) -> str:
        return "postgres_cstore_fdw"

    @property
    def dialect(self) -> Dialect:
        return postgresql.dialect()

    @staticmethod
    def metadata_transform(metadata: MetaData) -> MetaData:
        new_metadata = MetaData()
        for table in metadata.tables.values():
            table_name = "{}_{}".format(metadata.schema, table.name)
            new_cols = [
                Column(c.name, c.type, nullable=c.nullable)
                for c in table.columns.values()
                if c.autoincrement is not True
            ]
            Table(table_name, new_metadata, *new_cols)
        return new_metadata

    def _foreign_table_ddl(self, table: Table) -> str:
        type_compiler = self.dialect.type_compiler_instance
        prep = self.dialect.identifier_preparer
        col_lines = []
        for col in table.columns.values():
            col_type = type_compiler.process(col.type)
            null_part = "" if col.nullable else " NOT NULL"
            col_lines.append(f"\t{prep.quote(col.name)} {col_type}{null_part}")
        opts_sql = ", ".join(f"{k} '{v}'" for k, v in CSTORE_OPTIONS.items())
        return (
            f"\nCREATE FOREIGN TABLE {prep.quote(table.name)} (\n"
            + ",\n".join(col_lines)
            + f"\n) SERVER {CSTORE_SERVER} OPTIONS ({opts_sql})"
        )

    def make_create_ddl(self, metadata: MetaData) -> DdlString:
        server_ddl = (
            "\nCREATE EXTENSION IF NOT EXISTS cstore_fdw;\n"
            f"CREATE SERVER IF NOT EXISTS {CSTORE_SERVER} FOREIGN DATA WRAPPER cstore_fdw"
        )
        ddl = [server_ddl] + [self._foreign_table_ddl(t) for t in metadata.tables.values()]
        return ";\n".join(ddl) + ";\n"
