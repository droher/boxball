"""Regenerate fixture archives under ``extract/fixtures/raw/``.

Stdlib only. Run from repo root::

    uv run python extract/fixtures/build_fixtures.py --target retrosheet

Source of truth for retrosheet bytes is the canonical
``https://retrosheet.org/downloads/alldata.zip`` per ADR 0002. The fixture is a
small slice of that archive — two seasons (1928 + 2018) chosen to exercise every
parser code path: deduced events (.ED*), per-team event files (.EV*), all-star,
postseason, gamelogs, schedules, rosters, and box scores (.EB*) whose game ids
overlap with the deduced events so ``remove_redundant_box_score_files`` actually
exercises its remove path.

The fixture's inner directory is normalized to ``retrosheet-master/`` so that
``tests/conftest.py`` and ``extract/Dockerfile``'s ``mv retrosheet-* retrosheet``
flow keep working unchanged.
"""

from __future__ import annotations

import argparse
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

INNER_DIR = "retrosheet-master"

# Two seasons cover every parser code path while keeping the zip in low single-
# digit MB:
#   1928 → deduced events (.ED*) + box scores (.EB*) with natural game-id overlap
#          that exercises ``remove_redundant_box_score_files``.
#   2018 → per-team event files (.EV*), all-star, postseason.
SAMPLE_YEARS: tuple[int, ...] = (1928, 2018)

# Members copied verbatim from the source archive into the fixture root.
ROOT_FILES: tuple[tuple[str, str], ...] = (
    # The parser globs at the retrosheet-root level for these two; alldata.zip
    # nests them under ``biodata/``, so we flatten on the way in.
    ("biodata/ballparks.csv", "ballparks.csv"),
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

    # Verbatim root files (ballparks.csv).
    for src, dest in ROOT_FILES:
        payload[dest] = source.read(src)

    # Truncated biofile.csv (header + first N rows).
    bio_full = source.read("biodata/biofile.csv").splitlines(keepends=True)
    if len(bio_full) <= 1:
        raise RuntimeError("biodata/biofile.csv is empty or header-only")
    payload["biofile.csv"] = b"".join(bio_full[: 1 + BIOFILE_ROW_LIMIT])
    logger.info(
        "biofile.csv: %d rows (truncated from %d) → %d bytes",
        BIOFILE_ROW_LIMIT,
        len(bio_full) - 1,
        len(payload["biofile.csv"]),
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


def _write_zip(payload: dict[str, bytes], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Pin per-entry timestamp so re-runs against the same source produce a
    # byte-identical fixture (zipfile defaults to current time).
    fixed_dt = (2026, 1, 1, 0, 0, 0)
    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for relpath, body in sorted(payload.items()):
            info = zipfile.ZipInfo(filename=f"{INNER_DIR}/{relpath}", date_time=fixed_dt)
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


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument(
        "--target",
        choices=("retrosheet",),
        required=True,
        help="Which fixture to rebuild.",
    )
    _ = parser.add_argument(
        "--source",
        type=Path,
        default=None,
        help=(
            "Optional path to a pre-downloaded alldata.zip. If omitted, the "
            "builder fetches it from retrosheet.org."
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
    else:  # pragma: no cover - argparse choices guard
        raise AssertionError(f"unhandled target {args.target}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
