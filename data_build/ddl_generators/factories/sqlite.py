from sqlalchemy import MetaData, Table
from sqlalchemy.dialects import sqlite
from sqlalchemy.engine.interfaces import Dialect

from ddl_generators.factories.target_ddl_factory import DdlString, TargetDdlFactory


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
            cols = [c.copy() for c in table.columns.values() if c.autoincrement is not True]

            Table(table_name, new_metadata, *cols)
        return new_metadata

    def make_copy_ddl(self, metadata: MetaData) -> DdlString:
        copy_ddl_template = ".import {csv_file} {full_table_name}"
        ddl = [".mode csv"]
        for table_obj in metadata.tables.values():
            name: str = table_obj.fullname
            csv_dir = self.data_path_prefix.joinpath(name[:name.index("_")])
            csv_file = csv_dir.joinpath(name[name.index("_")+1:]).with_suffix(".csv")
            copy_ddl = copy_ddl_template.format(full_table_name=name, csv_file=csv_file)
            ddl.append(copy_ddl)
        return "\n".join(ddl)

    def make_create_ddl(self, metadata: MetaData) -> DdlString:
        existing_ddl = super().make_create_ddl(metadata)
        # Change booleans to CHAR(1) T/F
        return existing_ddl.replace("BOOLEAN", "CHAR(1)").replace("(0, 1)", "('0', '1', 'T', 'F')")
