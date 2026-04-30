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

PLE-334 + PLE-335 done — squash-merged into local `next` (commit `2356b62`). Bumped every Python pin (Dockerfiles, GHA, `transform/src/setup.py`) to 3.13; deleted `.circleci/` and swapped README CircleCI badge for GH Actions. PLE-335 collapsed into PLE-334 because PLE-334's `grep 'python.*3\.7'` AC could not be satisfied while CircleCI config remained. `requirements.txt`: `pyarrow==14.0.1` → `pyarrow>=18` (no 3.13 wheel for 14.x); rest left for PLE-336.

**Known breakage carried over** (both reproduce identically on `master` — not caused by 3.13 bump):

1. `make ci-int-test` red — `sqlalchemy_fdw==0.3.0` calls removed SQLAlchemy internal `sqlalchemy.util.dependencies._importlater`; fails at module import in `transform/src/ddl_factories/postgres_cstore_fdw.py`. Promoted to hard DoD bullet on **PLE-336**.
2. `BUILD_ENV=test docker compose build` red at `mysql` target — `mysql:8.0.35-debian` apt repo signing key (`B7B3B788A8D3785C`) expired upstream. Promoted to hard DoD bullet on **PLE-344** (multi-arch / Dockerfile bases) since the multi-arch AC's verification can't pass until mysql base is bumped or GPG re-pinned.

PLE-332 shipped without verifying either. PLE-334's local rehearsal exposed both for the first time.

Active: none. Next up: PLE-336 (must restore `make ci-int-test` to green as part of DoD).
