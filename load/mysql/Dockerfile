FROM mysql:8.0.16 as mysql-build
ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes
COPY my.cnf /etc/mysql/conf.d/
COPY A_unzip_csvs.sh z_remove_csvs.sh /docker-entrypoint-initdb.d/
RUN apt-get update && apt-get install -y zstd
COPY --chown=mysql:mysql --from=doublewick/boxball:csv-latest /ddl/mysql.sql /docker-entrypoint-initdb.d/
COPY --chown=mysql:mysql --from=doublewick/boxball:csv-latest /data /data
