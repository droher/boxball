from unittest.mock import patch
from pathlib import Path

from parsers.retrosheet import (
    PARSE_FUNCS,
    RetrosheetParser,
    all_pbp_game_ids,
    deduced_game_ids,
    event_game_ids,
)
from parsers.baseballdatabank import get_baseballdatabank_files
from parsers.util import OUTPUT_PATH, compress

TMP = Path("/tmp/boxball")
MOCK_FUNCS = {k: "cat *{year}*" for k in PARSE_FUNCS}

SIMPLE_OUTPUTS = ("gamelog.csv.zst", "schedule.csv.zst", "park.csv.zst", "bio.csv.zst", "roster.csv.zst")
EVENT_OUTPUTS = ("daily.csv.zst", "comment.csv.zst", "game.csv.zst", "sub.csv.zst", "event.csv.zst")


def _assert_non_empty(*names: str) -> None:
    for name in names:
        path = OUTPUT_PATH / name
        assert path.exists(), f"expected parser output {path} to exist"
        assert path.stat().st_size > 0, f"expected parser output {path} to be non-empty"


class TestRetrosheet:
    def test_parse_code_tables(self):
        with patch("parsers.retrosheet.compress", autospec=True) as mock_compress:
            RetrosheetParser().parse_code_tables()
            assert mock_compress.call_count == 7

    def test_parse_simples_files(self):
        RetrosheetParser().parse_simple_files()
        _assert_non_empty(*SIMPLE_OUTPUTS)

    def test_parse_event_types(self):
        # Contract enforced by parsers/retrosheet.py:51-53 — deduced games must
        # never duplicate event-file games. Verify the fixture honors it before
        # invoking the parser, so a regression in fixture build surfaces here
        # rather than as a downstream ValueError.
        assert event_game_ids().isdisjoint(deduced_game_ids()), (
            "fixture invariant violated: deduced game ids overlap event game ids"
        )
        with patch("parsers.retrosheet.PARSE_FUNCS", MOCK_FUNCS):
            RetrosheetParser().parse_event_types(use_parallel=False)
        _assert_non_empty(*EVENT_OUTPUTS)

    def test_run_all(self):
        with patch("parsers.retrosheet.PARSE_FUNCS", MOCK_FUNCS):
            RetrosheetParser().run(use_parallel=False)
        assert all_pbp_game_ids(), "expected non-empty PBP game id set after full run"
        _assert_non_empty("deduced_game.csv.zst")


class TestBaseballDatabank:
    def test_get_baseballdatabank_files(self):
        get_baseballdatabank_files()
        assert True


class TestExtractUtil:
    def test_compress(self):
        compress(TMP / "retrosheet/gamelogs/gl2018.txt", TMP / "retrosheet/gamelogs",
                 remove_original=False)
