# ADR 0001: Columnar Postgres Replacement for `cstore_fdw`

- **Status:** Accepted — implemented on `feature/ple-337-338-351-wave3-cleanup`
- **Date:** 2026-04-30
- **Linear ticket:** PLE-331 (spike); implementers: PLE-338 / PLE-339 / PLE-340 / PLE-341 / PLE-342
- **Authors:** Boxball 2026 Refresh

## Context

Boxball ships a `postgres-cstore-fdw` Docker target as the README-recommended on-ramp for users who want Postgres semantics with columnar storage on the wide Retrosheet `event` table (Lahman-style queries against ~14M play-by-play rows). The current implementation:

- Pins to `postgres:13.13-bookworm` because [`cstore_fdw`](https://github.com/citusdata/cstore_fdw) was last released in February 2020 with PostgreSQL 12 as its newest supported major. PG 13+ is unsupported (the build sometimes succeeds against the master branch but is uncertified).
- Builds the extension from source in `load/Dockerfile` via `wget` of the GitHub master archive, `apt`-installs `postgresql-server-dev-13` + protobuf-c toolchain, and `make install`s into the image.
- Uses `sqlalchemy_fdw.dialect.PGDialectFdw` and `ForeignTable` to emit `cstore_fdw`-flavored DDL (`SERVER cstore_server`, `pglz` compression, no schemas — table names are `<schema>_<table>` because foreign tables don't honor schemas the same way).
- Strips `dummy_id` autoincrement PKs in `metadata_transform`.
- Uses Postgres `COPY FROM PROGRAM 'zstd -dc ...'` loaders inherited from `PostgresDdlFactory`.

Constraints driving this ADR:

1. The `cstore_fdw` upstream is in **maintenance mode** by its own README (`citusdata/cstore_fdw`), explicitly redirecting users to the modern columnar implementation in Citus. It is unpackaged for PG 13+ and pins us to an EOL-bound major.
2. The 2026 refresh requires PG 16+ for parity with the plain `postgres` target (PLE-336/PLE-377 deps modernization).
3. PLE-343 is going multi-arch (`linux/amd64` + `linux/arm64`). Whatever we land here must either ship multi-arch images or build cleanly multi-arch from source.
4. Existing users running queries against the cstore target should see no SQL surface change beyond the storage clause — Postgres dialect, same column types, same NULL handling.
5. Bulk-load semantics matter: the load stage does a one-shot `COPY` and the DB never sees `UPDATE`/`DELETE` against the columnar `event` table at runtime. Append-only is fine.

Two real candidates emerged and were evaluated:

### Option A — Hydra Columnar (`hydradatabase/columnar`)

Originally a fork of `cstore_fdw`, rewritten on the Postgres 12 Table Access Method (TAM) API. Distributed as the `ghcr.io/hydradatabase/hydra` Docker image (a drop-in `postgres` replacement bundling several extensions) and as the standalone `columnar` extension source.

| Criterion | Finding |
|---|---|
| **PG versions** | v1.1.x supports **PG 13–16**. PG 17 support is an open feature request ([issue #272](https://github.com/hydradatabase/columnar/issues/272), opened Nov 2024, no progress as of last check). PG 18 not on the roadmap. |
| **Latest release** | **v1.1.2 — April 1, 2024.** No tagged release in 2025 or 2026. |
| **Commit cadence** | Most recent commit on `main` is Feb 10, 2025 (README update). Prior code commits Oct 7, 2024. **Effectively dormant** — 13+ months since last code-bearing commit at time of writing. |
| **Install path** | `ghcr.io/hydradatabase/hydra:latest` is a full Postgres-replacement image bundling several extensions (`pgsql-http`, etc.), built FROM a custom `postgres_base` (not the official `postgres` image). Standalone extension is a `make && make install` against `postgresql-server-dev-N`, similar shape to current cstore_fdw build. |
| **Multi-arch** | Hydra `ghcr.io` tags publish manifests for `linux/amd64` AND `linux/arm64` (per package page metadata), but the most recent published tags are >1 year old and pinned to PG 13/15/16 SHAs. From-source build would compile for whatever arch the base image is — viable. |
| **Image size** | Not advertised. Bundles extra extensions we don't need (analytics tooling, http, etc.). |
| **License** | Columnar code AGPL-3.0; surrounding tooling Apache-2.0. AGPL extension code linked into a Postgres distribution we redistribute is the relevant question — Boxball already redistributes AGPL Postgres extensions (Citus's columnar is also AGPL), so no new exposure. |
| **DDL/DML** | TAM-based. Supports bulk INSERT, UPDATE, DELETE (with caveats — "not meant for frequent large updates, small transactions"). Btree+hash indexes only. No logical replication. **For our append-only use case, all DML we exercise is supported.** |
| **Migration parity with cstore_fdw** | Higher than Citus on the syntax axis: Hydra defaults to creating columnar tables transparently (heap → columnar conversion is the path). But our DDL factory currently emits `cstore_fdw`-specific FDW + SERVER + foreign-table syntax — that goes away regardless of choice. |

### Option B — Citus columnar (single-node mode, `citusdata/citus`)

Citus is the modern, first-party successor — its README of `cstore_fdw` literally points users at Citus columnar. Columnar storage is implemented as a TAM inside the Citus extension and works on a single node without any sharding/distribution being enabled.

| Criterion | Finding |
|---|---|
| **PG versions** | **Citus 13.x supports PG 17.x** (Citus 13.0.1 brought PG 17.2 support, Feb 2025). **Citus 14.0 (Feb 17, 2026) supports PG 18.1.** Older 12.1.x line covers PG 14–16. |
| **Latest release** | **Citus 14.0 — February 17, 2026.** Active 2025 and 2026 releases. |
| **Commit cadence** | Active. ~7,275 commits on `main`, 134 releases, releases on 2024/2025/2026 cadence. First-party Microsoft-owned. |
| **Install path** | Multiple, all easier than current cstore build: <br>(a) `citusdata/citus` Docker image (full PG + Citus, comes in `alpine` and Debian variants); <br>(b) `apt`/`yum` packages from packagecloud.io (`postgresql-NN-citus-13.X`); <br>(c) Build from source (`PG_CONFIG=... make && make install`). For Boxball, **(b) layered onto the official `postgres:16-bookworm` image** mirrors how we already build cstore_fdw and matches the per-stage pattern in `load/Dockerfile`. |
| **Multi-arch** | **The biggest risk.** Citus issues [#3854](https://github.com/citusdata/citus/issues/3854) (2020) and [docker#309](https://github.com/citusdata/docker/issues/309) (2022) requesting ARM64 are both still **open**. The `citusdata/citus` Docker Hub tags do not advertise `linux/arm64` manifests. **However:** Citus is plain Postgres extension C code — building from source on `arm64` works (community confirms in those threads), and packagecloud has shipped arm64 `.deb`s for Citus on Debian for some recent releases. Our load stage already does extension builds; we'd inherit that path for arm64. |
| **Image size** | Layered onto `postgres:16-bookworm` the extension itself is a few MB. We don't pull the bundled `citusdata/citus` image — we apt-install the extension into the same `postgres:16-bookworm` base we already use for the plain `postgres` target. Net image-size delta vs. plain postgres: small. |
| **License** | Server is AGPL-3.0, same exposure profile as Hydra's columnar. |
| **DDL/DML** | TAM-based, native syntax: `CREATE TABLE ... USING columnar`. **Append-only — no UPDATE / DELETE / FK on columnar tables.** ON CONFLICT only with `DO NOTHING` and no target. No tuple locks, no SERIALIZABLE, btree+hash indexes only, no bitmap index scans. Supports `pglz`, `zstd` (default, level 1–19), `lz4`, `lz4hc`. **Has WAL, ROLLBACK, streaming replication, pg_dump, pg_upgrade** — the four big things `cstore_fdw` lacked. |
| **Migration parity with cstore_fdw** | Documented and intentional successor path. Drop the FDW/SERVER/foreign-table apparatus; emit ordinary `CREATE TABLE` with a `USING columnar` clause. Schemas work normally (no more `<schema>_<table>` flattening). Loader is plain `COPY` — same as the row-store `postgres` target. |

## Decision

**Adopt Citus columnar (single-node mode) as the replacement for `cstore_fdw`.**

Rename the Boxball target from `postgres-cstore-fdw` to **`postgres-columnar`** and pin to **PostgreSQL 16** (matching the plain `postgres` target) using the **Citus 13.x** extension line. Re-evaluate moving to PG 17 + Citus 13.x or PG 18 + Citus 14.x in a follow-up ticket once the rest of the refresh is shipped.

### Why Citus over Hydra

1. **Maintenance trajectory dominates.** Hydra Columnar's last release is April 2024 and the last code-bearing commit is October 2024 — over 13 months stale. PG 17 is an unanswered open issue. Citus had a major release ten weeks ago (Citus 14.0 in Feb 2026) and has shipped continuously through 2024–2026. Picking the dormant fork to escape the dead extension is not an upgrade.
2. **PG version reach.** Citus already supports PG 16 today and PG 17/18 are landed in current minor lines, giving us a clear forward path. Hydra would re-pin us to PG 16 with no clear PG 17 ETA, recreating the exact problem this refresh is unwinding for `cstore_fdw`.
3. **Native syntax beats FDW kludges.** Both options use TAM, so both let us drop the FDW/SERVER/foreign-table layer. But Citus's `USING columnar` is the documented industry-standard syntax for this use case and what users will recognize. The DDL factory becomes a thin subclass of `PostgresDdlFactory` that adds a `WITH (...)` storage clause — much smaller surface than `sqlalchemy_fdw`.
4. **Loss of `sqlalchemy_fdw` dependency.** `sqlalchemy-utils-fdw` (or whatever flavor we depend on) is itself a niche, sporadically-maintained package. Deleting it shrinks our dependency surface.
5. **First-party and durable.** Microsoft-owned; the Citus columnar code is the canonical successor named in `cstore_fdw`'s own deprecation notice.

### Accepted risks

- **ARM64 image story is unresolved upstream.** We will build the Citus extension from source against `postgres:16-bookworm` in our load stage rather than relying on `citusdata/citus` Docker images, which means our `linux/arm64` build is on us to verify (PLE-346). Mitigation: extension is plain C against PG headers, expected to compile clean on arm64; community confirms it works. If apt-from-packagecloud has arm64 `.deb`s for our PG 16 + Citus 13.x combo, prefer that; otherwise fall back to source build.
- **Append-only constraint.** Citus columnar refuses `UPDATE` and `DELETE`. Boxball's load is one-shot bulk insert and we never mutate at runtime, so this is non-binding for the build pipeline. **README must call this out** so downstream users don't try to mutate columnar tables — they'd hit a Citus error, not a Boxball one (PLE-342).
- **Benchmarking deferred to PLE-338.** This spike does not run head-to-head perf numbers — no Docker available in research env. PLE-338 (the implementation ticket) must do a `BUILD_ENV=test` smoke build and a query parity check (a handful of representative queries from README) against the new target. If Citus columnar perf regresses substantially vs. cstore_fdw on real (non-fixture) data, revisit.
- **AGPL is unchanged exposure.** We are not introducing AGPL into the project; cstore_fdw was already AGPL.

## Consequences

### For PLE-338 — Replace `postgres-cstore-fdw` with chosen columnar
- Rename the target end-to-end to `postgres-columnar`. Old image tags (`doublewick/boxball:postgres-cstore-fdw-*`) will be left untouched on Docker Hub for backward compatibility but no new ones cut.
- Coordinate the rename across `docker-compose.yml`, `load/`, `transform/src/ddl_factories/`, `README.md` (README cross-link is PLE-342), and any test references.
- Smoke-test `BUILD_ENV=test docker compose build postgres-columnar` and run a small query parity check (count + a couple of GROUP BYs against `event`) before declaring done.

### For PLE-339 — Add columnar target factory
- Create `transform/src/ddl_factories/postgres_columnar.py` subclassing `PostgresDdlFactory` (NOT `PostgresCstoreFdwDdlFactory`).
- `target_name = "postgres_columnar"`. Reuse the parent's `PGDialect`. **Drop the `PGDialectFdw` import.**
- `metadata_transform` only needs to strip `dummy_id` autoincrement PKs (same as cstore did) — schemas can be preserved (no more `<schema>_<table>` flattening). Keep the existing schema layout so users see `retrosheet.event` etc., matching the plain `postgres` target.
- Override `make_create_ddl` to:
  1. Emit `CREATE EXTENSION IF NOT EXISTS citus;` at the top.
  2. Add `USING columnar` to each `CREATE TABLE` statement. Easiest path: post-process the SQLAlchemy-generated DDL string with a regex (`CREATE TABLE ... \(...\)\s*;` → append `USING columnar;`) or, cleaner, use SQLAlchemy's `postgresql_using` table-level kwarg in `metadata_transform` if the dialect supports it for non-MATERIALIZED tables. Spike during implementation; either is fine.
  3. Optionally set columnar storage parameters via `ALTER TABLE ... SET (columnar.compression = 'zstd', columnar.compression_level = 9);` after creation. Default `zstd` is reasonable; revisit only if PLE-338 benchmarking shows a problem.
- Register in `transform/src/ddl_factories/__init__.py::all_factories`. Remove `PostgresCstoreFdwDdlFactory` registration.
- `make_copy_ddl` does NOT need overriding — inherited `PostgresDdlFactory.make_copy_ddl` (`COPY FROM PROGRAM 'zstd -dc ...'`) works against columnar tables identically. Bulk-load is the supported path.
- **Drop the `sqlalchemy-fdw` / `sqlalchemy_fdw` dependency** from `transform/`'s requirements (PLE-336 / PLE-377 territory if not yet purged).

### For PLE-340 — Load-stage Dockerfile + init scripts
- New stage `postgres-columnar` in `load/Dockerfile` and new dir `load/postgres-columnar/`.
- Base: `FROM postgres:16-bookworm` (matching the `postgres` target).
- Install Citus extension. **Preferred path:** apt from packagecloud:
  ```dockerfile
  RUN curl -sSf https://install.citusdata.com/community/deb.sh | bash && \
      apt-get install -y postgresql-16-citus-13.0 && \
      apt-get clean && rm -rf /var/lib/apt/lists/*
  ```
  If packagecloud arm64 coverage proves spotty during PLE-346, fall back to building from source against `postgresql-server-dev-16` + the `citus` source tarball pinned by tag.
- Add `shared_preload_libraries = 'citus'` to `postgresql.conf` (the `A_build_conf.sql` script can `ALTER SYSTEM SET shared_preload_libraries = 'citus';` — though that needs a restart, which complicates the entrypoint flow. Cleaner: write directly to `postgresql.conf` in the Dockerfile, same as the current cstore stage does for `cstore_fdw`).
- Copy `A_build_conf.sql` and `z_run_conf.sql` from current `load/postgres_cstore_fdw/` (they're generic Postgres DW tuning, still applicable). Create the new `load/postgres-columnar/` as a sibling dir; do NOT delete `load/postgres_cstore_fdw/` until PLE-341.
- Copy `/ddl/postgres_columnar.sql` from the `ddl` build stage and `/transform/csv` from the `csv` stage.

### For PLE-341 — Update compose, delete cstore_fdw entries
- In `docker-compose.yml`: replace `x-postgres-cstore-fdw` anchor + `postgres-cstore-fdw` / `postgres-cstore-fdw-latest` services with `x-postgres-columnar` + `postgres-columnar` / `postgres-columnar-latest`.
- Update `target:` from `postgres-cstore-fdw` to `postgres-columnar`, `image:` tag prefix accordingly.
- Volume path: `~/boxball/postgres-columnar:/var/lib/postgresql/data`.
- Drop the `platforms: ["linux/amd64"]` pin — PLE-343/344/345 will set this multi-arch globally.
- Delete `load/postgres_cstore_fdw/` directory and the `postgres-cstore-fdw-build` / `postgres-cstore-fdw` stages from `load/Dockerfile`.
- Delete `transform/src/ddl_factories/postgres_cstore_fdw.py` and remove its registration.
- Grep for residual references: `cstore`, `cstore_fdw`, `PGDialectFdw`, `sqlalchemy_fdw`, `postgres-cstore-fdw`, `postgres_cstore_fdw`. Expected hit sites: README, CLAUDE.md, this ADR (don't edit — historical), tests.

### For PLE-342 — README + ADR cross-link
- Link this ADR from the README's target-comparison section.
- Update `docker run` recipe: target name, port (5432 unchanged), volume path, image tag.
- **Add a "do not run UPDATE/DELETE on columnar tables" note** — Citus columnar is append-only by design. For users who need mutability, point them at the plain `postgres` target.
- Note that the columnar target now matches the plain `postgres` target's PG version (16) and schema layout — no more `<schema>_<table>` flattening; users get `retrosheet.event` not `retrosheet_event`.

### Tests
- Existing `tests/test_transform.py::TestSchemas` walks `all_factories × all_metadata` and just exercises `make_create_ddl` / `make_copy_ddl` not erroring; the new factory will be picked up automatically once registered. No hardcoded target-name assertions to update there (verify during PLE-339).
- Add a smoke check that the emitted SQL contains `USING columnar` for every table and `CREATE EXTENSION ... citus`. Keep it config-driven — derive expected table set from `all_metadata`, not from a hardcoded list.

### CI
- `make ci` (act-based) runs `BUILD_ENV=test docker compose build` for the e2e job; once PLE-341 lands, it'll build `postgres-columnar` instead of `postgres-cstore-fdw`. No CI workflow changes needed for the swap itself. Multi-arch CI wiring is PLE-345.

### Out of scope for this ADR
- Performance benchmarking — deferred to PLE-338 implementation. If results are surprising, write a follow-up ADR.
- PG 17 / 18 + Citus 14.x. Stay on PG 16 + Citus 13.x for the 2026 refresh to minimize risk; the rest of the suite is also pinned to PG 16. Open a separate ticket post-refresh to revisit.
- Migration tooling for users with existing `postgres-cstore-fdw` data volumes. The README will tell them to nuke the volume and re-pull; we are not writing a data migration.

## References

- Current target source: `transform/src/ddl_factories/postgres_cstore_fdw.py`, `load/postgres_cstore_fdw/`, `load/Dockerfile` (stages `postgres-cstore-fdw-build` / `postgres-cstore-fdw`).
- [`citusdata/cstore_fdw`](https://github.com/citusdata/cstore_fdw) — deprecation notice in README.
- [`citusdata/citus`](https://github.com/citusdata/citus) — successor extension; releases page confirms 14.0 Feb 2026, 13.x with PG 17 support.
- [Citus columnar README](https://github.com/citusdata/citus/blob/main/src/backend/columnar/README.md) — DDL/DML constraints, compression options.
- [`hydradatabase/columnar`](https://github.com/hydradatabase/columnar) — alternative; releases page shows v1.1.2 (Apr 2024) as latest.
- [Hydra PG 17 request issue #272](https://github.com/hydradatabase/columnar/issues/272) — open since Nov 2024.
- [Citus ARM64 issue #3854](https://github.com/citusdata/citus/issues/3854) and [docker#309](https://github.com/citusdata/docker/issues/309) — both open; arm64 build path is source-build today.
