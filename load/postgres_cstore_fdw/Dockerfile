ARG VERSION
FROM doublewick/boxball:ddl-${VERSION} as ddl
FROM doublewick/boxball:csv-${VERSION} as csv

FROM postgres:13.2 as build
RUN apt-get update && apt-get install -y --no-install-recommends postgresql-server-dev-13 build-essential zstd libprotobuf-c-dev protobuf-c-compiler wget ca-certificates unzip make gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
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
