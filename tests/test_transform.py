import os
from pathlib import Path

from src.schemas import retrosheet_metadata, baseballdatabank_metadata

os.chdir(Path("/tmp/boxball"))


class TestSchemas:
    def test_schemas_compile(self):
        assert len(retrosheet_metadata.tables) == 16
        assert len(baseballdatabank_metadata.tables) == 27
