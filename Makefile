.PHONY: ci ci-style ci-int-test ci-e2e-test ci-list buildx-bootstrap bake-print bake-push build-local

# Local GitHub Actions runner via `act`.
# All targets exec `.github/workflows/ci.yml` against the same runner image
# the workflow uses on GitHub. Requires `act` (brew install act) + a running
# Docker daemon. Image config lives in `.actrc`.

WORKFLOW := .github/workflows/ci.yml
EVENT    := pull_request

ci:
	act $(EVENT) -W $(WORKFLOW)

ci-style:
	act $(EVENT) -W $(WORKFLOW) -j style

ci-int-test:
	act $(EVENT) -W $(WORKFLOW) -j int-test

ci-e2e-test:
	act $(EVENT) -W $(WORKFLOW) -j e2e-test

ci-list:
	act $(EVENT) -W $(WORKFLOW) -l

# Multi-arch builds live in `docker-bake.hcl` and run via `docker buildx bake`.
# Compose itself stays host-arch / single-platform so `docker compose build`
# loads intermediates into the local image store, letting downstream
# `FROM doublewick/boxball:<stage>-${VERSION}` resolve locally.
#
# The default `docker` buildx driver cannot build for multiple platforms; bake
# needs the `docker-container` driver. This target creates an idempotent
# builder named `boxball`. Bake selects it via `BUILDX_BUILDER`.
buildx-bootstrap:
	@if ! docker buildx inspect boxball >/dev/null 2>&1; then \
		echo "Creating docker-container buildx builder 'boxball'..."; \
		docker buildx create --name boxball --driver docker-container; \
		docker buildx inspect --bootstrap boxball; \
	else \
		echo "Builder 'boxball' already exists."; \
	fi
	@echo "Multi-arch dry-run: make bake-print"
	@echo "Multi-arch push:    make bake-push  (needs DH login; release workflow drives this in CI)"

# Single-platform amd64 build of the full chain. Two reasons to pin amd64:
#  1) `postgres-columnar` is amd64-only (Citus has no arm64 packages). If the
#     rest of the chain is built host-arch (e.g. arm64 on Apple Silicon),
#     postgres-columnar's `FROM doublewick/boxball:ddl-${VERSION}` looks for
#     an amd64 image, doesn't find one locally, and falls back to the
#     registry — pulling the previous release's tag, which predates the
#     PLE-338 schema rename and breaks `COPY --from=ddl /ddl/postgres_columnar.sql`.
#     Building everything amd64 keeps the local image store coherent.
#  2) Multi-arch needs `--push` (buildx can't `--load` manifest lists), which
#     is the release workflow's job. For local validation, single-platform
#     amd64 matches CI (ubuntu-latest GH runners) and the published artifact.
#
# The serialized boundaries (extract → transform → load) avoid compose v2's
# parallel-build race where downstream `FROM <tag>` lookups beat upstream
# tags landing in the local store.
#
# On arm64 hosts this emulates amd64 via QEMU (slow but coherent). For native
# arm64 dev images, build a single non-columnar target host-arch:
# `docker compose build postgres`.
build-local: export DOCKER_DEFAULT_PLATFORM=linux/amd64
build-local:
	docker compose build extract
	docker compose build ddl parquet csv
	docker compose build clickhouse postgres postgres-columnar mysql sqlite

BAKE_FILES := --file docker-compose.yml --file docker-bake.hcl
BAKE_TARGET ?= multiarch

# Print the resolved bake graph (multi-arch platforms, tags, contexts) without
# building. Validates the bake file parses + targets resolve.
bake-print:
	docker buildx bake $(BAKE_FILES) --print $(BAKE_TARGET)

# Build + push multi-arch manifest lists. Requires:
#   1) `make buildx-bootstrap` (docker-container builder)
#   2) `docker login` against $$REPO's registry (DH for prod)
# `--push` is mandatory: buildx cannot `--load` multi-platform output to the
# local image store.
bake-push:
	BUILDX_BUILDER=boxball docker buildx bake $(BAKE_FILES) --push $(BAKE_TARGET)
