FROM postgres:11.2-alpine
COPY build_conf.sql /docker-entrypoint-initdb.d/
RUN apk add zstd
COPY --chown=postgres:postgres --from=dockerball-csv /data /data
RUN mv /data/load.sql /docker-entrypoint-initdb.d/
