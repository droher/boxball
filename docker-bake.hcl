# Multi-arch overrides for the release pipeline. Layered on top of
# docker-compose.yml: bake reads the compose file (https://docs.docker.com/build/bake/compose-file/),
# inherits build context/args/image tags, and we override `platforms` here.
#
# Compose itself stays host-arch / single-platform so `docker compose build`
# loads intermediates into the local image store, letting downstream
# `FROM doublewick/boxball:<stage>-${VERSION}` resolve locally instead of
# pulling stale registry tags. Multi-arch needs `--push` (buildx can't `--load`
# a manifest list), so it lives here and runs from the release workflow.
#
# Usage (release; needs DH creds — PLE-357/358):
#   docker buildx bake --file docker-compose.yml --file docker-bake.hcl --push multiarch
#
# Local dry-run (single-platform, validates HCL parses + targets resolve):
#   docker buildx bake --file docker-compose.yml --file docker-bake.hcl --print multiarch

# Most targets multi-arch.
target "extract"    { platforms = ["linux/amd64", "linux/arm64"] }
target "ddl"        { platforms = ["linux/amd64", "linux/arm64"] }
target "parquet"    { platforms = ["linux/amd64", "linux/arm64"] }
target "csv"        { platforms = ["linux/amd64", "linux/arm64"] }
target "clickhouse" { platforms = ["linux/amd64", "linux/arm64"] }
target "postgres"   { platforms = ["linux/amd64", "linux/arm64"] }
target "mysql"      { platforms = ["linux/amd64", "linux/arm64"] }
target "sqlite"     { platforms = ["linux/amd64", "linux/arm64"] }

# Citus packagecloud has no arm64 .debs (install.citusdata.com aborts with
# "the Citus repository does not contain packages for non-x86_64
# architectures"). Pin amd64-only.
target "postgres-columnar" { platforms = ["linux/amd64"] }

group "multiarch" {
  targets = [
    "extract",
    "ddl",
    "parquet",
    "csv",
    "clickhouse",
    "postgres",
    "postgres-columnar",
    "mysql",
    "sqlite",
  ]
}

# TODO(PLE-358): the compose `<stage>-latest` twins (extract-latest, ddl-latest,
# …) are *not* in the `multiarch` group. PLAN.md M2 requires both `<stage>-${VERSION}`
# and `<stage>-latest` on Docker Hub. The release workflow should retag rather
# than rebuild — after `bake-push` lands the versioned manifest lists, run:
#   docker buildx imagetools create -t doublewick/boxball:<stage>-latest \
#                                    doublewick/boxball:<stage>-${VERSION}
# per stage (cheap, byte-identical). Don't add the `-latest` services to this
# group — that would rebuild from scratch and waste time + bandwidth.
