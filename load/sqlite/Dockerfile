ARG VERSION
FROM doublewick/boxball:ddl-${VERSION} as ddl
FROM doublewick/boxball:csv-${VERSION} as csv

FROM alpine:3.9.3 as build
RUN apk add --no-cache \
    zstd \
    sqlite
RUN sqlite3 boxball.db ".databases"
COPY --from=ddl /ddl/sqlite.sql .
COPY --from=csv /transform/csv /data
RUN echo "Decompressing fies..." && \
    for f in /data/**/*.csv.zst; do zstd --rm -d ${f}; done && \
    echo "Building db..." && \
    < sqlite.sql sqlite3 -bail boxball.db && \
    rm -rf /data && \
    zstd --rm boxball.db


FROM python:3.7.3-alpine3.9
RUN apk add --no-cache \
    zstd \
    sqlite
RUN pip install sqlite-web==0.3.6
COPY --from=build boxball.db.zst /tmp/
ENTRYPOINT zstd --rm -d /tmp/boxball.db.zst -fo /db/boxball.db && sqlite_web -H 0.0.0.0 -x /db/boxball.db
