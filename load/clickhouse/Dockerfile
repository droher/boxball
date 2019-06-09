ARG VERSION
FROM doublewick/boxball:ddl-${VERSION} as ddl
FROM doublewick/boxball:parquet-${VERSION} as parquet

FROM yandex/clickhouse-server:19.6.2.11
COPY z_load.sh /docker-entrypoint-initdb.d/
COPY --chown=clickhouse:clickhouse --from=ddl /ddl/clickhouse.sql /docker-entrypoint-initdb.d/
COPY --chown=clickhouse:clickhouse --from=parquet /transform/parquet /data
