.PHONY: ci ci-style ci-int-test ci-e2e-test ci-list buildx-bootstrap compose-build

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

# One-time local bootstrap for multi-platform builds. The default `docker`
# buildx driver cannot build for multiple platforms in a single invocation;
# `docker compose build` against a multi-platform service errors with
# "Multi-platform build is not supported for the docker driver". This target
# creates a `docker-container` builder named `boxball` (idempotent). It does
# *not* `--use` the builder as the global default, since `docker buildx use`
# is not honoured by `docker compose build` in compose v2 — pair it with
# `make compose-build SVC=...` (or set `BUILDX_BUILDER=boxball` manually).
buildx-bootstrap:
	@if ! docker buildx inspect boxball >/dev/null 2>&1; then \
		echo "Creating docker-container buildx builder 'boxball'..."; \
		docker buildx create --name boxball --driver docker-container; \
		docker buildx inspect --bootstrap boxball; \
	else \
		echo "Builder 'boxball' already exists."; \
	fi
	@echo "Run multi-arch builds via: make compose-build SVC=<service>"
	@echo "Or manually:               BUILDX_BUILDER=boxball docker compose build [<service>]"

# Wrapper around `docker compose build` that selects the docker-container
# builder explicitly via env var (compose v2 ignores `docker buildx use`).
# Pass SVC=<service> to build a single target, or omit to build everything.
# Pass BUILD_ENV=test for fixture-driven smoke builds.
compose-build:
	BUILDX_BUILDER=boxball docker compose build $(SVC)
