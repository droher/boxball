FROM postgres:11.2-alpine
ARG REPO
ARG VERSION
COPY A_build_conf.sql z_run_conf.sql /docker-entrypoint-initdb.d/
RUN apk add zstd
COPY --chown=postgres:postgres --from=${REPO}:ddl-{VERSION} /ddl/postgres.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=${REPO}:csv-{VERSION} /transform/csv /data
