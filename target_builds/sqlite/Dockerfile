FROM alpine:3.9.3 as build
RUN apk add --no-cache \
    zstd \
    sqlite
RUN sqlite3 containerball.db ".databases"
COPY --from=dockerball-csv /ddl/sqlite.sql .
RUN cat sqlite.sql
COPY --from=dockerball-csv /data /data
RUN echo "Decompressing fies..." && \
    for f in /data/**/*.csv.zst; do zstd --rm -d $f; done && \
    echo "Building db..." && \
    cat sqlite.sql | sqlite3 containerball.db


FROM python:3.7.3-alpine3.9
USER containerball
RUN pip install sqlite-web==0.3.6
WORKDIR db
COPY --from=build containerball.db .