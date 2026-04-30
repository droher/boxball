# Test fixtures

Tiny sandbox of Retrosheet + Baseball Databank data that backs `BUILD_ENV=test docker compose build` and `pytest`. The fixture's job is to exercise every code path in `extract/parsers/` end-to-end without pulling 300+ MB of upstream archives.

## Inventory

| Path | Source | Notes |
|---|---|---|
| `raw/retrosheet.zip` | `https://retrosheet.org/downloads/alldata.zip` | Two-season slice (1928 + 2018). Regenerable via the builder below. |
| `raw/baseballdatabank.zip` | `tom-719/baseballdatabank` (legacy fork) | Will be rebuilt under PLE-353 against `cdalzell/Lahman` per ADR 0002. |
| `extract/retrosheet/*.zst` | committed pre-parsed output | Consumed by `tests/conftest.py:33`; downstream stages bypass the parser when running on test fixtures. |
| `extract/baseballdatabank/*.zst` | committed pre-parsed output | Same. |

## Layout contract — `raw/retrosheet.zip`

The fixture's inner directory is `retrosheet-master/` so that `tests/conftest.py:32` (`mv /tmp/{name}-master /tmp/boxball/{name}`) and `extract/Dockerfile`'s `mv retrosheet-* retrosheet` flow keep working unchanged. Inside that directory the layout matches `extract/parsers/retrosheet.py:19-20` + `:155-158`:

```
retrosheet-master/
  ballparks.csv          ← parser globs at root (parsers/retrosheet.py:156)
  biofile.csv            ← parser globs at root (parsers/retrosheet.py:157)
  gamelogs/gl<year>.txt
  schedules/<year>schedule.csv
  rosters/<TEAM><year>.ROS
  events/<year>*.EV*     ← per-team play-by-play (2018)
  events/<year>.ED*      ← deduced events (1928)
  boxes/<year>.EB*       ← box-score-only games (1928)
  allstar/<year>AS.EVE
  postseason/<year><series>.EVE
  teams/TEAM<year>
```

Year coverage:

- **1928** — deduced events (`.ED*`) plus box scores (`.EB*`) whose game ids overlap with the deduced ids by 95 games. This is the only path that exercises `remove_redundant_box_score_files` (`parsers/retrosheet.py:62-90`).
- **2018** — per-team event files (`.EV*`), the all-star game, and one wild-card postseason file. Covers `cwgame`/`cwevent`/`cwdaily` for all three `EVENT_FOLDERS`.

`biofile.csv` is truncated to the first 50 rows; the upstream copy is ~5 MB and the parser only needs a non-empty input to produce a non-empty `bio.csv.zst`.

## Regenerating

```sh
uv run python extract/fixtures/build_fixtures.py --target retrosheet
```

The builder is stdlib-only. By default it downloads `alldata.zip` from retrosheet.org (with a non-default User-Agent — retrosheet.org 403s the curl/wget defaults). Pass `--source <path>` to point at a pre-downloaded archive, e.g. when iterating offline:

```sh
uv run python extract/fixtures/build_fixtures.py --target retrosheet --source /tmp/alldata.zip
```

The builder logs the source archive's sha256 and the output zip's sha256. Record the new value in this README's checksum table after each regen.

## When to regenerate

- Upstream Retrosheet release changes the shape of `alldata.zip` (new subdir, renamed file, schema change in `ballparks.csv` / `biofile.csv` / a `*.ROS` file).
- `extract/parsers/retrosheet.py`'s layout contract changes — e.g. a new top-level glob, or `RETROSHEET_SUBDIRS` / `EVENT_FOLDERS` gains an entry.
- The chosen sample years (1928, 2018) no longer cover a glob path the parser exercises.

## Checksums

Recorded after the most recent regen. CI does not currently verify these; they exist to make accidental modification visible in PR review.

| File | sha256 |
|---|---|
| `raw/retrosheet.zip` | `9021329ee78cabb6137baaf4845c54a0510d339f16a7cbe39ee2250d2752ca49` |
| upstream `alldata.zip` (Dec 2025 release) | `88fbc6a2e179a3174d13d688b761b096671b9121f0d5e88bcdae0272557b1a14` |
| `raw/baseballdatabank.zip` | `94034e3bd043ef647968cfddb9aa2be242f8450e982626183ff98d0d96c34a3c` |
