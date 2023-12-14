ARG VERSION
FROM doublewick/boxball:ddl-${VERSION} as ddl
FROM doublewick/boxball:csv-${VERSION} as csv
FROM doublewick/boxball:parquet-${VERSION} as parquet

FROM yandex/clickhouse-server:22.9.7.34 as clickhouse
COPY z_load.sh /docker-entrypoint-initdb.d/
COPY --chown=clickhouse:clickhouse --from=ddl /ddl/clickhouse.sql /docker-entrypoint-initdb.d/
COPY --chown=clickhouse:clickhouse --from=parquet /transform/parquet /data

FROM drill/apache-drill:1.17.0 as drill
COPY --from=parquet /transform/parquet /data

FROM mysql:8.0.35-debian as mysql
ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes
COPY my.cnf /etc/mysql/conf.d/
COPY A_unzip_csvs.sh z_remove_csvs.sh /docker-entrypoint-initdb.d/
RUN apt-get update && apt-get install -y --no-install-recommends zstd zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY --chown=mysql:mysql --from=ddl /ddl/mysql.sql /docker-entrypoint-initdb.d/
COPY --chown=mysql:mysql --from=csv /transform/csv /data

FROM postgres:16.1-bookworm as postgres
RUN apt-get update && apt-get install -y --no-install-recommends zstd zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY A_build_conf.sql z_run_conf.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=ddl /ddl/postgres.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=csv /transform/csv /data

FROM postgres:13.13-bookworm as postgres-cstore-fdw-build
RUN apt-get update && apt-get install -y --no-install-recommends postgresql-server-dev-13 build-essential zstd libprotobuf-c-dev protobuf-c-compiler wget ca-certificates unzip make gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN wget https://github.com/citusdata/cstore_fdw/archive/master.zip -O cstore_fdw.zip && \
    unzip cstore_fdw.zip && \
    mv cstore_fdw-master cstore_fdw
WORKDIR /cstore_fdw
RUN make && \
    make install
WORKDIR /
RUN echo "shared_preload_libraries = 'cstore_fdw'" >> "${PGDATA}/postgresql.conf"
COPY --chown=postgres:postgres --from=ddl /ddl/postgres_cstore_fdw.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=csv /transform/csv /data
RUN cat /docker-entrypoint-initdb.d/postgres_cstore_fdw.sql

FROM postgres-cstore-fdw-build as postgres-cstore-fdw

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


FROM python:3.11-alpine3.19 AS sqlite
RUN apk add --no-cache \
    zstd \
    sqlite
RUN pip install sqlite-web==0.4.1
COPY --from=sqlite-build boxball.db.zst /tmp/
ENTRYPOINT zstd --rm -d /tmp/boxball.db.zst -fo /db/boxball.db && sqlite_web -H 0.0.0.0 -x /db/boxball.db
