from sqlalchemy import create_engine
from sqlalchemy.dialects import sqlite, postgresql, mysql
from sqlalchemy.schema import CreateTable, Table, MetaData, Column
from sqlalchemy_fdw.dialect import dialect
from sqlalchemy_fdw import ForeignDataWrapper, ForeignTable

from src.retrosheet import metadata as m, Game

engine = create_engine('pgfdw://user:password@host:10/dbname', strategy="mock", executor=lambda x: None)
metadata = MetaData()
metadata.bind = engine

fdw = ForeignDataWrapper("myfdwserver", "myfdwextension", metadata=metadata,
                            options={'option1': 'test'})
fdw.create()


for table in m.tables.values():
    t: Table = table
    new_cols = []
    for c in t.columns.values():
        new_cols.append(c.copy())
    ft = ForeignTable(t.name, metadata, *[c.copy() for c in t.columns.values()], pgfdw_server="myfdwserver")

for t in metadata.tables.values():
    print(CreateTable(t).compile(dialect=dialect()))
