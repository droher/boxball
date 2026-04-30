# Changelog

All notable changes to Boxball are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project
adopts [calendar versioning](https://calver.org/) (`YYYY.MINOR.PATCH`,
where `MINOR` resets to `0` each calendar year and increments per data
refresh, `PATCH` covers post-refresh fixes).

The Boxball release workflow (`.github/workflows/release.yml`) reads the
section matching the published tag and uses it as the GitHub Release body,
so each version below must have a `## [X.Y.Z]` heading with the same
version string as the tag.

## [2026.0.0] — 2026-04-30

First release of the Boxball 2026 Refresh. After ~18 months of drift, the
project is back on current upstream data and a modernized build chain.

### Added

- New `postgres-columnar` target on PostgreSQL 16 + Citus 13 columnar
  (replaces the retired `postgres-cstore-fdw` target).
- Multi-architecture (amd64 + arm64) image manifests for every kept target
  except `postgres-columnar` (Citus has no arm64 packages upstream).
- Structured build-time logging across the extract / transform / DDL stages,
  controlled by `BOXBALL_LOG_LEVEL` and tagged per stage with `BOXBALL_STAGE`.
- Local CI parity via `make ci` (runs `.github/workflows/ci.yml` through
  `act` against the same runner image GitHub Actions uses).
- `auth-smoke.yml` workflow that validates Docker Hub PAT and PyPI OIDC
  trusted publishing without performing a real publish.
- `release.yml` workflow that builds + pushes multi-arch images, generates
  Parquet and CSV bundles, and publishes a GitHub Release on `v*.*.*` tags.

### Changed

- Refreshed Retrosheet to its December 2025 release, fetched directly from
  `https://retrosheet.org/downloads/alldata.zip` and integrity-pinned by
  sha256 (no GitHub mirror dependency).
- Refreshed Baseball Databank to SABR Lahman v2025
  (`corbtastik/lahman-baseball-db@b5e7327`), replacing the retired
  `chadwickbureau/baseballdatabank` source. Lahman v2025 reorganized the
  `People` and `Parks` tables — Boxball's schemas absorb the column
  reordering while preserving column names and primary keys, so existing
  queries (`WHERE player_id = …`, `WHERE park_id = …`) continue to work.
- Bumped Python to 3.13 across every Dockerfile, GitHub Actions job, and
  the `boxball-schemas` package metadata.
- Migrated the host development stack to `uv` + `ruff` + `basedpyright`;
  consolidated tooling configuration into `pyproject.toml`.
- Bumped SQLAlchemy to 2.x; replaced the deprecated `sqlalchemy_fdw` with
  inline `CREATE FOREIGN TABLE` DDL.
- Switched the MySQL target base image from `mysql:8.0.35-debian` to
  `mysql:8.0.40` (Oracle Linux 9 default), resolving the upstream
  Debian-flavor apt-key expiry and adding arm64 support.
- Test fixtures regenerated against the new canonical upstreams; tests
  rewritten to assert invariants rather than hardcoded counts.
- Repo-anchored `BOXBALL_*_PATH` env vars now drive every path resolver,
  so host runs and tests no longer depend on the current working directory.

### Removed

- Drill target (low usage, unmaintained upstream).
- `postgres-cstore-fdw` target (cstore_fdw is no longer maintained;
  `postgres-columnar` replaces it).
- CircleCI configuration (replaced by GitHub Actions).
