ARG VERSION
FROM doublewick/boxball:ddl-${VERSION} as ddl
FROM doublewick/boxball:csv-${VERSION} as csv
FROM doublewick/boxball:parquet-${VERSION} as parquet

FROM clickhouse/clickhouse-server:23.11.2.11 as clickhouse
COPY z_load.sh /docker-entrypoint-initdb.d/
COPY --chown=clickhouse:clickhouse --from=ddl /ddl/clickhouse.sql /docker-entrypoint-initdb.d/
COPY --chown=clickhouse:clickhouse --from=parquet /transform/parquet /data

# Oracle Linux variant (default `mysql:<ver>` tag) instead of -debian: Oracle
# stopped publishing arm64 builds for the -debian flavor, and the -debian image
# also ships an expired apt signing key (B7B3B788A8D3785C) that breaks
# `apt-get update` at build time. Oracle Linux 9 image is multi-arch.
# zstd ships in the OL9 base (used by A_unzip_csvs.sh), so no package install
# is needed. If pinning to a future mysql tag, re-verify zstd availability.
FROM mysql:8.0.40 as mysql
ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes
COPY my.cnf /etc/mysql/conf.d/
COPY A_unzip_csvs.sh z_remove_csvs.sh /docker-entrypoint-initdb.d/
COPY --chown=mysql:mysql --from=ddl /ddl/mysql.sql /docker-entrypoint-initdb.d/
COPY --chown=mysql:mysql --from=csv /transform/csv /data

FROM postgres:16.1-bookworm as postgres
RUN apt-get update && apt-get install -y --no-install-recommends zstd zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY A_build_conf.sql z_run_conf.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=ddl /ddl/postgres.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=csv /transform/csv /data

FROM postgres:16.1-bookworm as postgres-columnar
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates gnupg zstd zip && \
    curl -sSf https://install.citusdata.com/community/deb.sh | bash && \
    apt-get install -y --no-install-recommends postgresql-${PG_MAJOR}-citus-13.0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN echo "shared_preload_libraries = 'citus'" >> /usr/share/postgresql/${PG_MAJOR}/postgresql.conf.sample
COPY A_build_conf.sql z_run_conf.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=ddl /ddl/postgres_columnar.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=csv /transform/csv /data

FROM alpine:3.19.0 as sqlite-build
RUN apk add --no-cache \
    zstd \
    sqlite
RUN sqlite3 boxball.db ".databases"
COPY --from=ddl /ddl/sqlite.sql .
COPY --from=csv /transform/csv /data
RUN echo "Decompressing fies..." && \
    for f in /data/**/*.csv.zst; do zstd --rm -d ${f}; done && \
    echo "Building db..." && \
    < sqlite.sql sqlite3 -bail -echo boxball.db && \
    rm -rf /data && \
    zstd --rm boxball.db


FROM python:3.13-alpine3.19 AS sqlite
RUN apk add --no-cache \
    zstd \
    sqlite
RUN pip install sqlite-web==0.4.1
COPY --from=sqlite-build boxball.db.zst /tmp/
ENTRYPOINT zstd --rm -d /tmp/boxball.db.zst -fo /db/boxball.db && sqlite_web -H 0.0.0.0 -x /db/boxball.db
