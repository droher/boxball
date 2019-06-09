FROM doublewick/boxball:ddl-0.0.1 as ddl
FROM doublewick/boxball:parquet-0.0.1 as parquet

FROM yandex/clickhouse-server:19.6.2.11
COPY z_load.sh /docker-entrypoint-initdb.d/
COPY --chown=clickhouse:clickhouse --from=ddl /ddl/clickhouse.sql /docker-entrypoint-initdb.d/
COPY --chown=clickhouse:clickhouse --from=parquet /transform/parquet /data
