ARG VERSION
FROM doublewick/boxball:parquet-${VERSION} as parquet

FROM drill/apache-drill:1.17.0
COPY --from=parquet /transform/parquet /data
