ARG VERSION
FROM doublewick/boxball:ddl-${VERSION} as ddl
FROM doublewick/boxball:csv-${VERSION} as csv

FROM postgres:11.2-alpine as build
RUN apk --no-cache add \
    zstd \
    alpine-sdk \
    protobuf-c-dev \
    wget
RUN wget https://github.com/citusdata/cstore_fdw/archive/master.zip -O cstore_fdw.zip && \
    unzip cstore_fdw.zip && \
    mv cstore_fdw-master cstore_fdw
WORKDIR /cstore_fdw
RUN make && \
    make install
WORKDIR /
RUN echo "shared_preload_libraries = 'cstore_fdw'" >> "${PGDATA}/postgresql.conf"
COPY --chown=postgres:postgres --from=ddl /ddl/postgres_cstore_fdw.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=csv /transform/csv /data
RUN cat /docker-entrypoint-initdb.d/postgres_cstore_fdw.sql

FROM build
