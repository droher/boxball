# Stub Dockerfile — real stages live in load/Dockerfile. This file exists only
# so docker-compose can use load/postgres-columnar as build context for the
# init-script + conf SQL copies, mirroring the pattern of load/postgres.
ARG VERSION
FROM doublewick/boxball:postgres-columnar-${VERSION}
