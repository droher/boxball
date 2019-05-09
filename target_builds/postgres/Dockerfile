FROM postgres:11.2-alpine
COPY build_conf.sql /docker-entrypoint-initdb.d/
RUN apk add zstd
COPY --chown=postgres:postgres --from=dockerball-csv /retrosheet /retrosheet
RUN mv /retrosheet/retrosheet.sql /docker-entrypoint-initdb.d/
