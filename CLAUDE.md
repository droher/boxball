# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Boxball builds prepopulated databases of two open-source baseball datasets (Retrosheet play-by-play + Baseball Databank/Lahman seasonal stats). Output is a family of Docker images (`doublewick/boxball:<target>-<version>`) plus flat-file Parquet/CSV downloads. The repo is the build pipeline, not a runtime app — there is no server to start; "running" the project means building images via `docker compose`.

## Workflow — Boxball 2026 Refresh

Refresh tickets (PLE-33x/35x/36x/37x) ship **locally only** — no GitHub PRs during the refresh phase.

- Per-ticket branch: `feature/ple-XXX-<slug>` (matches Linear `gitBranchName`).
- Squash-merge each ticket branch into the long-lived local `next` branch.
- Do **not** push refresh branches (or `next`) to `origin`. Feature branches may be pushed for backup, but never opened as PRs. `next` stays local until release-time cutover.
- `master` and Docker Hub tags / README badges / release notes flip in a single batch when the refresh is shippable. Until then, master stays untouched.
- CI runs locally via `make ci` (see below). No `gh pr create`, no GitHub Actions runs against this work.

## Local CI — `act`

`make ci` runs `.github/workflows/ci.yml` locally inside Docker via [`act`](https://github.com/nektos/act). Same workflow file, same runner image (`catthehacker/ubuntu:act-latest`). High-fidelity local rehearsal — not byte-identical to GitHub-hosted runners (cache action, buildx, and docker-in-docker behavior diverge), so final source of truth is GitHub Actions when we cut over to master.

```
make ci                # full pipeline (style → int-test → e2e-test)
make ci-style          # one job
make ci-int-test
make ci-e2e-test
make ci-list           # list jobs without running
```

Requires `act` (`brew install act`) + a running Docker daemon. `.actrc` pins `linux/amd64` for reproducibility on M-series and forwards the host Docker socket so the e2e job's `docker compose build` works against the host daemon.

Schemas are SQLAlchemy-defined and authoritative. DDL for every target dialect (Postgres, Postgres+cstore_fdw, MySQL, SQLite, Clickhouse) is generated from the same metadata.

## Pipeline architecture

Three stages, each its own Docker context, chained via multi-stage builds:

1. **`extract/`** — Downloads pinned Retrosheet + Baseball Databank archives (versions in `.env`), builds Chadwick from source, runs `cwdaily/cwgame/cwevent/cwsub/cwcomment` over Retrosheet event files to produce CSVs, depascalizes Databank CSVs. Output: zstd-compressed CSVs under `/extract/{retrosheet,baseballdatabank}/`. Entry points: `extract/parsers/retrosheet.py`, `extract/parsers/baseballdatabank.py`.
2. **`transform/`** — Two parallel branches from the extract image:
   - `csv.Dockerfile` — passthrough (currently identity; placeholder for cleaning steps).
   - `parquet.Dockerfile` — runs `transform/src/parquet.py` to convert each zstd-CSV into a Parquet file using the SQLAlchemy schema as the type contract (PyArrow streaming reader, zstd compression).
   - `ddl.Dockerfile` — runs `transform/src/ddl_maker.py`, which iterates `all_factories × all_metadata` and writes one `.sql` (or `.sql`-like) file per target into `/ddl/`.
3. **`load/`** — One Dockerfile (`load/Dockerfile`) with a stage per target DB. Each stage `FROM`s the official DB image, copies the matching `/ddl/<target>.sql` into `/docker-entrypoint-initdb.d/`, copies CSV or Parquet from the relevant transform stage, and lets the DB's init mechanism load on first container start. Per-target shell/SQL hooks live under `load/<target>/` (named `A_*` to run before the generated DDL, `z_*` to run after, alphabetically).

The `docker-compose.yml` wires this up — every service uses YAML anchors (`x-extract`, `x-postgres`, …) and each has a `<svc>-latest` twin that retags `${VERSION}` → `latest`. `depends_on` reflects the build DAG (`parquet`/`csv` → `extract`; DB targets → `csv`+`ddl` or `parquet`+`ddl`).

## DDL factory pattern

`transform/src/target_ddl_factory.TargetDdlFactory` is the abstract base. Each target subclass provides:
- `target_name` (output filename stem) and `dialect` (SQLAlchemy `Dialect`, or `None` if hand-rolled).
- `metadata_transform(metadata)` — overridable rewrite of the SQLAlchemy `MetaData` before DDL emit. Used to e.g. flatten schemas into table-name prefixes for SQLite/cstore_fdw, swap engines for Clickhouse, drop `dummy_id` autoincrement PKs that don't translate.
- `make_copy_ddl(metadata)` — emits the loader statements (`COPY FROM PROGRAM`, `LOAD DATA INFILE`, `.import`, etc.) tailored per dialect's NULL/bool/CSV quirks.

When adding a new target, subclass `TargetDdlFactory`, register it in `transform/src/ddl_factories/__init__.py::all_factories`, and add a stage in `load/Dockerfile` + service entry in `docker-compose.yml`.

When changing a schema column, edit `transform/src/boxball_schemas/{retrosheet,baseballdatabank}.py` — every target's DDL re-emits from there. The `dummy_id = Column(Integer, autoincrement=True, primary_key=True)` pattern is intentional: tables without natural PKs use it, and every target factory strips it because most loaders can't autoincrement during bulk load.

## Build / run

`.env` defines `VERSION`, `REPO`, dataset SHAs, and `BUILD_ENV` (`prod` pulls real data; `test` uses tiny fixtures from `extract/fixtures/raw/`). Compose reads it automatically.

```
docker compose build extract                      # extract stage only
docker compose build parquet ddl                  # transform outputs
docker compose build postgres-cstore-fdw          # full chain to one DB target
docker compose build                              # all targets

BUILD_ENV=test docker compose build               # CI smoke build with fixtures
```

To run a built image, see the `docker run` recipes in `README.md` — they mount `~/boxball/<target>/` for persistence and expose the DB's standard port.

## Tests

Top-level `requirements.txt` is for the host test runner (not used inside Docker stages — those have their own per-stage requirements). Tests assume Python 3.7-ish (per `.circleci/config.yml`); mostly compatibility checks rather than deep correctness.

```
pip install -r requirements.txt
pytest --cov                                      # full suite (mirrors CI int-test job)
pytest tests/test_transform.py::TestSchemas       # one class
pytest tests/test_extract.py -k parse_simples     # one test
flake8                                            # style (config in .flake8, ignores E741/E731, max-line=120)
```

`tests/conftest.py` unpacks `extract/fixtures/raw/*.zip` into `/tmp/boxball/` and `chdir`s there; tests run against fixture data only. The fixture path mirrors the in-container layout, so the same parser/transform code works in both.

CI (`.circleci/config.yml`) runs `style` (flake8) → `int-test` (pytest+coverage) → `e2e-test` (`BUILD_ENV=test docker compose build`).

## Gotchas

- `transform/src/__init__.py` defines `OUTPUT_PATH = Path("ddl")` etc. as **relative** paths. `ddl_maker.py` and `parquet.py` are run with the working directory set by their Dockerfiles; running them from the host requires matching CWD or these paths break.
- `transform/src/boxball_schemas/` is also packaged standalone as the `boxball-schemas` PyPI package (see `transform/src/setup.py`) — keep it import-clean of the rest of `transform/src/`.
- Retrosheet is fetched from `droher/retrosheet-mirror` (a fork) rather than upstream, pinned by SHA in `.env`. Baseball Databank similarly pinned to a fork (`tom-719/baseballdatabank`) per a comment in `extract/Dockerfile` waiting on upstream 2023 data.
- The `postgres-cstore-fdw` target is pinned to Postgres 13 because cstore_fdw isn't packaged for newer versions; plain `postgres` runs on 16.
- `load/<target>/` shell scripts rely on alphabetical execution order in `/docker-entrypoint-initdb.d/` — the `A_` / `z_` prefixes are load-bearing, not cosmetic.
- MySQL CSV loader needs explicit per-column `IF(@col = '', NULL, @col)` because MySQL won't treat blank fields as NULL; floats also need an `inf` guard. See `transform/src/ddl_factories/mysql.py`.
