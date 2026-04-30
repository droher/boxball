# Boxball 2026 Refresh — Execution Plan

Linear project: [Boxball 2026 Refresh](https://linear.app/plenary-horse/project/boxball-2026-refresh-ab8262942e21)

## Milestones

| # | Name | Done criteria |
|---|---|---|
| **M1** | Modernize Foundation | `BUILD_ENV=test docker compose build` green on py3.13 / GHA for every kept target, amd64+arm64. Drill dropped, cstore_fdw replaced, structured logging, CWD paths fixed. |
| **M2** | Refresh Data and Images | `doublewick/boxball:<target>-<NEW_VERSION>` + `latest` on Docker Hub for postgres, columnar-pg, mysql, sqlite, clickhouse with current upstream data. Concurrent with M3. |
| **M3** | Automate Shipping and UX | One real release shipped end-to-end auto. README rewritten with quickstart + decision matrix + freshness badge. Concurrent with M2. |

Order: **M1 strict gate → M2 ∥ M3**.

## Wave plan

### Wave 0 — Unblock everything (serial; M1)

1. **PLE-332** Migrate CI to GH Actions — gates every downstream PR's validation. Scope to workflow file only (see dupe flag).
2. **PLE-333** Author `ci.yml` — sub-task of 332; collapse or land together.
3. **PLE-334** Bump Python to 3.13 across Dockerfiles + GHA + host. Land before deps churn. **(PLE-335 collapsed in.)**
4. **PLE-336** Modernize per-stage Python deps — needs 334's interpreter bump first.
5. **PLE-377** Modernize dev dependency stack (uv, ruff, basedpyright) — sibling to 336; lands after/with it. Promotes ruff config into `pyproject.toml`, adds uv lockfile, adds basedpyright baseline.
6. **PLE-351** Fix CWD-coupled relative paths in `transform/src/__init__.py` — small, removes footgun before later refactors.

### Wave 1 — Spikes in parallel (M1; decisions block downstream)

- **PLE-331** Spike: Hydra vs Citus columnar (blocks PLE-338/339/340/341)
- **PLE-352** Spike: validate upstream Retrosheet/Databank as direct sources (blocks PLE-353/354)

Both research, no code conflict. Run concurrent.

### Wave 2 — Foundation cleanups (parallel-safe after Wave 0; M1)

- **PLE-337** Drop Drill target
- **PLE-347 → 348 → 349 → 350** Structured logging chain (348 = shared module)

### Wave 3 — Columnar replacement (after PLE-331; M1)

- **PLE-338** Replace `postgres-cstore-fdw` with chosen columnar
- **PLE-339** Add columnar target factory
- **PLE-340** Load stage Dockerfile + init scripts
- **PLE-341** Update compose, delete cstore_fdw entries
- **PLE-342** README + ADR cross-link

### Wave 4 — Multi-arch (after Wave 3 stable; M1)

- **PLE-344** Compose platforms + Dockerfile bases
- **PLE-345** Buildx wiring in GH Actions
- **PLE-346** Verify arm64 init scripts
- **PLE-343** Parent multi-arch ticket closes

### Wave 5 — M2 Data refresh (after PLE-352)

- **PLE-353** Repoint extract sources upstream
- **PLE-354** Bump VERSION + data SHAs
- **PLE-355** Validate fixture coverage
- **PLE-356** ← **defer** until release workflow exists (PLE-358)

### Wave 6 — Shipping infra (M3; can start parallel to Wave 5 once Wave 0 done)

- **PLE-357** Provision DH + PyPI creds (manual, do early)
- **PLE-358 → 359** Release workflow + multi-arch push job
- **PLE-360** Flat-file bundle + GH Release upload
- **PLE-361** Release notes from CHANGELOG
- **PLE-356** First real release at new VERSION (now unblocked)

### Wave 7 — Schema PyPI auto-publish (M3)

- **PLE-362 → 363 → 364** boxball-schemas auto-publish chain

### Wave 8 — Auto-rebuild on upstream change (M3)

- **PLE-365 → 366 → 367 → 368 → 369** Daily SHA poll → PR → auto-tag → live test cycle

### Wave 9 — Docs & polish (M3; last)

- **PLE-370 → 371 → 372 → 373** README rewrite chain
- **PLE-374** Load-progress visibility
- **PLE-375** Freshness badge
- **PLE-376** SQLite on-ramp framing

## Critical path

```
332 → 334 → 336 → 377 → 331 → 338 → 358 → 356 → 365-chain → docs
```

## Dupe / scope flags

- **PLE-332** AC overlaps PLE-334 (py3.13) + PLE-335 (delete CircleCI). Decision: keep PLE-332 scoped to ci.yml only; PLE-335 collapsed into PLE-334 (AC depended on each other — see PLE-334 done note).
- **PLE-343** parent of 344/345/346. Close on child completion.
- **PLE-347** parent of 348/349/350. Same.
- **PLE-365** parent of 366/367/368/369. Same.
- **PLE-370** parent of 371/372/373. Same.

## Cross-issue dependencies (prose-only; no Linear `blockedBy` set)

- PLE-338 → PLE-331 (spike picks columnar engine)
- PLE-353 → PLE-352 (spike validates upstream sources)
- PLE-356 → PLE-358 (needs release workflow)
- All downstream PRs → PLE-332 ("CI must move first")

## Workflow conventions

- New branch per issue: `feature/ple-XXX-<slug>` (matches Linear `gitBranchName`).
- Mark issue **In Progress** in Linear at branch creation; **Done** at local squash-merge into `next`.
- No GitHub PRs during refresh phase. Code review subagent runs locally before each squash-merge.
- CI runs locally via `make ci` (act). No GH Actions runs until cutover.
- Update CLAUDE.md / README / this PLAN.md when scope shifts.
- Squash-merge into `next` (long-lived local integration branch; not pushed to origin). `next` → `master` is a single batched cutover at release time.

## Status

PLE-332 done — squash-merged into local `next` (commit `be77685`). PLE-333 collapsed into PLE-332.

PLE-334 + PLE-335 done — squash-merged into local `next` (commit `2356b62`). Bumped every Python pin (Dockerfiles, GHA, `transform/src/setup.py`) to 3.13; deleted `.circleci/` and swapped README CircleCI badge for GH Actions. PLE-335 collapsed into PLE-334 because PLE-334's `grep 'python.*3\.7'` AC could not be satisfied while CircleCI config remained.

PLE-331 + PLE-352 (research spikes) done — both squash-merged into `next` from worktree branches (commits `3510063`, `3d216a3`). PLE-331 picks Citus columnar single-node on PG 16+ to replace cstore_fdw (ADR `docs/adr/0001-columnar-pg.md`). PLE-352 keeps Retrosheet on `droher/retrosheet-mirror` (parser depends on alldata.zip layout + NLB-dedup patches) and switches Baseball Databank to `cdalzell/Lahman` because `chadwickbureau/baseballdatabank` is gone (ADR `docs/adr/0002-data-sources.md`).

PLE-336 + PLE-377 done — combined squash-merge into `next` (commit `6e9a956`, single PR per PLE-377 sequencing note). Replaced `sqlalchemy_fdw` with inline CREATE FOREIGN TABLE DDL in `postgres_cstore_fdw.py`; bumped SA → 2.x (incl. `declarative_base` import path), pyarrow ParquetWriter `version="2.0"` → `"2.6"`, all per-stage `requirements.txt`. Migrated host deps + ruff/pytest config into `pyproject.toml`; deleted `.flake8` and host `requirements.txt`; committed `uv.lock`. Added `basedpyright` dev dep + advisory CI job (40 errors / 2709 warnings baseline; strict-mode bring-up is follow-up scope). CI rewired to `astral-sh/setup-uv@v3` + `uv sync` + `uv run`; pinned `python-version: "3.13"` on every uv setup. README gained `## Development` section. `make ci-int-test` and `make ci-style` green locally via `act`. Test fixes: `tests/test_transform.py` swapped hardcoded table-count asserts for invariant checks (per global rule); added minimal `extract/fixtures/extract/retrosheet/bio.csv.zst` for the new `bio` schema; marked 3 `tests/test_extract.py` retrosheet parser tests `xfail(strict=True)` because the 2020-vintage fixture layout (`gamelog/`, `event/{asg,post,regular}`) predates the parser rewrite (`gamelogs/`, `allstar/`, `postseason/`, `events/`). Pre-existing red on master, unrelated to deps modernization — flagged for follow-up fixture regen ticket.

**Known breakage still carried over:**

- `mysql` apt-repo signing key (`B7B3B788A8D3785C`) expiry on `mysql:8.0.35-debian`. Carryover from PLE-336; bolted onto **PLE-344** DoD. **Resolved in PLE-344**: swapped to Oracle Linux variant `mysql:8.0.40` + microdnf, see Wave 4 entry below.

PLE-337 + PLE-338 (umbrella; absorbs children PLE-339/340/341/342) + PLE-351 done — single composite squash-merge into local `next` (commit `2fdea3f`) from `feature/ple-337-338-351-wave3-cleanup`. **Drill** target dropped (stage from `load/Dockerfile`, anchor + services from compose, README section). **`postgres-cstore-fdw` replaced by `postgres-columnar`**: new `PostgresColumnarDdlFactory` (subclasses `PostgresDdlFactory`, emits `CREATE EXTENSION IF NOT EXISTS citus;` + native `CREATE TABLE ... USING columnar`, preserves schemas — no more `<schema>_<table>` flattening); new `load/postgres-columnar/` (DW-tuning conf SQL); load/Dockerfile stage swaps PG 13 + cstore_fdw build-from-source for `postgres:16.1-bookworm` + apt `postgresql-16-citus-13.0` from packagecloud + `shared_preload_libraries='citus'` written to `postgresql.conf.sample` so initdb picks it up; compose anchor + services renamed; README rewritten with append-only caveat and ADR 0001 cross-link; `transform/src/ddl_factories/postgres_cstore_fdw.py` and `load/postgres_cstore_fdw/` deleted; `tests/test_transform.py::TestDdlFactory::test_columnar_ddl_uses_citus_columnar` asserts `CREATE EXTENSION ... citus` once per metadata + one `USING columnar` per table (45 tables). Standalone Citus 13.0 install + runtime smoke verified (`Custom Scan (ColumnarScan)` in EXPLAIN). Full `docker compose build postgres-columnar` end-to-end blocked only by the retrosheet fixture-regen carryover above. **PLE-351**: `BOXBALL_*_PATH` env-var override with `__file__`-anchored absolute defaults across `transform/src/__init__.py` + `extract/parsers/{util,retrosheet,baseballdatabank}.py`; Dockerfiles set the env vars for in-container builds; `tests/conftest.py` sets them at module-import time (before path-resolving imports run) so `os.chdir("/tmp/boxball")` is gone and tests are CWD-independent. `make ci-style` and `make ci-int-test` green locally; `pytest --cov` 8 passed / 3 xfailed (same 3 retrosheet-fixture xfails as before).

PLE-378 done — squash-merged into local `next` (commit `62db38a`). Carryover (a) from PLE-378 fixed in commit `125f243`: added `.strip()` to `parsers/retrosheet.py:75` so `remove_redundant_box_score_files` actually removes overlapping box-score accounts; new unit test `tests/test_extract.py::TestRetrosheet::test_remove_redundant_box_score_strips_game_id` covers the path with CRLF input under a patched `RETROSHEET_PATH`. `pytest --cov` now 12 passed. Rebuilt `extract/fixtures/raw/retrosheet.zip` against the canonical `https://retrosheet.org/downloads/alldata.zip` (per ADR 0002 revision; **not** `droher/retrosheet-mirror` as the original PLE-378 plan assumed) covering 1928 (deduced events + box-score overlap) and 2018 (per-team `.EV*`, all-star, postseason). Dropped the 3 `xfail(strict=True)` markers + `_FIXTURE_STALE` from `tests/test_extract.py`; replaced `assert True` with invariant assertions on `OUTPUT_PATH` outputs and on `event_game_ids().isdisjoint(deduced_game_ids())`; fixed `test_compress`'s hardcoded `gamelog/GL1871.TXT` path to the new `gamelogs/gl2018.txt`. New `extract/fixtures/build_fixtures.py` (stdlib-only) regenerates the fixture; new `extract/fixtures/README.md` documents layout, regen procedure, and sha256s. `pytest --cov` now 11 passed / 0 xfailed (vs. baseline 8 passed / 3 xfailed). `BUILD_ENV=test docker compose build extract` green end-to-end (cwdaily/cwgame/cwevent/cwsub/cwcomment all run; `parsed/event.csv` ~20 MB, `daily.csv` ~4.2 MB). Baseballdatabank fixture left alone — parser tolerates the missing `contrib/` dir via `pathlib.Path.glob` no-op behavior, and PLE-353 will rebuild that fixture against `cdalzell/Lahman` per ADR 0002. **Carryovers / follow-ups uncovered during PLE-378:** (a) `parsers/retrosheet.py:75` `game_id = line.split(",")[1]` is missing a `.strip()`; the `pbp_ids` set is built with stripped ids (`_pbp_game_ids` line 38 strips), so `remove_redundant_box_score_files` never finds a match and removes 0 accounts even when overlap exists (verified via `make ci-e2e-test`: "Removing 0 accounts from /retrosheet/boxes/1928.EBA" despite the builder's overlap check showing 95-game overlap). One-line fix; file separately. (b) Full `make ci-e2e-test` still red downstream of extract, but for an unrelated reason: it pulls `doublewick/boxball:ddl-2024.0.0` from Docker Hub instead of building locally, and that published tag predates PLE-338's `postgres_cstore_fdw.sql` → `postgres_columnar.sql` rename. Fixes itself at release-time cutover when fresh tags get published; until then `make ci-int-test` is the relevant local CI signal.

PLE-347 (umbrella; absorbs children PLE-348/349/350) done — single composite squash-merge into local `next` (commit `51c9905`) from `feature/ple-347-350-logging`. **Shared logging module**: `extract/parsers/_logging.py` and `transform/src/_logging.py` (duplicated because each Docker build context only sees its own subtree; `boxball_schemas` must stay import-clean per CLAUDE.md so it can't host the helper either). Both expose `get_logger(name) -> logging.Logger`, configure once at first call, read `BOXBALL_LOG_LEVEL` (default `INFO`, invalid value falls back to INFO) and `BOXBALL_STAGE` (rendered as `[<stage>]` between level and logger name; `%` in the stage value is escaped so a typo can't break `logging.Formatter`'s substitution). `tests/test_logging.py` covers default level, env override, invalid level, stage rendering, and a sync-invariant test that asserts the two `_logging.py` files are byte-identical below their docstrings. **Wire-up**: every `print(...)` removed from `extract/parsers/{retrosheet,baseballdatabank,util}.py` and `transform/src/{parquet,ddl_maker}.py`; failed parses log via `logger.exception(...)` with the file path; `parquet.py` also gained `try/finally` around `ParquetWriter.close()` (carryover correctness fix riding alongside the print swap). **Dockerfiles**: `extract/Dockerfile`, `transform/parquet.Dockerfile`, `transform/ddl.Dockerfile` declare `ARG BOXBALL_LOG_LEVEL=INFO` and bake it + `BOXBALL_STAGE=<stage>` into the image; `docker-compose.yml` lists `BOXBALL_LOG_LEVEL` in the args list for `extract`/`parquet`/`ddl` so `BOXBALL_LOG_LEVEL=DEBUG docker compose build extract` raises verbosity end-to-end (verified — DEBUG-level lines from `baseballdatabank.py` show up only when overridden). `csv.Dockerfile` left untouched — it runs no Python and the AC-literal `ENV` line had no consumer. README "Build-time logging" subsection + CLAUDE.md "Build / run" one-liner document the override. `pytest --cov`: 21 passed (was 11). `make ci-style` + `make ci-int-test` green via `act`. `BUILD_ENV=test docker compose build extract` end-to-end green with formatted output (`<asctime> [INFO] [extract] parsers.util: ...`).

PLE-343 (parent; absorbs children PLE-344/345/346) done — single composite squash-merge into local `next` (commit `a5f3015`) from `feature/ple-344-multiarch-bases`. **Multi-arch readiness for every target except `postgres-columnar`**:

- **PLE-344**: every Dockerfile base verified multi-arch via `docker manifest inspect`. Bumped `mysql:8.0.35-debian` → `mysql:8.0.40` (Oracle Linux 9 default flavor, multi-arch on Docker Hub) in `load/Dockerfile`'s mysql stage and *removed* the `RUN apt-get install zstd zip` line entirely — `zstd` ships in the OL9 base (verified on the live arm64 image) and `zip`/`unzip` were unused. Resolves the PLE-336 carryover (Oracle stopped publishing arm64 .debs for the `-debian` flavor and the `-debian` image's apt signing key `B7B3B788A8D3785C` expired). Bumped `parquet.Dockerfile` final stage `alpine:3.9.3` → `alpine:3.19.0` (consistency + arm64 wheel support) and build-common base `python:3.13-slim-bullseye` → `python:3.13-slim-bookworm`. Added `platforms: ["linux/amd64", "linux/arm64"]` to every compose anchor (extract/ddl/parquet/csv/clickhouse/postgres/mysql/sqlite). Dropped obsolete `version: '3.7'` from compose. **postgres-columnar pinned to amd64-only** with documented reason: Citus packagecloud's install script aborts on non-x86_64 with "the Citus repository does not contain packages for non-x86_64 architectures" (verified empirically by running the script in `postgres:16.1-bookworm` under `--platform linux/arm64`). README's "Development" section gained a "Multi-arch builds" subsection; the "Postgres columnar (Recommended)" block now also flags the amd64-only constraint to arm64 host users. Added `make buildx-bootstrap` (creates docker-container builder `boxball`; does *not* `--use` it since compose v2 ignores `docker buildx use`) and `make compose-build SVC=...` wrapper that exports `BUILDX_BUILDER=boxball` for the invocation. Empirically verified: `BUILDX_BUILDER=boxball BUILD_ENV=test docker compose build extract` produces a manifest list with both arches.
- **PLE-345**: `.github/workflows/ci.yml` e2e-test job gained `docker/setup-qemu-action@v3` (binfmt_misc handlers for cross-arch emulation on amd64 GH runners) before the existing `setup-buildx-action@v3` step. The buildx step is now id'd (`id: buildx`) and the build step explicitly exports `BUILDX_BUILDER: ${{ steps.buildx.outputs.name }}` rather than relying on the action's `use: true` default — that selection path is on a deprecation arc per the action's own `install:` deprecation message, and explicit env-var selection matches the local `make compose-build` recipe. (Real multi-arch validation requires `--push` to a registry — `docker compose build` cannot `--load` multi-platform output. Full registry push lands with PLE-358's release workflow.)
- **PLE-346**: read every `load/<target>/` init script (`clickhouse/z_load.sh`, `mysql/{A_unzip_csvs.sh,z_remove_csvs.sh,my.cnf}`, `postgres/{A_build_conf.sql,z_run_conf.sql}`, `postgres-columnar/{A_build_conf.sql,z_run_conf.sql}`) and the inline `RUN` blocks in `load/Dockerfile`'s `sqlite-build` stage (zstd loop + `sqlite3 -bail -echo` ingest). All arch-portable: pure bash + SQL `ALTER SYSTEM SET` statements, no compiled binaries shipped from the repo. The only binary tools they invoke (`zstd`, `clickhouse-client`, `sqlite3`) come from the base images, all of which are multi-arch.

`make ci-style` (ruff) and `make ci-int-test` (pytest) green locally; `pytest --cov` 21 passed.

**Carryover blocking full e2e validation locally**: `docker compose build postgres-columnar` (and the full chain) still pulls `doublewick/boxball:ddl-2024.0.0` from Docker Hub for the `--from=ddl` stage. The published image predates PLE-338's `postgres_cstore_fdw.sql` → `postgres_columnar.sql` rename, so the COPY fails with `"/ddl/postgres_columnar.sql": not found`. Same root cause as the PLE-378 follow-up (b). Self-resolves at release-time cutover when fresh tags publish; until then, multi-arch verification is via `manifest inspect` on bases + isolated single-service builds.

Local-e2e unblock done — squash-merged into `next` (commit `30ebdcf`) from `feature/ple-e2e-unblock-local-chain`. Diagnosed three layered race conditions in the PLE-343 multi-arch wiring that together produced the "stale `ddl-2024.0.0` from Docker Hub" carryover above:

1. **Multi-arch via buildx can't `--load`**: PLE-345 wired CI's e2e-test job through `BUILDX_BUILDER=<docker-container>` to satisfy compose's `platforms: [amd64, arm64]` declaration. But buildx cannot `--load` a multi-platform manifest list back into the local docker image store (only single-platform builds get `--load`). Each downstream `FROM doublewick/boxball:<stage>-${VERSION}` therefore missed the local store and pulled from the registry — getting the previous release's tag.
2. **Compose v2 builds services in parallel**: even with single-platform default-driver builds, `docker compose build` (no args) builds services concurrently. Downstream `FROM <tag>` lookups on `clickhouse`/`postgres-columnar`/etc. can race ahead of the upstream `ddl`/`csv`/`parquet` tag landing in the local store, again falling back to the registry.
3. **Platform mismatch on arm64 hosts**: `postgres-columnar` is pinned amd64-only (Citus has no arm64 packages). On an arm64 host (Apple Silicon dev), default-driver builds of `extract`/`ddl`/`csv` produce arm64 images. `postgres-columnar`'s amd64 build of `--from=ddl` then can't find an amd64 `ddl-${VERSION}` in the local store and falls back to the registry — even with serialization.

Fixes: dropped `platforms:` from every `docker-compose.yml` anchor (compose stays single-platform). Multi-arch intent moved to a new `docker-bake.hcl` that imports the compose targets and overrides `platforms` per-target (most amd64+arm64; `postgres-columnar` amd64-only). New `make build-local` Make target serializes the build into three waves (`extract` → `ddl parquet csv` → `clickhouse postgres postgres-columnar mysql sqlite`) and exports `DOCKER_DEFAULT_PLATFORM=linux/amd64` so the entire chain coheres at one platform that matches CI (ubuntu-latest) and the published `postgres-columnar` artifact. arm64 hosts emulate via QEMU (slow but coherent); for native-arm64 dev images, build a single non-columnar target host-arch (`docker compose build postgres`). New `make bake-print` (validates bake graph) and `make bake-push` (release path; needs DH login + the `boxball` docker-container builder from `make buildx-bootstrap`). Dropped the obsolete `make compose-build` wrapper. CI's e2e-test job swapped `docker/setup-qemu-action@v3` + `docker/setup-buildx-action@v3` + `BUILDX_BUILDER` env-var for plain `make build-local` — single-platform amd64 matches the GH amd64 runner natively, no QEMU/buildx dance needed. README "Multi-arch builds" section split into "Local builds" (`make build-local`) + "Multi-arch (release)" (`make bake-push`); CLAUDE.md "Build / run" block points at `make build-local` for full-chain. Empirically verified: `BUILD_ENV=test make build-local` green end-to-end on arm64 Apple Silicon (~30 min via Rosetta/QEMU), all 9 image tags written (`extract`/`ddl`/`csv`/`parquet`/`clickhouse`/`postgres`/`postgres-columnar`/`mysql`/`sqlite`-`2024.0.0`); `postgres-columnar`'s `COPY --from=ddl /ddl/postgres_columnar.sql` resolves against the just-built local `ddl-2024.0.0` (no registry pull).

Active: none. Next up: Wave 5 data refresh (**PLE-353/354/355**) per PLAN.md, or Wave 6 shipping infra (**PLE-357/358/359**) — `make bake-push` is one `docker login` away from being a full release pipeline.
