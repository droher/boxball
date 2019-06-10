ARG VERSION
FROM doublewick/boxball:ddl-${VERSION} as ddl
FROM doublewick/boxball:csv-${VERSION} as csv

FROM mysql:8.0.16 as mysql-build
ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes
COPY my.cnf /etc/mysql/conf.d/
COPY A_unzip_csvs.sh z_remove_csvs.sh /docker-entrypoint-initdb.d/
RUN apt-get update && apt-get install -y --no-install-recommends zstd=1.1.2-1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY --chown=mysql:mysql --from=ddl /ddl/mysql.sql /docker-entrypoint-initdb.d/
COPY --chown=mysql:mysql --from=csv /transform/csv /data
