import sys
import os
from unittest.mock import patch
from pathlib import Path
sys.path.insert(0, os.getcwd())

from parsers.retrosheet import RetrosheetParser, PARSE_FUNCS
from parsers.baseballdatabank import get_baseballdatabank_files
from parsers.util import compress


MOCK_FUNCS = {k: "cat *{year}*" for k in PARSE_FUNCS}


class TestRetrosheet:
    def test_parse_code_tables(self):
        RetrosheetParser().parse_code_tables()
        assert True

    def test_parse_simples_files(self):
        RetrosheetParser().parse_simple_files()

    def test_parse_event_types(self):
        with patch("parsers.retrosheet.PARSE_FUNCS", MOCK_FUNCS) as mock_funcs:
            RetrosheetParser().parse_event_types(use_parallel=False)
        assert True


class TestBaseballDatabank:
    def test_get_baseballdatabank_files(self):
        get_baseballdatabank_files()
        assert True


class TestExtractUtil:
    def test_compress(self):
        compress(Path("retrosheet/gamelog/GL1871.TXT"), Path("retrosheet/gamelog"),
                 remove_original=False)
        assert True
