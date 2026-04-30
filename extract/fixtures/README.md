# Test fixtures

Tiny sandbox of Retrosheet + Baseball Databank data that backs `BUILD_ENV=test docker compose build` and `pytest`. The fixture's job is to exercise every code path in `extract/parsers/` end-to-end without pulling 300+ MB of upstream archives.

## Inventory

| Path | Source | Notes |
|---|---|---|
| `raw/retrosheet.zip` | `https://retrosheet.org/downloads/alldata.zip` | Two-season slice (1928 + 2018). Regenerable via the builder below. |
| `raw/baseballdatabank.zip` | `corbtastik/lahman-baseball-db@b5e7327` | Slice of SABR Lahman v2025 (Dec 10, 2025). All 27 schema-mapped Lahman tables (1 verbatim + 26 truncated to header + 50 rows). |
| `extract/retrosheet/*.zst` | committed pre-parsed output | Consumed by `tests/conftest.py`; downstream stages bypass the parser when running on test fixtures. |
| `extract/baseballdatabank/*.zst` | committed pre-parsed output | Same. |

## Layout contract — `raw/retrosheet.zip`

Mirrors the canonical `alldata.zip` layout exactly (no inner wrapper directory) so `extract/Dockerfile`'s test stage (`unzip -d /retrosheet`) and `tests/conftest.py` land the tree at the same place the prod path does:

```
gamelogs/gl<year>.txt
schedules/<year>schedule.csv
rosters/<TEAM><year>.ROS
events/<year>*.EV*     ← per-team play-by-play (2018)
events/<year>.ED*      ← deduced events (1928)
boxes/<year>.EB*       ← box-score-only games (1928)
allstar/<year>AS.EVE
postseason/<year><series>.EVE
teams/TEAM<year>
biodata/biofile.csv    ← parser uses `**/biofile.csv` glob
biodata/ballparks.csv  ← parser uses `**/ballparks.csv` glob
```

Year coverage:

- **1928** — deduced events (`.ED*`) plus box scores (`.EB*`) whose game ids overlap with the deduced ids by 95 games. This is the only path that exercises `remove_redundant_box_score_files` in `parsers/retrosheet.py`.
- **2018** — per-team event files (`.EV*`), the all-star game, and one wild-card postseason file. Covers `cwgame`/`cwevent`/`cwdaily` for all three `EVENT_FOLDERS`.

`biofile.csv` is truncated to the first 50 rows; the upstream copy is ~5 MB and the parser only needs a non-empty input to produce a non-empty `bio.csv.zst`.

## Layout contract — `raw/baseballdatabank.zip`

CSVs at the zip root (no wrapper directory). Both the Dockerfile test stage (`unzip -d /baseballdatabank/core`) and `tests/conftest.py` land them under `BOXBALL_BASEBALLDATABANK_CORE_PATH`. All 27 schema-mapped Lahman tables are included so the downstream `parquet` stage finds an input for every metadata table:

- `AllstarFull.csv` ships verbatim — it carries the Negro Leagues `9;9` rows in `startingPos` that exercise the parser's row-fixup path.
- The other 26 CSVs are truncated to header + first 50 rows. That keeps the fixture under 100 KB while every depascalized file produced by `parsers/baseballdatabank.py` is non-empty and every parquet/load-target stage finds the file it expects.

## Regenerating

```sh
uv run python extract/fixtures/build_fixtures.py --target retrosheet
uv run python extract/fixtures/build_fixtures.py --target baseballdatabank
```

The builder is stdlib-only. By default it downloads each source archive directly from upstream (`retrosheet.org` for Retrosheet — with a non-default User-Agent because retrosheet.org 403s the curl/wget defaults; GitHub for `corbtastik/lahman-baseball-db`). Pass `--source <path>` to point at a pre-downloaded archive, e.g. when iterating offline:

```sh
uv run python extract/fixtures/build_fixtures.py --target retrosheet --source /tmp/alldata.zip
uv run python extract/fixtures/build_fixtures.py --target baseballdatabank --source /tmp/lahman.zip
```

The builder logs the source archive's sha256 and the output zip's sha256. Record the new values in this README's checksum table after each regen.

## When to regenerate

- Upstream Retrosheet release changes the shape of `alldata.zip` (new subdir, renamed file, schema change in `ballparks.csv` / `biofile.csv` / a `*.ROS` file).
- A new Lahman release lands in `corbtastik/lahman-baseball-db` (or wherever the data lives) — bump `BASEBALLDATABANK_FIXTURE_SHA` in the builder + rerun.
- Either parser's layout contract changes — e.g. a new top-level glob, or `RETROSHEET_SUBDIRS` / `EVENT_FOLDERS` gains an entry.
- The chosen sample years (1928, 2018) no longer cover a glob path the parser exercises.

## Checksums

Recorded after the most recent regen. CI does not currently verify these; they exist to make accidental modification visible in PR review.

| File | sha256 |
|---|---|
| `raw/retrosheet.zip` | `b5587b36464598730b73b9396d7a17216022d7504e78c3cefc382048bcf26281` |
| upstream `alldata.zip` (Dec 2025 release) | `88fbc6a2e179a3174d13d688b761b096671b9121f0d5e88bcdae0272557b1a14` |
| `raw/baseballdatabank.zip` | `5b12b3dc56286ac886293bdc412923a9b07c9d86295af8346d69c185a7b1fcdd` |
| upstream `corbtastik/lahman-baseball-db@b5e7327` archive | `fb14eeceda8450760a9d3a94a26cacf210b029b4de2f8e2d978398f5498361e3` |
