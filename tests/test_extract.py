from unittest.mock import patch
from pathlib import Path

from parsers import retrosheet as retrosheet_mod
from parsers.retrosheet import (
    PARSE_FUNCS,
    RetrosheetParser,
    all_pbp_game_ids,
    deduced_game_ids,
    event_game_ids,
    remove_redundant_box_score_files,
)
from parsers.baseballdatabank import (
    ROW_FIXUPS,
    _strip_multi_position_starting_pos,
    get_baseballdatabank_files,
)
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

    def test_remove_redundant_box_score_strips_game_id(self, tmp_path):
        # Box-score `id,` rows can carry trailing whitespace/newline.
        # Without `.strip()` on game_id, no overlap with pbp_ids would be
        # detected and 0 accounts would be removed even when ids match.
        pbp_dir = tmp_path / "boxes"
        pbp_dir.mkdir()
        ed_file = pbp_dir / "1928CHN.ED"
        ed_file.write_text("id,CHN192801010\nversion,2\n")
        # Use CRLF: retrosheet files historically ship with DOS line endings,
        # so the strip must drop \r as well as \n.
        eb_file = pbp_dir / "1928CHN.EB"
        eb_file.write_bytes(
            b"id,CHN192801010\r\ninfo,visteam,BSN\r\n"
            b"id,CHN192801020\r\ninfo,visteam,BSN\r\n"
        )

        all_pbp_game_ids.cache_clear()
        deduced_game_ids.cache_clear()
        event_game_ids.cache_clear()
        try:
            with patch.object(retrosheet_mod, "RETROSHEET_PATH", tmp_path):
                remove_redundant_box_score_files()
        finally:
            all_pbp_game_ids.cache_clear()
            deduced_game_ids.cache_clear()
            event_game_ids.cache_clear()

        remaining = eb_file.read_text()
        assert "CHN192801010" not in remaining, (
            "overlapping box-score id should have been removed; .strip() regression?"
        )
        assert "CHN192801020" in remaining, "non-overlapping id must be preserved"


class TestBaseballDatabank:
    def test_get_baseballdatabank_files(self):
        get_baseballdatabank_files()
        assert True

    def test_starting_pos_index_matches_schema(self):
        # The fixup writes to a hardcoded index — guard it against schema drift
        # by deriving the expected position from the SQLAlchemy schema.
        from src.boxball_schemas.baseballdatabank import AllstarFull
        non_autoinc = [c.name for c in AllstarFull.__table__.columns if c.autoincrement is not True]
        assert non_autoinc.index("starting_pos") == 7, \
            "starting_pos position drifted; update _strip_multi_position_starting_pos"

    def test_strip_multi_position_collapses_to_first_int(self):
        row = ["wrighwi01", "1942", "0", "", "BEG", "EAS", "2", "9;9"]
        out = _strip_multi_position_starting_pos(list(row))
        assert out == ["wrighwi01", "1942", "0", "", "BEG", "EAS", "2", "9"]

    def test_strip_multi_position_passes_through_clean_values(self):
        row = ["aaronha01", "1955", "0", "ALS195507120", "ML1", "NL", "1", "8"]
        assert _strip_multi_position_starting_pos(list(row)) == row

    def test_strip_multi_position_passes_through_blank_starting_pos(self):
        row = ["banksern01", "1956", "0", "", "CHN", "NL", "1", ""]
        assert _strip_multi_position_starting_pos(list(row)) == row

    def test_row_fixups_registers_allstar_full(self):
        assert "allstar_full" in ROW_FIXUPS
        assert ROW_FIXUPS["allstar_full"] is _strip_multi_position_starting_pos


class TestExtractUtil:
    def test_compress(self):
        compress(TMP / "retrosheet/gamelogs/gl2018.txt", TMP / "retrosheet/gamelogs",
                 remove_original=False)
