FROM doublewick/boxball:parquet-0.0.1 as parquet

FROM drill/apache-drill:1.16.0
COPY --from=parquet /transform/parquet /data
