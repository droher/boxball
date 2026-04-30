"""Regenerate fixture archives under ``extract/fixtures/raw/``.

Stdlib only. Run from repo root::

    uv run python extract/fixtures/build_fixtures.py --target retrosheet
    uv run python extract/fixtures/build_fixtures.py --target baseballdatabank

Source-of-truth bytes are pulled directly from the same upstream URLs the
prod Dockerfile uses (per ADR 0002 + the PLE-353 revision):

    Retrosheet      → https://retrosheet.org/downloads/alldata.zip
    BaseballDatabank → corbtastik/lahman-baseball-db (Lahman v2025, CSV layout)

Each fixture's inner layout mirrors the matching Dockerfile test stage's
``unzip -d`` target: retrosheet ships the canonical alldata.zip top-level
tree (gamelogs/, events/, biodata/, …) at the zip root; baseballdatabank
ships the Lahman v2025 CSVs at the zip root and the test stage rehomes them
under ``/baseballdatabank/core/`` on the way in. Fixtures stay tiny by
slicing two seasons (1928 + 2018) and trimming biofile.csv to the first 50
rows. Per-entry timestamps are pinned so a regen against the same source
yields a byte-identical zip.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import logging
import sys
import urllib.request
import zipfile
from collections.abc import Iterable
from pathlib import Path

logger = logging.getLogger("build_fixtures")

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURES_RAW = REPO_ROOT / "extract" / "fixtures" / "raw"

ALLDATA_URL = "https://retrosheet.org/downloads/alldata.zip"
USER_AGENT = "Mozilla/5.0 (compatible; boxball-build)"

# Two seasons cover every parser code path while keeping the zip in low single-
# digit MB:
#   1928 → deduced events (.ED*) + box scores (.EB*) with natural game-id overlap
#          that exercises ``remove_redundant_box_score_files``.
#   2018 → per-team event files (.EV*), all-star, postseason.
SAMPLE_YEARS: tuple[int, ...] = (1928, 2018)

# Members copied verbatim from the source archive into the fixture, preserving
# their canonical paths so the fixture mirrors the alldata.zip layout exactly.
ROOT_FILES: tuple[str, ...] = (
    "biodata/ballparks.csv",
)

# Per-year event/box/allstar/postseason members.
EVENT_MEMBERS: dict[int, tuple[str, ...]] = {
    1928: (
        "events/1928.EDA",
        "events/1928.EDN",
        "boxes/1928.EBA",
        "boxes/1928.EBN",
    ),
    2018: (
        # A handful of teams give cwdaily/cwgame/cwevent enough material without
        # ballooning the zip to the full 30-team season.
        "events/2018WAS.EVN",
        "events/2018HOU.EVA",
        "events/2018BOS.EVA",
        "events/2018NYA.EVA",
        "allstar/2018AS.EVE",
        "postseason/2018ALWC.EVE",
    ),
}

# Truncated biofile.csv — full upstream copy is ~5 MB; keep just enough rows for
# the parser's ``concat_files`` path to produce a non-empty bio.csv.zst.
BIOFILE_ROW_LIMIT = 50

# Baseball Databank fixture sources: corbtastik/lahman-baseball-db. Pin the SHA
# so a regen is reproducible; bump alongside .env's BASEBALLDATABANK_VERSION
# when refreshing data.
BASEBALLDATABANK_FIXTURE_SHA = "b5e7327707fff91ff3bdcbe1f6892c8c5015cf1d"
BASEBALLDATABANK_URL = (
    f"https://github.com/corbtastik/lahman-baseball-db/archive/{BASEBALLDATABANK_FIXTURE_SHA}.zip"
)
# All 27 Lahman CSVs are included so the parquet stage finds every schema-mapped
# input. Most are truncated; AllstarFull is shipped verbatim because it carries
# the Negro Leagues `9;9` starting_pos rows that exercise the parser's row-level
# fixup path (parsers/baseballdatabank.py::_strip_multi_position_starting_pos).
BASEBALLDATABANK_VERBATIM_FILES: tuple[str, ...] = (
    "AllstarFull.csv",
)
BASEBALLDATABANK_TRUNCATED_FILES: tuple[str, ...] = (
    "Appearances.csv",
    "AwardsManagers.csv",
    "AwardsPlayers.csv",
    "AwardsShareManagers.csv",
    "AwardsSharePlayers.csv",
    "Batting.csv",
    "BattingPost.csv",
    "CollegePlaying.csv",
    "Fielding.csv",
    "FieldingOF.csv",
    "FieldingOFsplit.csv",
    "FieldingPost.csv",
    "HallOfFame.csv",
    "HomeGames.csv",
    "Managers.csv",
    "ManagersHalf.csv",
    "Parks.csv",
    "People.csv",
    "Pitching.csv",
    "PitchingPost.csv",
    "Salaries.csv",
    "Schools.csv",
    "SeriesPost.csv",
    "Teams.csv",
    "TeamsFranchises.csv",
    "TeamsHalf.csv",
)
BASEBALLDATABANK_TRUNCATE_ROWS = 50


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _download(url: str) -> bytes:
    logger.info("Downloading %s", url)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req) as resp:  # noqa: S310 — pinned URL
        body = resp.read()
    logger.info("Downloaded %d bytes (sha256=%s)", len(body), _sha256(body))
    return body


def _rosters_for_year(names: Iterable[str], year: int) -> list[str]:
    """Find ``rosters/<TEAM><year>.ROS`` members. Year is the last 4 of the stem."""
    target = f"{year}.ROS"
    return [n for n in names if n.startswith("rosters/") and n.endswith(target)]


def _build_retrosheet_payload(source: zipfile.ZipFile) -> dict[str, bytes]:
    """Return mapping of fixture-relative path → bytes, sourced from ``alldata.zip``."""

    names = source.namelist()
    payload: dict[str, bytes] = {}

    # Verbatim files at canonical paths.
    for member in ROOT_FILES:
        payload[member] = source.read(member)

    # Truncated biofile.csv (header + first N rows), kept at canonical path.
    bio_full = source.read("biodata/biofile.csv").splitlines(keepends=True)
    if len(bio_full) <= 1:
        raise RuntimeError("biodata/biofile.csv is empty or header-only")
    payload["biodata/biofile.csv"] = b"".join(bio_full[: 1 + BIOFILE_ROW_LIMIT])
    logger.info(
        "biodata/biofile.csv: %d rows (truncated from %d) → %d bytes",
        BIOFILE_ROW_LIMIT,
        len(bio_full) - 1,
        len(payload["biodata/biofile.csv"]),
    )

    # Per-year event / box / allstar / postseason members.
    for year, members in EVENT_MEMBERS.items():
        for member in members:
            payload[member] = source.read(member)

    # Gamelogs + schedules + teams + rosters per sample year.
    for year in SAMPLE_YEARS:
        gamelog = f"gamelogs/gl{year}.txt"
        payload[gamelog] = source.read(gamelog)

        schedule = f"schedules/{year}schedule.csv"
        payload[schedule] = source.read(schedule)

        team_file = f"teams/TEAM{year}"
        payload[team_file] = source.read(team_file)

        rosters = _rosters_for_year(names, year)
        if not rosters:
            raise RuntimeError(f"No roster files found for {year}")
        for roster in rosters:
            payload[roster] = source.read(roster)

    # Sanity: deduced ∩ pbp game-id overlap. The parser raises ValueError if
    # deduced and event game ids overlap, so we need the two streams disjoint;
    # but we *do* want box-score game ids to overlap with deduced/event ids so
    # ``remove_redundant_box_score_files`` exercises its remove path. Compute
    # the overlap and log it as a smoke check.
    _check_overlap_invariants(payload)

    return payload


def _ids_in(payload: dict[str, bytes], suffixes: tuple[str, ...]) -> set[str]:
    ids: set[str] = set()
    for path, body in payload.items():
        if not any(path.endswith(s) for s in suffixes):
            continue
        for raw in body.splitlines():
            if raw.startswith(b"id,"):
                parts = raw.split(b",", 2)
                if len(parts) >= 2:
                    ids.add(parts[1].strip().decode("ascii"))
    return ids


def _check_overlap_invariants(payload: dict[str, bytes]) -> None:
    event_ids = _ids_in(payload, suffixes=(".EVA", ".EVN", ".EVE"))
    deduced_ids = _ids_in(payload, suffixes=(".EDA", ".EDN", ".EDE"))
    box_ids = _ids_in(payload, suffixes=(".EBA", ".EBN", ".EBE"))

    if event_ids & deduced_ids:
        sample = sorted(event_ids & deduced_ids)[:5]
        raise RuntimeError(
            f"Sampled events overlap deduced — parser would raise ValueError: {sample}"
        )

    pbp_ids = event_ids | deduced_ids
    box_overlap = pbp_ids & box_ids
    if not box_overlap:
        raise RuntimeError(
            "Sampled box scores share no game ids with sampled PBP — remove_redundant_box_score_files would no-op."
        )

    logger.info(
        "Game-id invariants ok: events=%d deduced=%d boxes=%d redundant_overlap=%d",
        len(event_ids),
        len(deduced_ids),
        len(box_ids),
        len(box_overlap),
    )


def _build_baseballdatabank_payload(source: zipfile.ZipFile) -> dict[str, bytes]:
    """Return fixture mapping for the Lahman v2025 CSV slice. CSVs at zip root."""

    names = source.namelist()
    # corbtastik archive is wrapped in lahman-baseball-db-<sha>/. Build a name
    # map so we can address by basename.
    by_basename: dict[str, str] = {}
    for n in names:
        if n.endswith("/"):
            continue
        base = n.rsplit("/", 1)[-1]
        if base in by_basename:
            raise RuntimeError(f"Ambiguous basename in archive: {base}")
        by_basename[base] = n

    payload: dict[str, bytes] = {}

    for fname in BASEBALLDATABANK_VERBATIM_FILES:
        if fname not in by_basename:
            raise RuntimeError(f"Missing fixture source: {fname}")
        payload[fname] = source.read(by_basename[fname])

    for fname in BASEBALLDATABANK_TRUNCATED_FILES:
        if fname not in by_basename:
            raise RuntimeError(f"Missing fixture source: {fname}")
        body = source.read(by_basename[fname])
        rows = body.splitlines(keepends=True)
        if len(rows) <= 1:
            raise RuntimeError(f"{fname} is header-only or empty")
        truncated = b"".join(rows[: 1 + BASEBALLDATABANK_TRUNCATE_ROWS])
        payload[fname] = truncated
        logger.info(
            "%s: %d rows (truncated from %d) → %d bytes",
            fname,
            BASEBALLDATABANK_TRUNCATE_ROWS,
            len(rows) - 1,
            len(truncated),
        )

    _check_baseballdatabank_invariants(payload)
    return payload


def _check_baseballdatabank_invariants(payload: dict[str, bytes]) -> None:
    """Verify each CSV has body rows AND its header column count matches the
    SQLAlchemy schema's non-autoincrement column count for the matching table.
    The column-count match is the load-bearing check — a truncation that lops
    or duplicates a column would otherwise silently produce a fixture that
    only fails downstream at parquet conversion time.
    """

    # Lazy import — keeps the build script stdlib-only at module load and only
    # touches the schema package at fixture-rebuild time.
    import sys as _sys
    transform_src = REPO_ROOT / "transform"
    _sys.path.insert(0, str(transform_src))
    try:
        from src.boxball_schemas import baseballdatabank_metadata
    finally:
        _sys.path.pop(0)

    schema_col_counts = {
        tbl.name: sum(1 for c in tbl.columns.values() if c.autoincrement is not True)
        for tbl in baseballdatabank_metadata.tables.values()
    }
    # Map fixture filename → table name via the same depascalize transform the
    # parser applies (parsers/baseballdatabank.py).
    import humps  # already a runtime dep of the parser; available under uv

    for name, body in payload.items():
        text = body.decode("utf-8-sig", errors="strict")
        rows = list(csv.reader(io.StringIO(text)))
        if len(rows) < 2:
            raise RuntimeError(f"{name} has no body rows")

        depascalized = humps.depascalize(name.replace("OFs", "OfS").replace("OF", "Of"))
        table_name = depascalized.removesuffix(".csv")
        expected = schema_col_counts.get(table_name)
        if expected is None:
            raise RuntimeError(f"{name} has no matching schema table ({table_name})")
        actual = len(rows[0])
        if actual != expected:
            raise RuntimeError(
                f"{name}: header column count {actual} != schema {expected} for "
                f"baseballdatabank.{table_name}"
            )
    logger.info(
        "Baseball Databank fixture invariants ok across %d files (column counts match schema)",
        len(payload),
    )


def _write_zip(payload: dict[str, bytes], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Pin per-entry timestamp so re-runs against the same source produce a
    # byte-identical fixture (zipfile defaults to current time).
    fixed_dt = (2026, 1, 1, 0, 0, 0)
    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for relpath, body in sorted(payload.items()):
            info = zipfile.ZipInfo(filename=relpath, date_time=fixed_dt)
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, body)
    logger.info(
        "Wrote %s — %d files, %d bytes, sha256=%s",
        out_path,
        len(payload),
        out_path.stat().st_size,
        _sha256(out_path.read_bytes()),
    )


def build_retrosheet(out_path: Path, source_zip: Path | None) -> None:
    if source_zip is None:
        body = _download(ALLDATA_URL)
    else:
        logger.info("Reading source archive from %s", source_zip)
        body = source_zip.read_bytes()
        logger.info("Source size %d bytes (sha256=%s)", len(body), _sha256(body))

    with zipfile.ZipFile(io.BytesIO(body)) as src:
        payload = _build_retrosheet_payload(src)
    _write_zip(payload, out_path)


def build_baseballdatabank(out_path: Path, source_zip: Path | None) -> None:
    if source_zip is None:
        body = _download(BASEBALLDATABANK_URL)
    else:
        logger.info("Reading source archive from %s", source_zip)
        body = source_zip.read_bytes()
        logger.info("Source size %d bytes (sha256=%s)", len(body), _sha256(body))

    with zipfile.ZipFile(io.BytesIO(body)) as src:
        payload = _build_baseballdatabank_payload(src)
    _write_zip(payload, out_path)


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument(
        "--target",
        choices=("retrosheet", "baseballdatabank"),
        required=True,
        help="Which fixture to rebuild.",
    )
    _ = parser.add_argument(
        "--source",
        type=Path,
        default=None,
        help=(
            "Optional path to a pre-downloaded source archive. If omitted, the "
            "builder fetches it from the canonical upstream URL."
        ),
    )
    _ = parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Override output path. Defaults to extract/fixtures/raw/<target>.zip.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    args = _parse_args(argv)
    if args.target == "retrosheet":
        out = args.out or FIXTURES_RAW / "retrosheet.zip"
        build_retrosheet(out_path=out, source_zip=args.source)
    elif args.target == "baseballdatabank":
        out = args.out or FIXTURES_RAW / "baseballdatabank.zip"
        build_baseballdatabank(out_path=out, source_zip=args.source)
    else:  # pragma: no cover - argparse choices guard
        raise AssertionError(f"unhandled target {args.target}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
