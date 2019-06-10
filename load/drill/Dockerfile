ARG VERSION
FROM doublewick/boxball:parquet-${VERSION} as parquet

FROM drill/apache-drill:1.16.0
COPY --from=parquet /transform/parquet /data
