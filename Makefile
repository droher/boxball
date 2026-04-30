.PHONY: ci ci-style ci-int-test ci-e2e-test ci-list

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
