# ADR 0002: Upstream Retrosheet and Baseball Databank Data Sources

- **Status:** Accepted
- **Date:** 2026-04-30
- **Linear ticket:** PLE-352 (spike); implementers: PLE-353 (`.env` repoint), PLE-354 (VERSION + SHA bump)
- **Authors:** Boxball 2026 Refresh

## Context

`extract/Dockerfile` pulls Retrosheet and Baseball Databank from third-party forks rather than canonical upstream:

- **Retrosheet:** `https://github.com/droher/retrosheet-mirror/archive/${RETROSHEET_VERSION}.zip` — pinned `RETROSHEET_VERSION=8449632be02cdf743932600f3218d77e059d5c91`, which is the head of the **`working`** branch of that fork (Dec 14, 2023).
- **Baseball Databank:** `https://github.com/tom-719/baseballdatabank/archive/${BASEBALLDATABANK_VERSION}.zip` — pinned `BASEBALLDATABANK_VERSION=28169eaf9007200d7f51160713c647eac64f9aa8`, head of `master` on that fork (Oct 16, 2023). The Dockerfile carries the comment `# Temporarily grab from old fork until 2023 data appears`.

The 2026 refresh is the first time we've been forced to look at these pins since 2023, so this spike asks: can we drop the forks and pull from upstream? It turns out the answer is different for each source, because the upstream landscape has changed materially.

This ADR is research-only — no `.env` edits, no extract pipeline runs. PLE-353 and PLE-354 are the implementers.

## Findings

### Retrosheet — `droher/retrosheet-mirror`

**What the fork is.** Three permanent branches, per its README:

| Branch | Head SHA | What it contains |
|---|---|---|
| `official` | `319bf913…` | Mirror of `retrosheet.org/downloads/alldata.zip`, with the nested archives extracted to directories. |
| `submitted` | `486fe197…` | `official` + corrections submitted upstream to Retrosheet's QA. |
| `working` | `8449632b…` | `submitted` + locally-applied fixes plus a **folder restructure** that flattens `alldata/<subdir>/` to top-level `<subdir>/`. |

**The current `.env` pin is `working`-branch HEAD**, not `submitted` as one might assume from the comment in CLAUDE.md.

**What the fork actually does for Boxball.** Two distinct value-adds, only one of which is data correction:

1. **Layout adapter (load-bearing).** `parsers/retrosheet.py` expects `RETROSHEET_PATH = Path("retrosheet")` to contain top-level `gamelogs/`, `schedules/`, `rosters/`, `events/`, `allstar/`, `postseason/`, `teams/` plus `biofile.csv` / `ballparks.csv`. Upstream `alldata.zip` (and the `official` branch mirroring it) has those nested under an extra `alldata/` directory. The `working` branch's "Restructure folders" commit (`f52cd5f`, Nov 2023) flattens this. **Without that flatten, the parser breaks at the `data_path = event_base.joinpath(folder)` step.**
2. **Hand-applied data corrections (small but cumulative).** The 17 commits on `working` apply:
   - 6 hand-edited corrections to historical event/box files: 1917BOS, 1919SLA, 1926NGL, 1939BOS, 1941BRO, 1947PHI, 1948NGL, 2011NLD2 (one-character fixes to pitch types, caught-stealing notation, `presadj` values, dates, player IDs).
   - Several Negro Leagues deduplication passes ("Remove NLB All-Star dupes", "Remove NLB postseason dupes", "Remove NLB dupes", "Stray dupes") in Dec 2023.
   - "Fix malformed ball-strike count", "Fix trailing space on BIR team", "gamelog fixes", "Fixes to box files".

**Upstream state.** Retrosheet itself has shipped two newer releases since the fork froze in Dec 2023:
- July 2024 release
- December 2024 release (mirrored as `chadwickbureau/retrosheet@1f11638`, Feb 1, 2025)
- July 2025 release (`chadwickbureau/retrosheet@01dc2cd`, Sep 27, 2025)
- **December 2025 release** (`chadwickbureau/retrosheet@bf5af7d`, Jan 8, 2026) — current HEAD of `chadwickbureau/retrosheet@official`.

`chadwickbureau/retrosheet` is actively maintained by `tturocy` (Ted Turocy, Chadwick Bureau), with merges from Retrosheet's `official` branch on each release.

**Why we can't just switch to `chadwickbureau/retrosheet`.** Its `master` branch has a **completely different layout** from `alldata.zip`: top-level `gamelog/`, `reference/`, `seasons/` (vs. our parser's expectation of `gamelogs/`, `events/`, `rosters/`, `schedules/`, `allstar/`, `postseason/`, `teams/`, `biofile.csv`, `ballparks.csv`). The chadwickbureau repo is "an augmented version of the data" intended for use with Chadwick library tooling, not a bytewise mirror. Switching to it would require rewriting `parsers/retrosheet.py` end-to-end — out of scope for the refresh.

**The other upstream options:**

| Option | Pros | Cons |
|---|---|---|
| **(A) Pull `https://retrosheet.org/downloads/alldata.zip` directly** | Truly canonical, no third-party. Zero patching to expected file layout once the parser is taught about the extra `alldata/` wrapper. | URL is a moving target — no SHA pin, no reproducibility, no archive of past versions. We'd have to mirror it ourselves anyway to get reproducible builds. We lose the dedup / data-fix patches. retrosheet.org occasionally returns 403 to non-browser User-Agents (saw it in this spike). |
| **(B) `chadwickbureau/retrosheet@official` branch (`bf5af7d`)** | SHA-pinnable. Active maintenance. Tracks `alldata.zip` on each official release. | Needs spot-check that the `official` branch is a verbatim mirror of `alldata.zip` with the same `alldata/` wrapper. Loses the dedup / data-fix patches. Parser needs a 1-line tweak to step into `alldata/` after unzip. |
| **(C) Stay on `droher/retrosheet-mirror`, advance the pin to a fresh `working`-branch commit that incorporates the Dec 2025 release.** | Zero parser changes. Keeps all dedup / fix patches. | The fork isn't currently up to date past Dec 2023. PLE-352 is a research spike — the user (also the fork owner) has not yet rebased `working` onto Dec 2025. |
| **(D) Rebuild the fork's value-add as Boxball-side processing**: pull from chadwickbureau or retrosheet.org, then apply the dedup / restructure / hand-corrections in `parsers/retrosheet.py`. | Eliminates the fork entirely. Long-term cleanest. | Substantial scope: each of the 6 hand-corrections becomes a small data-patch step, and the NLB dedup needs to be re-derived (we don't have a single committed diff representing it — it spans multiple commits on `working`). Not 2026-refresh-sized. |

### Baseball Databank — `tom-719/baseballdatabank`

**The upstream is gone.** `https://github.com/chadwickbureau/baseballdatabank` returns **404**. The repo is no longer in `chadwickbureau`'s org listing (which currently has 6 repos: `chadwick`, `retrosplits`, `retrosheet`, `register`, `chadwickbureau.github.io`, `data-boxscores` — no `baseballdatabank`). Confirmed via `/orgs/chadwickbureau/repositories` and the GitHub API for the repo (also 404).

The Chadwick Bureau appears to have **discontinued the Baseball Databank** as a maintained repository. This was hinted at by `cbwinslow/baseballdatabank`'s README, which is another fork of the original chadwickbureau repo and explicitly labels it `**a legacy resource**`. `cbwinslow`'s fork is frozen at Oct 22, 2022 (`8a908d51…`), data through 2021 season.

`tom-719/baseballdatabank` (our current pin) is itself a fork of `orrski/baseballdatabank` (which was a fork of the chadwickbureau repo). It's frozen at Oct 16, 2023 (`28169eaf…`), with data through the 2022 season. Last 10 commits are "Updated People." cosmetic touch-ups by the same `tturocy` (Chadwick Bureau) account that maintains `chadwickbureau/retrosheet` — i.e., this fork is the last preserved snapshot from when chadwickbureau was still publishing.

**Where the data went.** The Lahman Baseball Database — which the Baseball Databank was built on — is now distributed directly by SABR:

- **Lahman v2025** released Jan 2, 2026 (CSV format updated Feb 18, 2026 with BOM fixes).
- Hosted at `https://sabr.app.box.com/s/y1prhc795jk8zvmelfd3jq7tl389y6cd` (CSV variant) — a Box.com share, not a Git URL.
- The CSV release uses the same file names as Baseball Databank's `core/` directory (`People.csv`, `Batting.csv`, `Pitching.csv`, `Teams.csv`, `AllstarFull.csv`, `Appearances.csv`, etc.) — schema-compatible with what `parsers/baseballdatabank.py` expects.
- Available secondary Git mirror: `cdalzell/Lahman`'s `source-data/baseballdatabank-master.zip` (9.06 MB), the build artifact for the R package. R package is at version 14.0-0 (Feb 11, 2026) representing the 2025 data, so the embedded zip is current. Last `source-data/` commit is May 2024 ("include source-data data files"); the zip is updated in-place without per-update commits, so SHA-pinning the parent repo at a specific commit doesn't reliably pin the data version.

**No upstream PR will resurrect `chadwickbureau/baseballdatabank`.** This is a deliberate end-of-life by the maintainer (the README on `cbwinslow`'s mirror calls it "legacy"; the chadwickbureau org has removed the repo). There is nothing to wait for.

**Options for replacing the fork:**

| Option | Pros | Cons |
|---|---|---|
| **(A) Stay on `tom-719/baseballdatabank@28169eaf` indefinitely** | Zero changes. Currently works. | Permanently capped at 2022 season data. The 2023, 2024, and 2025 seasons will never appear here. |
| **(B) Switch to SABR Lahman v2025 CSVs (Box.com URL)** | Most up-to-date data (through 2025 season). Same file names, schema-compatible with current parser. | URL is a Box.com share, not GitHub — no SHA pin. Box's share-link stability over years is a real risk; SABR could re-issue the share link or restructure, breaking our build. Requires `wget`/`curl` of a Box link, which Box gates behind a JS-rendered redirect (need `?download=1` or `/file/<id>` direct-download flow — has to be tested). The `extract/` Dockerfile assumes `${VAR}.zip` of a GitHub archive; switching to Box requires Dockerfile shape change. |
| **(C) Switch to `cdalzell/Lahman/source-data/baseballdatabank-master.zip`** | GitHub-hosted, SHA-pinnable repo. Already through 2025 data (R package version 14.0-0). Schema-compatible (same `core/` layout). | Pinning the repo SHA does NOT pin the zip's contents — the zip gets updated in place by the R package author without a new commit per update. So we'd be SHA-pinning the wrapper but not the data. Acceptable if we trust `cdalzell` not to silently rewrite history, but technically we lose reproducibility-by-SHA. |
| **(D) Mirror Lahman v2025 ourselves** (e.g., `droher/lahman-mirror`, similar to retrosheet-mirror) | Full control. Reproducible by SHA. | Manual ongoing maintenance burden. We have to download from SABR Box and re-publish on each Lahman release (annually). |

## Decision

**Two sources, two different decisions.**

### Retrosheet: stay on `droher/retrosheet-mirror` for 2026 refresh; advance the pin.

- The fork is doing real work that the parser depends on (folder flatten + data corrections). Dropping it within the refresh scope means either (B) chadwickbureau/retrosheet w/ parser tweak + losing patches, or (D) re-implementing the patches Boxball-side. Both are bigger scope than this refresh window allows, and neither is required to ship the 2026 refresh.
- **Action for PLE-353/354:** the fork owner is the same person as the user driving this refresh. The right move is to rebase `working` onto Retrosheet's December 2025 release locally, push it to `droher/retrosheet-mirror`, and bump `RETROSHEET_VERSION` to the new `working`-branch HEAD. That's a one-time fork-maintenance task happening alongside the Boxball pin bump, not a Boxball code change.
- **Concrete `.env` value for PLE-353:** `RETROSHEET_VERSION=<TBD pending fork rebase>` — the new `working`-branch HEAD after `droher/retrosheet-mirror` is brought current with `chadwickbureau/retrosheet@official` (`bf5af7d40e1f0c33026074705cda8ed1c5177f95`, Dec 2025 release) and the local patch series (folder restructure + dedup commits + 6 hand-corrections) is replayed. PLE-354 owners must record the resulting SHA in `.env` and in PLE-354's commit message.
- **Update the comment** in `extract/Dockerfile` to note the fork is a layout-adapter + QA-patch holder, not "temporary".
- **Open a follow-up ticket** (post-2026-refresh) to evaluate Option D — eliminating the fork by absorbing its patches into `parsers/retrosheet.py`. Out of scope for the refresh.

### Baseball Databank: switch to `cdalzell/Lahman` source-data zip.

- The chadwickbureau upstream is dead (404, removed from the org). There is no upstream PR/issue to wait on; the wait-for-2023-data comment in `extract/Dockerfile` is now permanently false. `tom-719` is itself a stale fork that's frozen at the 2022 season.
- SABR Box.com is the actual canonical source going forward but is operationally unfriendly (Box share URL, JS-mediated download, not GitHub-shaped, not SHA-pinnable).
- `cdalzell/Lahman` is the cleanest middle ground: GitHub-hosted (fits the existing Dockerfile shape), maintained as the upstream of an active CRAN package (so kept current with each Lahman release), and the embedded `source-data/baseballdatabank-master.zip` is byte-for-byte the modern Lahman dataset in the file layout `parsers/baseballdatabank.py` already understands.
- The zip-content-not-pinned-by-SHA caveat is real but small: `cdalzell/Lahman` is a long-running R package repo (8+ years, CRAN-published) — it's not going to silently rewrite history. We'll accept commit-pin + manual recheck on each refresh.
- **Action for PLE-353:** repoint `BASEBALLDATABANK_VERSION` to a SHA in `cdalzell/Lahman` that contains the 2025 data zip. Update `extract/Dockerfile` to:
  - change the `wget` URL to `https://github.com/cdalzell/Lahman/archive/${BASEBALLDATABANK_VERSION}.zip`,
  - add an `unzip` step that pulls `Lahman-*/source-data/baseballdatabank-master.zip` out and unzips it (or, simpler, change the `mv baseballdatabank-* baseballdatabank` step to navigate the nested structure).
  - delete the `# Temporarily grab from old fork until 2023 data appears` comment; replace with a one-liner explaining the SABR/Lahman lineage and the `cdalzell/Lahman` indirection.
- **Concrete `.env` value for PLE-353:** `BASEBALLDATABANK_VERSION=<TBD: latest commit SHA on cdalzell/Lahman master that contains source-data/baseballdatabank-master.zip>`. PLE-353 owners must `git ls-remote https://github.com/cdalzell/Lahman.git refs/heads/master` at execution time and record the SHA. Verify by extracting the zip and confirming `core/Teams.csv` contains a 2025 row before committing.

### Out of scope for both decisions

- Schema changes to accommodate Lahman 2025's reorg (Negro Leagues integration, new columns, BOM in CSVs, the Master→People rename — though the rename is already reflected in the file we use). PLE-355 / PLE-356 territory; if any of those schema changes are observed during PLE-353 build, raise immediately and decide whether to absorb in this refresh or defer.
- Eliminating the Retrosheet fork entirely. Tracked as a follow-up post-refresh.

## Consequences

### For PLE-353 — `.env` repoint + Dockerfile updates

- `RETROSHEET_VERSION`: bump to new `working`-branch HEAD on `droher/retrosheet-mirror` after the fork is rebased onto Retrosheet Dec 2025 release. **Blocked on fork rebase.**
- `BASEBALLDATABANK_VERSION`: bump to a fresh SHA on `cdalzell/Lahman@master`. **Resolved at PLE-353 execution time** via `git ls-remote`.
- `extract/Dockerfile`:
  - Change `wget https://github.com/tom-719/baseballdatabank/archive/${BASEBALLDATABANK_VERSION}.zip` to `wget https://github.com/cdalzell/Lahman/archive/${BASEBALLDATABANK_VERSION}.zip`.
  - Adjust the unzip + `mv` flow to reach `Lahman-*/source-data/baseballdatabank-master.zip`, unzip *that*, and rename the inner `baseballdatabank-master/` to `baseballdatabank` so `parsers/baseballdatabank.py`'s `Path("baseballdatabank/core")` and `Path("baseballdatabank/contrib")` keep working unchanged.
  - Replace the `# Temporarily grab from old fork until 2023 data appears` comment with an accurate one (e.g. `# chadwickbureau/baseballdatabank was retired in 2024; cdalzell/Lahman ships the canonical 2025 SABR Lahman release in the same file layout.`).
  - Update the comment near the Retrosheet `wget` to note that `droher/retrosheet-mirror` is intentional (folder flatten + QA patches), not a temporary workaround.
- Smoke-build with `BUILD_ENV=test docker compose build extract` to ensure the new unzip path lands files where parsers expect them. (Note: test-mode reads from `extract/fixtures/raw/baseballdatabank.zip` which is a snapshot of the OLD fork's layout — confirm fixtures still match the parser's assumptions, and if not, rebuild fixtures from the new source as part of PLE-353.)
- Schema-compat smoke check: `pytest tests/test_extract.py` against the new fixtures to ensure `parsers/baseballdatabank.py`'s depascalize step still produces the expected output filenames.

### For PLE-354 — VERSION + SHA bump

- Bump `VERSION=2024.0.0` → `VERSION=2026.0.0` (or whatever the refresh version is) per release-numbering convention.
- The new `RETROSHEET_VERSION` and `BASEBALLDATABANK_VERSION` SHAs from PLE-353 are committed in the same change.
- Release notes (when master flip happens) should mention the data-source migration and the new dataset coverage (Retrosheet through 2025 season; Lahman 2025 — through 2025 season including Negro Leagues integration).

### For tests / CI

- `extract/fixtures/raw/baseballdatabank.zip` may need to be rebuilt from the new source so its inner structure matches the new layout. If the fixture is already a `core/`-rooted zip, no change; if it's a `baseballdatabank-<sha>/` zip, the parser logic unzips and renames identically and fixtures should still work. Verify during PLE-353.
- `extract/fixtures/raw/retrosheet.zip` does not need rebuilding — fork structure unchanged on the rebased `working` branch.
- `tests/conftest.py` unzips both fixtures into `/tmp/boxball/`; no test changes required as long as the in-zip layout is preserved.

### For CLAUDE.md

- The Gotchas line "Retrosheet is fetched from `droher/retrosheet-mirror` (a fork) rather than upstream, pinned by SHA in `.env`. Baseball Databank similarly pinned to a fork (`tom-719/baseballdatabank`) per a comment in `extract/Dockerfile` waiting on upstream 2023 data." needs updating after PLE-353 lands. Replace with: Retrosheet still pinned to `droher/retrosheet-mirror@working`-branch (intentional layout adapter + QA patch holder); Baseball Databank now pinned to `cdalzell/Lahman` whose `source-data/baseballdatabank-master.zip` is the canonical SABR Lahman v2025 release after `chadwickbureau/baseballdatabank` was retired.

## References

- [`droher/retrosheet-mirror`](https://github.com/droher/retrosheet-mirror) — branches `official`, `submitted`, `working`. Current `.env` pin `8449632b` is `working` HEAD as of Dec 14, 2023.
- [`chadwickbureau/retrosheet`](https://github.com/chadwickbureau/retrosheet) — actively maintained, latest release `bf5af7d` (Jan 8, 2026, Dec 2025 Retrosheet release). Different file layout from `alldata.zip`.
- [Retrosheet alldata.zip](https://retrosheet.org/downloads/alldata.zip) — canonical Retrosheet archive (326 MB).
- [`chadwickbureau/baseballdatabank`](https://github.com/chadwickbureau/baseballdatabank) — **404, repo retired**.
- [`tom-719/baseballdatabank`](https://github.com/tom-719/baseballdatabank) — current `.env` pin `28169eaf`. Frozen Oct 2023.
- [`cbwinslow/baseballdatabank`](https://github.com/cbwinslow/baseballdatabank) — alternate fork, README labels itself "legacy resource". Frozen Oct 2022.
- [SABR Lahman Database](https://sabr.org/lahman-database/) — canonical successor distribution. v2025 released Jan 2, 2026.
- [`cdalzell/Lahman`](https://github.com/cdalzell/Lahman) — R package containing the 2025 Lahman release in `source-data/baseballdatabank-master.zip`, schema-compatible with the retired Baseball Databank.
