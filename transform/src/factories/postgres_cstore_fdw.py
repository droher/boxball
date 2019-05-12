from sqlalchemy.schema import MetaData
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy_fdw import ForeignTable
from sqlalchemy_fdw.dialect import PGDialectFdw

from src.factories.postgres import PostgresDdlFactory
from src.target_ddl_factory import DdlString

CSTORE_SERVER = "cstore_server"


class PostgresCstoreFdwDdlFactory(PostgresDdlFactory):
    """
    Almost exactly the same create/copy syntax as Postgres proper, except the create table syntax is different
    and we need to create the server.
    """

    @property
    def target_name(self) -> str:
        return "postgres_cstore_fdw"

    @property
    def dialect(self) -> Dialect:
        return PGDialectFdw()

    @staticmethod
    def metadata_transform(metadata: MetaData) -> MetaData:
        new_metadata = MetaData()
        opts = {"pgfdw_server": CSTORE_SERVER, "pgfdw_options": {"compression": "pglz"}}
        for table in metadata.tables.values():
            # Need to namespace in the tablename because no schemas in fdw
            table_name = "{}_{}".format(metadata.schema, table.name)
            # Remove dummy cols as no need for PKs (and we can't autoincrement anyway)
            cols = [c.copy() for c in table.columns.values() if c.autoincrement is not True]

            ForeignTable(table_name, new_metadata, *cols, **opts)
        return new_metadata

    def make_create_ddl(self, metadata: MetaData) -> DdlString:
        server_ddl = """
        CREATE EXTENSION IF NOT EXISTS cstore_fdw;
        CREATE SERVER IF NOT EXISTS {} FOREIGN DATA WRAPPER cstore_fdw;
        """.format(CSTORE_SERVER)

        existing_ddl = super().make_create_ddl(metadata)
        return "{}\n{}".format(server_ddl, existing_ddl)
