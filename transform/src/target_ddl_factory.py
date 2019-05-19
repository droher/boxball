from pathlib import Path
from typing import Optional

from sqlalchemy import MetaData
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.sql.ddl import CreateSchema, CreateTable

from src import OUTPUT_PATH, DATA_PATH_PREFIX

DdlString = str


class TargetDdlFactory:

    @property
    def target_name(self) -> str:
        raise NotImplementedError("Each target must implement its own target name (e.g. 'postgres'")

    @property
    def dialect(self) -> Optional[Dialect]:
        raise NotImplementedError("Each target must specify its own dialect or explicitly declare it None")

    @property
    def file_format(self) -> str:
        return "sql"

    @property
    def data_path_prefix(self) -> Path:
        return DATA_PATH_PREFIX

    def make_create_ddl(self, metadata: MetaData) -> DdlString:
        if not self.dialect:
            raise ValueError("Dialect must be specified to use default metadata creation function")

        ddl = []
        if metadata.schema:
            schema_ddl = str(CreateSchema(metadata.schema).compile(dialect=self.dialect))
            ddl.append(schema_ddl)
        for table_obj in metadata.tables.values():
            table_ddl = str(CreateTable(table_obj).compile(dialect=self.dialect))
            ddl.append(table_ddl)
        return ";\n".join(d for d in ddl) + ";\n"

    def make_copy_ddl(self, metadata: MetaData) -> DdlString:
        raise NotImplementedError("Each target must implement its own copy function")

    @staticmethod
    def metadata_transform(metadata: MetaData) -> MetaData:
        """
        Overridable function to transform the metadata into a suitable format, e.g.
        for postgres_cstore_fdw, which requires table-level transformations
        """
        return metadata

    def build_ddl(self, *metadatas: MetaData) -> None:
        for metadatum in metadatas:
            transformed_metadata = self.metadata_transform(metadatum)
            output_file = OUTPUT_PATH.joinpath("{}.{}".format(self.target_name, self.file_format))
            with open(output_file, "a+") as f:
                f.write(self.make_create_ddl(transformed_metadata))
                f.write(self.make_copy_ddl(transformed_metadata))
