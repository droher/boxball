FROM postgres:11.2-alpine as build
RUN apk --no-cache add \
    zstd \
    alpine-sdk \
    protobuf-c-dev \
    wget
RUN wget https://github.com/citusdata/cstore_fdw/archive/master.zip -O cstore_fdw.zip && \
    unzip cstore_fdw.zip && \
    mv cstore_fdw-master cstore_fdw
RUN cd cstore_fdw && \
    make && \
    make install
RUN echo "shared_preload_libraries = 'cstore_fdw'" >> ${PGDATA}/postgresql.conf
COPY --chown=postgres:postgres --from=doublewick/containerball:csv-latest /ddl/postgres_cstore_fdw.sql /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres --from=doublewick/containerball:csv-latest /data /data
RUN cat /docker-entrypoint-initdb.d/postgres_cstore_fdw.sql

FROM build