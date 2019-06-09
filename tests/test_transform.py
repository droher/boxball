import os
from pathlib import Path

from src import OUTPUT_PATH
from src.schemas import retrosheet_metadata, baseballdatabank_metadata, all_metadata
from src.ddl_factories import all_factories
from src.parquet import write_files, PARQUET_PREFIX


os.chdir(Path("/tmp/boxball"))


class TestSchemas:
    def test_schemas_compile(self):
        assert len(retrosheet_metadata.tables) == 16
        assert len(baseballdatabank_metadata.tables) == 27


class TestDdlFactory:
    def test_ddl_compiles(self):
        for factory in all_factories:
            for metadata in all_metadata:
                transformed_metadata = factory.metadata_transform(metadata)
                assert isinstance(factory.make_create_ddl(transformed_metadata), str)
                assert isinstance(factory.make_copy_ddl(transformed_metadata), str)

    def test_ddl_writes(self):
        OUTPUT_PATH.mkdir(exist_ok=True)
        for factory in all_factories:
            factory.build_ddl(*all_metadata)
            assert OUTPUT_PATH.joinpath("{}.{}".format(factory.target_name, factory.file_format)).exists()


class TestParquet:
    def test_parquet_writes(self):
        for m in all_metadata:
            write_files(m)
            for table in m.tables.values():
                table_name = table.name
                assert PARQUET_PREFIX.joinpath(m.schema, table_name).with_suffix(".parquet").exists()
