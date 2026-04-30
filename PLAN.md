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

- `BUILD_ENV=test docker compose build` red at the `extract` stage — the `retrosheet.zip` fixture has the pre-2020 layout (`gamelog/`, `event/{asg,post,regular}`) but the parser was rewritten to expect `gamelogs/`, `allstar/`, `postseason/`, `events/`. Same root cause as the xfail-strict `tests/test_extract.py` parser tests. Needs fixture-regen ticket — **not yet filed**, blocks final e2e smoke for the entire pipeline.
- `mysql` apt-repo signing key (`B7B3B788A8D3785C`) expiry on `mysql:8.0.35-debian`. Carryover from PLE-336; bolted onto **PLE-344** DoD.

PLE-337 + PLE-338 (umbrella; absorbs children PLE-339/340/341/342) + PLE-351 done — single composite squash-merge into local `next` (commit `2fdea3f`) from `feature/ple-337-338-351-wave3-cleanup`. **Drill** target dropped (stage from `load/Dockerfile`, anchor + services from compose, README section). **`postgres-cstore-fdw` replaced by `postgres-columnar`**: new `PostgresColumnarDdlFactory` (subclasses `PostgresDdlFactory`, emits `CREATE EXTENSION IF NOT EXISTS citus;` + native `CREATE TABLE ... USING columnar`, preserves schemas — no more `<schema>_<table>` flattening); new `load/postgres-columnar/` (DW-tuning conf SQL); load/Dockerfile stage swaps PG 13 + cstore_fdw build-from-source for `postgres:16.1-bookworm` + apt `postgresql-16-citus-13.0` from packagecloud + `shared_preload_libraries='citus'` written to `postgresql.conf.sample` so initdb picks it up; compose anchor + services renamed; README rewritten with append-only caveat and ADR 0001 cross-link; `transform/src/ddl_factories/postgres_cstore_fdw.py` and `load/postgres_cstore_fdw/` deleted; `tests/test_transform.py::TestDdlFactory::test_columnar_ddl_uses_citus_columnar` asserts `CREATE EXTENSION ... citus` once per metadata + one `USING columnar` per table (45 tables). Standalone Citus 13.0 install + runtime smoke verified (`Custom Scan (ColumnarScan)` in EXPLAIN). Full `docker compose build postgres-columnar` end-to-end blocked only by the retrosheet fixture-regen carryover above. **PLE-351**: `BOXBALL_*_PATH` env-var override with `__file__`-anchored absolute defaults across `transform/src/__init__.py` + `extract/parsers/{util,retrosheet,baseballdatabank}.py`; Dockerfiles set the env vars for in-container builds; `tests/conftest.py` sets them at module-import time (before path-resolving imports run) so `os.chdir("/tmp/boxball")` is gone and tests are CWD-independent. `make ci-style` and `make ci-int-test` green locally; `pytest --cov` 8 passed / 3 xfailed (same 3 retrosheet-fixture xfails as before).

Active: none. Next up: Wave 2 logging chain (**PLE-347→350**), then Wave 4 multi-arch (**PLE-343/344/345/346**, including the mysql apt-key fix on PLE-344). File the retrosheet fixture-regen ticket before Wave 5 (data refresh) starts — it blocks any meaningful e2e validation.
