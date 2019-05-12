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
        null_template = "UPDATE {table_name} SET {col_name}=NULL WHERE {col_name}='';"
        bool_template = "UPDATE {table_name} SET {col_name}={bool_int} WHERE {col_name} = '{bool_str}';"
        ddl = [".mode csv"]
        for table_obj in metadata.tables.values():
            table_name: str = table_obj.fullname
            namespace = table_name[:table_name.index("_")]
            model_name = table_name[table_name.index("_")+1:]
            csv_dir = self.data_path_prefix.joinpath(namespace)
            csv_file = csv_dir.joinpath(model_name).with_suffix(".csv")
            copy_ddl = copy_ddl_template.format(table_name=table_name, csv_file=csv_file)
            ddl.append(copy_ddl)

            for col in table_obj.columns.values():
                col_name = col.name
                base_kwargs = dict(table_name=table_name, col_name=col_name)
                ddl.append(null_template.format(**base_kwargs))
                if isinstance(col.type, Boolean):
                    ddl.append(bool_template.format(bool_int=1, bool_str="T", **base_kwargs))
                    ddl.append(bool_template.format(bool_int=0, bool_str="F", **base_kwargs))
        return "\n".join(ddl)

    def make_create_ddl(self, metadata: MetaData) -> DdlString:
        existing_ddl = super().make_create_ddl(metadata)
        return existing_ddl.replace("(0, 1)", "('0', '1', 'T', 'F', '')")
