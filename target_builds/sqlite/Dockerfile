FROM alpine:3.9.3 as build
RUN apk add --no-cache \
    zstd \
    sqlite
RUN sqlite3 containerball.db ".databases"
COPY --from=doublewick/containerball:csv-latest /ddl/sqlite.sql .
RUN cat sqlite.sql
COPY --from=doublewick/containerball:csv-latest /data /data
RUN echo "Decompressing fies..." && \
    for f in /data/**/*.csv.zst; do zstd --rm -d $f; done && \
    echo "Building db..." && \
    cat sqlite.sql | sqlite3 containerball.db
RUN rm -rf /data
RUN zstd --rm containerball.db


FROM python:3.7.3-alpine3.9
RUN apk add --no-cache \
    zstd \
    sqlite
RUN pip install sqlite-web==0.3.6
WORKDIR db
COPY --from=build containerball.db.zst .
ENTRYPOINT zstd --rm -d containerball.db.zst && sqlite_web -H 0.0.0.0 -x containerball.db
