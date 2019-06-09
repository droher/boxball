import os
from pathlib import Path

from src.schemas import retrosheet_metadata, baseballdatabank_metadata, all_metadata
from src.ddl_factories import all_factories

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
