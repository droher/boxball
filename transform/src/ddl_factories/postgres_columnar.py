import re

from sqlalchemy import Column, MetaData, Table

from src.ddl_factories.postgres import PostgresDdlFactory
from src.target_ddl_factory import DdlString

CITUS_EXTENSION_DDL = "CREATE EXTENSION IF NOT EXISTS citus;\n"
COLUMNAR_CLAUSE = " USING columnar"

# CreateTable emits "CREATE TABLE <name> (...)" with the closing paren followed
# (optionally) by table-level kwargs and a newline. Inject USING columnar
# immediately after the closing paren of the column list, before any trailing
# whitespace/newline. Anchored on a balanced one-level paren match because
# columns themselves can carry parens (e.g. CHAR(2), NUMERIC(10,2)).
_CREATE_TABLE_TAIL = re.compile(r"(CREATE TABLE [^(]+\((?:[^()]|\([^()]*\))*\))(\s*)$", re.MULTILINE)


class PostgresColumnarDdlFactory(PostgresDdlFactory):
    """
    Postgres + Citus columnar (single-node mode). Uses native
    `CREATE TABLE ... USING columnar` syntax and inherits the row-store
    Postgres COPY FROM PROGRAM loader unchanged. Schemas are preserved
    (no <schema>_<table> flattening — Citus columnar respects namespaces).
    """

    @property
    def target_name(self) -> str:
        return "postgres_columnar"

    @staticmethod
    def metadata_transform(metadata: MetaData) -> MetaData:
        new_metadata = MetaData(schema=metadata.schema)
        for table in metadata.tables.values():
            new_cols = [
                Column(c.name, c.type, nullable=c.nullable)
                for c in table.columns.values()
                if c.autoincrement is not True
            ]
            Table(table.name, new_metadata, *new_cols)
        return new_metadata

    def make_create_ddl(self, metadata: MetaData) -> DdlString:
        base_ddl = super().make_create_ddl(metadata)
        rewritten = _CREATE_TABLE_TAIL.sub(r"\1" + COLUMNAR_CLAUSE + r"\2", base_ddl)
        return CITUS_EXTENSION_DDL + rewritten
