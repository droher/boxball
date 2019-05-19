FROM yandex/clickhouse-server:19.6.2.11
COPY z_load.sh /docker-entrypoint-initdb.d/
COPY --chown=clickhouse:clickhouse --from=doublewick/boxball:ddl-0.0.1 /ddl/clickhouse.sql /docker-entrypoint-initdb.d/
COPY --chown=clickhouse:clickhouse --from=doublewick/boxball:parquet-0.0.1 /transform/parquet /data
