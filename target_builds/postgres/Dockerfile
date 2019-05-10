FROM postgres:11.2-alpine
COPY A_build_conf.sql z_run_conf.sql /docker-entrypoint-initdb.d/
RUN apk add zstd
COPY --chown=postgres:postgres --from=dockerball-csv /ddl/postgres.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=dockerball-csv /data /data
