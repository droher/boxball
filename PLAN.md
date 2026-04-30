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

Active: Wave 6 shipping infra wrapping up — only PLE-356 (first real release / cutover) remains, which is a manual user-driven step. Wave 5 done.

PLE-358 + PLE-359 + PLE-360 + PLE-361 done — single composite squash-merge into local `next` (commit `f9d05f6`) from `feature/ple-358-release-workflow`. **`.github/workflows/release.yml`** triggers on `v*.*.*` tag push and on `workflow_dispatch` with `version` + `dry_run` inputs. Pipeline:

1. **resolve** — derive VERSION from tag or input; assert it matches `.env` VERSION and that `CHANGELOG.md` has a `## [VERSION]` section. Refuses to proceed otherwise.
2. **build-push** (PLE-359) — `setup-qemu` + `setup-buildx` (docker-container driver) + DH login. Runs `docker buildx bake` against `docker-compose.yml` + `docker-bake.hcl` in three waves matching the build DAG (extract → ddl/parquet/csv → load stages). Each wave's pushed manifest list is the registry source for the next wave's `FROM doublewick/boxball:<stage>-${VERSION}` references — buildx cannot `--load` a manifest list, so registry serialization is the only path for first-release. Final step retags `<stage>-${VERSION}` → `<stage>-latest` for all 9 stages via `docker buildx imagetools create` (cheap, byte-identical, preserves manifest-list shape). `dry_run=true` swaps every `--push` for `--print` and skips bundles + release.
3. **bundles** (PLE-360) — pulls the just-pushed `parquet-${VERSION}` + `csv-${VERSION}` images (amd64 variant; flat files are arch-independent), `docker create` + `docker cp` extracts the output trees, tar+zstd-19 bundles them as `boxball-parquet-${VERSION}.tar.zst` / `boxball-csv-${VERSION}.tar.zst`, uploads as `actions/upload-artifact@v4`.
4. **release** (PLE-361) — downloads the bundles, extracts the matching `## [VERSION]` section from `CHANGELOG.md` via awk, validates the tag actually exists on origin (`gh api repos/.../git/refs/tags/$TAG`), then `gh release create --notes-file release-notes.md` with the bundles as assets. `workflow_dispatch` does NOT auto-create the tag — user must push the tag explicitly first; the workflow fails fast with a clear message if the tag is missing.

**`CHANGELOG.md`** new at repo root: Keep-a-Changelog format, calendar versioning (`YYYY.MINOR.PATCH`). `[2026.0.0]` retroactive entry covers the full Wave 0–5 refresh (postgres-columnar replacement, multi-arch readiness, structured logging, `make ci`/`make build-local`, `auth-smoke.yml` + `release.yml`, Retrosheet/Lahman v2025 source repoint, Python 3.13, uv/ruff/basedpyright stack, SA 2.x, MySQL base bump, fixture rebuild). Workflow's `resolve` job parses this file as the gate for releaseability.

**Security**: every `${{ ... }}` interpolation of `inputs.*`, `github.*`, or job outputs runs through `env:` blocks — no untrusted input reaches `run:` script bodies. `actionlint` clean.

**`docker-bake.hcl`** TODO referencing PLE-358 dropped (replaced by a comment pointing at `release.yml`'s retag step). `Makefile`'s `buildx-bootstrap` echo line updated to drop the PLE-357/358 reference.

**Live verification deferred to master cutover.** `workflow_dispatch` requires the workflow file to live on the default branch, and refresh phase keeps `master` untouched until the single batched cutover (PLE-356). Pre-flight checks completed locally: `docker buildx bake --print` resolves all 9 targets at `2026.0.0` with the expected platforms (8× amd64+arm64; postgres-columnar amd64-only); CHANGELOG awk extraction round-trips cleanly; `actionlint` passes both new workflows.

PLE-357 done — squash-merged into local `next` (commit `2aa6b5f`) from `feature/ple-357-creds`. Provisioned Docker Hub PAT (`boxball-ci`, Read+Write+Delete scoped to `doublewick/boxball`) and stored as `DOCKERHUB_USERNAME`+`DOCKERHUB_TOKEN` GH secrets via `gh secret set`. Configured PyPI trusted publishing for `boxball-schemas` with two pending publishers (`auth-smoke.yml` + `release.yml`); no long-lived PyPI token. Stale 2020 CircleCI-era secrets `DOCKER_HUB_USERNAME`/`DOCKER_HUB_PASSWORD` deleted. New `.github/workflows/auth-smoke.yml` (`workflow_dispatch`-only) validates DH login (`docker/login-action@v3`) and PyPI OIDC mint (raw curl to `pypi.org/_/oidc/mint-token`, token discarded — no publish). Maintainer creds doc lives outside the repo at `~/Documents/boxball-release-creds.md` per maintainer direction (no `RELEASING.md`/`CONTRIBUTING.md` addition). **Live verification deferred to master cutover**: `workflow_dispatch` requires the file on the default branch and refresh phase keeps `master` untouched until the batched flip; smoke run will fire pre-PLE-356 once `master` updates. Docker Hub OIDC trusted publishing not GA as of Apr 2026 (Docker blog "Building Trusted Content with GitHub Actions" lists it under "what's next"); PAT is canonical until that lands, at which point `auth-smoke.yml` and `release.yml` swap their DH login step for the OIDC equivalent.

PLE-353 + PLE-354 + PLE-355 done — single composite squash-merge into local `next` (commit `9ab6c6e`) from `feature/ple-353-355-data-refresh`. **Refreshes both upstream data sources to current vintage and bumps `VERSION` to `2026.0.0`.**

- **PLE-353 Retrosheet repoint** (per ADR 0002 R1): `.env` drops `RETROSHEET_VERSION` (git SHA on `droher/retrosheet-mirror`), adds `RETROSHEET_RELEASE_DATE=2025-12` (documentation) + `RETROSHEET_SHA256=88fbc6a2…` (integrity). `extract/Dockerfile` `get-retrosheet-prod` swaps GitHub archive wget for `wget --user-agent='Mozilla/5.0 (compatible; boxball-build)' https://retrosheet.org/downloads/alldata.zip` + `sha256sum -c` verification. Canonical `alldata.zip` extracts top-level dirs (gamelogs/, events/, biodata/, …) directly with no wrapper directory; `parsers/retrosheet.py` switched to recursive globs `**/biofile.csv` + `**/ballparks.csv` to find files now nested under `biodata/`.
- **PLE-353 Baseball Databank repoint** (per ADR 0002 R2 — _empirical correction to the original ADR_): `BASEBALLDATABANK_VERSION` repointed to `corbtastik/lahman-baseball-db@b5e7327707fff91ff3bdcbe1f6892c8c5015cf1d` (SABR Lahman v2025, Dec 10, 2025 release), **not** `cdalzell/Lahman` per the original ADR. Verified during PLE-353 that both `cdalzell/Lahman@master` and `cdalzell/Lahman@2025-update` ship a `source-data/baseballdatabank-master.zip` whose `core/Teams.csv`/`core/Batting.csv` cap at `yearID=2019` — strictly worse than the `tom-719/baseballdatabank` legacy pin (2022 ceiling). `corbtastik/lahman-baseball-db` ships flat CSVs at the repo root; `extract/Dockerfile` `get-baseballdatabank-prod` rehomes them under `/baseballdatabank/core/` to keep `BOXBALL_BASEBALLDATABANK_CORE_PATH` stable.
- **Dockerfile restructure**: moved unzip-and-rehome steps from `extract-retrosheet`/`extract-baseballdatabank` into the per-`BUILD_ENV` `get-*-{prod,test}` stages, so the alias stages each ship a ready-to-go directory tree at `/retrosheet/` or `/baseballdatabank/core/`. Both prod and test paths converge before the alias, keeping the downstream parser-running stages source-agnostic. `docker-compose.yml` `extract` anchor's `args:` list now passes `RETROSHEET_RELEASE_DATE` + `RETROSHEET_SHA256` (replacing `RETROSHEET_VERSION`).
- **PLE-354 VERSION bump**: `.env` `VERSION=2024.0.0 → 2026.0.0`. All 9 stage tags written to local image store at `2026.0.0` after `BUILD_ENV=test make build-local`.
- **PLE-355 fixture rebuild + Lahman v2025 schema reno** (per ADR 0002 R3): rewrote `extract/fixtures/build_fixtures.py` to source both fixtures from the new canonical upstreams (retrosheet.org `alldata.zip`; corbtastik archive at the pinned SHA) with byte-identical output across re-runs (pinned ZipInfo timestamps). Added `--target baseballdatabank` covering all 27 schema-mapped Lahman tables (`AllstarFull.csv` verbatim so the parser's `9;9` fixup is exercised; the other 26 truncated to header + first 50 rows; total ~70 KB). Retrosheet fixture inner layout now mirrors canonical `alldata.zip` (no `retrosheet-master/` wrapper); biofile + ballparks at canonical `biodata/` paths. `tests/conftest.py` retrosheet/databank unzips updated to land trees at `/tmp/boxball/retrosheet/` and `/tmp/boxball/baseballdatabank/core/` directly. **Schema changes** (compatibility-preserving — column NAMES + PK identity unchanged): `boxball_schemas/baseballdatabank.py::People` gained leading `id` column + reordered birth section to `birth_city, birth_country, birth_state` and tail to `bbref_id, final_game, retro_id` to track Lahman v2025's CSV column positions. `Parks` gained leading `id` column + reordered to `park_alias, park_id (PK), park_name, city, state, country`. `AllstarFull.starting_pos` kept `SmallInteger`; `parsers/baseballdatabank.py` gained a `ROW_FIXUPS` dict + `_strip_multi_position_starting_pos` that collapses Negro Leagues multi-position notation (`9;9` → `9`) to the first integer (~65 / 6425 rows; second-position datapoint dropped — follow-up ticket should add proper multi-position support). Verified end-to-end: `pytest --cov` 21 passed; `BUILD_ENV=test make build-local` green across all 9 stages including `postgres-columnar`'s Citus init at the new VERSION.

**Carryover / follow-ups:**

- (a) Negro Leagues all-star multi-position datapoint loss tracked by `parsers/baseballdatabank.py::_strip_multi_position_starting_pos`. Follow-up should add a sibling table or column that preserves the second position.
- (b) Retrosheet QA patches that the `droher/retrosheet-mirror` fork carried (NLB dedup, 6 historical-file corrections) are not currently re-applied Boxball-side. ADR 0002 Option D placeholder. Decide post-refresh whether any are load-bearing for downstream consumers.

PLE-356 prep done — squash-merged into local `next` (commit `43fb8b3`) from `feature/ple-lahman-widen-strings`. **Runtime e2e gating + bug fixes uncovered while building it.** First validation pass against the just-built `BUILD_ENV=test` `2026.0.0` images failed every load target; this commit makes all 5 pass and wires the harness into both CI and the release workflow so `latest` cannot be retagged onto a broken build.

- **Lahman v2025 schema width sweep** (carryover from PLE-355): wrote a positional `csv` ↔ SQLAlchemy-metadata audit (`humps.depascalize` of every column name; max-width comparator over the full upstream CSV tree at `corbtastik/lahman-baseball-db@b5e7327`) — the only mismatches are `parks.park_alias` 55 → 255 (Lahman v2025 stores semicolon-joined alias lists; Hard Rock Stadium's history hits 128 chars) and `parks.park_name` 40 → 80 (44-char ESPN Wide World of Sports value). Already on this branch from earlier validation iterations: `lg_id` 2 → 3 across 22 sites (Negro Leagues `WES`/etc.), `Parks.country` 2 → 20 (full country names), `HallOfFame.needed_note` 25 → 255. Retrosheet schema uses `String(>=256)` everywhere so was structurally exempt.
- **Parser CRLF bug** (`extract/parsers/baseballdatabank.py`): `csv.writer` defaults to `'\r\n'` per RFC 4180, so the row-fixup path (only `allstar_full` because of the `9;9` collapse) emitted CRLF while the passthrough path emitted LF (Python text-mode universal newlines `\r\n` → `\n` on read; `newline=''` on write preserves `\n` as-is). Postgres COPY tolerates CRLF transparently; MySQL `LINES TERMINATED BY '\n'` leaves a trailing `\r` in the last field, which the `IF(@col='', NULL, @col)` guard cannot match → "Incorrect integer value: '' for column 'starting_pos' at row 1" on the first AllstarFull row. Force `lineterminator='\n'`.
- **MySQL row-size bug** (`MySqlDdlFactory.metadata_transform`, new): `retrosheet.bio` `CREATE TABLE` failed at "Row size too large. The maximum row size for the used table type, not counting BLOBs, is 65535." 30+ `VARCHAR(1024)` columns × utf8mb4 4 bytes = 122 KiB, beyond InnoDB's hard cap. New `metadata_transform` rebuilds a fresh `MetaData` and promotes any `String(N >= 256)` non-PK column to `Text` (TEXT spills off-page and is exempt from the row-size check). Build a copy rather than mutating shared metadata so downstream factories (clickhouse, …) keep seeing the original SQLAlchemy types — direct mutation broke the clickhouse `type_lookup` with `KeyError: <class '…Text'>`.
- **sqlite missing dir** (`load/Dockerfile`): ENTRYPOINT decompresses `/tmp/boxball.db.zst -fo /db/boxball.db` but `/db` did not exist in the image. README's docker-run recipe mounts a host volume there, so this had been latent since the sqlite stage was authored. Added `RUN mkdir /db`.
- **`scripts/validate-targets.sh` (new)**: polling-based readiness probe (run a known `SELECT` in a loop, not `grep` of log lines — robust to upstream image log-format drift), then a `count(*)` query against `baseballdatabank.teams`, then teardown. One target per run; non-zero exit if any failed.
- **CI gate** (`.github/workflows/ci.yml::e2e-test`): runs the script after `make build-local`, so a PR cannot land a broken target.
- **Release gate** (`.github/workflows/release.yml`): added `validate-runtime` job between `build-push` and a newly-split `promote-latest` (and `bundles`/`release`) so the `<stage>-latest` retag only fires after the just-pushed `:VERSION` manifests pass the runtime e2e. `actionlint` clean.

End-to-end (BUILD_ENV=test, local store): all 5 targets PASS — 27 baseballdatabank tables and 50 teams rows in each.

PLE-356b retrosheet sweep done — squash-merged into local `next` (commit `2fc6f26`) from `feature/ple-356b-retro-sweep`. Same comprehensive width audit + runtime validation Lahman got in PLE-356 prep, applied to retrosheet against full prod data. Test-fixture validation in PLE-356 prep didn't exercise retrosheet at scale; this round caught chadwick column-count drift and 2024+ retrosheet schedule format changes that test fixtures (1928 + 2018 only) couldn't surface.

- **Chadwick bump** (`.env`): `CHADWICK_VERSION` 23 commits forward (`aff8d779` June 2023 → `c685ab51` Mar 2026). Three column-count changes flow through, all schema-compatible *if* parser flags + schema both move:
  - cwgame std 84 → 85: new `GAME_TYPE_TX` field at position 84 (between std and ext blocks). Bumped `cwgame -f 0-83` → `-f 0-84` in `extract/parsers/retrosheet.py::PARSE_FUNCS`. Schema `Game.game_type_tx String(16)` inserted between `home_finish_pit_id` (last std) and `away_team_league_id` (first ext) — *position matters*: chadwick emits std-then-ext ordering, so appending at end of the schema would shift every ext-field by one and break int16 conversions for the entire ext block.
  - cwevent ext 63 → 67: 4 new fields `COUNT_TX`, `RUN{1,2,3}_AUTO_FL` appended after `uncertain_play_exc_fl`. Bumped `cwevent -x 0-62` → `-x 0-66`. Schema `Event` gains `count_tx String(8)` + 3 `Boolean` flags at the end.
  - cwsub 10 → 25: pitch-detail block (`BALLS_CT`, `STRIKES_CT`, `PITCH_SEQ_TX`, plus 12 `PA_*_CT` mirrors of the event table). Parser uses default `cwsub` (no `-f` filter), so the new fields appear automatically post-bump. Schema `Sub` extended with the 15 new cols, `dummy_id` kept trailing.
- **2024+ schedule format drift** (`extract/parsers/retrosheet.py::concat_files`, schema): retrosheet schedule files added a 5-char park column at position 11 starting in 2024 (e.g. `SEO01` for the Seoul series); 4,739 of 233,832 rows in the prod corpus ship the new shape. Legacy 12-col rows are CSV-quoted (some with embedded commas) so the pad path uses `csv.reader`/`csv.writer` rather than naive `split(",")` and re-emits unquoted to give a uniform 13-col output. Schema `Schedule.park_id String(8)` inserted between `day_night` and `postponement_indicator`. Same rows widened `day_of_week` from `CHAR(3)` (`Sat`) to full-name (`Wednesday`, 9 chars) — schema bumped to `String(16)`.
- **Lahman college_playing year_id NOT NULL conflict** (incidental, surfaced during prod-data validation): Lahman v2025 ships ~310 college_playing rows with blank `year_id` (Negro Leagues era where year is unknown). Original schema had `(player_id, school_id, year_id)` composite PK — *no* row-level pre-validation in the prep audit caught this because that audit was width-only. (player, school) alone isn't unique either (5,461 multi-year players). Switched to dummy_id pattern; year_id becomes a regular nullable column. *Carryover for the next audit pass: extend the schema audit to verify NOT NULL columns are non-blank in the source CSVs.*
- **`scripts/validate-targets.sh` hardening** (uncovered when prep harness reported false-positive failures against prod data):
  - **Empty-table false-PASS**: `psql -tAc "SELECT 1 FROM baseballdatabank.teams LIMIT 1"` exits 0 even when teams is empty (it just returns nothing), so the polling loop declared "teams loaded" mid-init. Now pipes the result through `grep -q 1` to require an actual row. Same fix on the mysql + clickhouse probes.
  - **Timeouts**: prod-data load takes 10-15 min per target (vs ~30s on test fixtures); bumped postgres/clickhouse 360s → 600s and mysql 480s → 900s.
  - **SQLite mid-decompress malformed-image**: ENTRYPOINT does `zstd --rm -d /tmp/boxball.db.zst -fo /db/boxball.db && sqlite_web …`; the prep readiness check `test -s /db/boxball.db` fires while the 8.7 GB write is still in progress and the validate query then fails with "database disk image is malformed (11)" against a half-written file. `zstd --rm` deletes the source on a clean decompress, so absence of `/tmp/boxball.db.zst` is the right "DB whole" signal — switched to that.
- **sqlite-web 0.4.1 → 0.6.4** (`load/Dockerfile`): orthogonal to retrosheet but caught in the same validation pass. 0.4.1 imports `escape` from `flask`, removed in Flask 3.x; sqlite stage container exited with `ImportError` immediately after decompress on the Python 3.13 / Flask 3.x base. Bumped to a flask-3-compatible release. (The decompress-then-crash sequence still left a complete DB on disk, which is what masked this for so long: `docker run -d` returns immediately, the validate `docker exec` against the dying container caught the malformed mid-decompress signal *before* the container fully exited, so the symptom looked like a sqlite issue rather than a flask one.)

End-to-end against full prod data (Lahman v2025 + retrosheet 2025-12 = ~16M event rows, ~5.4M daily rows): all 5 targets PASS — 27 baseballdatabank tables and 3,614 teams rows in each.
