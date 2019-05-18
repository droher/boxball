from sqlalchemy import MetaData, Column, Table, Boolean, SmallInteger, CHAR, String, Integer, Float, DateTime, Date
from clickhouse_sqlalchemy.drivers.base import ClickHouseDialect
from clickhouse_sqlalchemy.engines import Memory
from clickhouse_sqlalchemy import types
from sqlalchemy.engine.interfaces import Dialect

from src.target_ddl_factory import DdlString, TargetDdlFactory

type_lookup = {
    Boolean: types.UInt8,
    SmallInteger: types.Int16,
    CHAR: types.String,
    String: types.String,
    Integer: types.Int32,
    Float: types.Float64,
    # Appears to be issue with the way it interprets parquet datetypes,
    # so we have Arrow cast all dates to a timestamp in the transform, which clickhouse can handle
    Date: types.DateTime,
    DateTime: types.DateTime
}


class ClickhouseDdlFactory(TargetDdlFactory):

    @property
    def target_name(self) -> str:
        return "clickhouse"

    @property
    def dialect(self) -> Dialect:
        return ClickHouseDialect()

    @staticmethod
    def metadata_transform(metadata: MetaData) -> MetaData:
        # Just need to remove autoincrement cols

        new_metadata = MetaData(schema=metadata.schema)

        for table in metadata.tables.values():
            cols = [c for c in table.columns.values() if c.autoincrement is not True]
            new_cols = []
            for col in cols:
                typ = types.Nullable(type_lookup[type(col.type)])
                new_cols.append(Column(col.name, typ))
            t = Table(table.name, new_metadata, *new_cols)
            t.engine = Memory()
        return new_metadata

    def make_copy_ddl(self, metadata: MetaData) -> DdlString:
        # Need to implement command line statements in the load folder
        return ""

    def make_create_ddl(self, metadata: MetaData) -> DdlString:
        return (super()
                .make_create_ddl(metadata)
                .replace("CREATE SCHEMA", "CREATE DATABASE")
                .replace("ENGINE = Memory", "Engine = File(Parquet)")
                .replace(" CHAR(", " FixedString(")
                )
