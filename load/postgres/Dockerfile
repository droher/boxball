ARG VERSION
FROM doublewick/boxball:ddl-${VERSION} as ddl
FROM doublewick/boxball:csv-${VERSION} as csv

FROM postgres:11.2-alpine
COPY A_build_conf.sql z_run_conf.sql /docker-entrypoint-initdb.d/
RUN apk add zstd
COPY --chown=postgres:postgres --from=ddl /ddl/postgres.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=csv /transform/csv /data
