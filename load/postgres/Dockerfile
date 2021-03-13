ARG VERSION
FROM doublewick/boxball:ddl-${VERSION} as ddl
FROM doublewick/boxball:csv-${VERSION} as csv

ENV POSTGRES_PASSWORD="N/A"

FROM postgres:13.2
RUN apt-get update && apt-get install -y --no-install-recommends zstd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY A_build_conf.sql z_run_conf.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=ddl /ddl/postgres.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=csv /transform/csv /data
