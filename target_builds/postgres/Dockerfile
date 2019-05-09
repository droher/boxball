FROM postgres:11.2-alpine
COPY --from=dockerball-csv.gz /retrosheet /retrosheet
COPY conf.sql /docker-entrypoint-initdb.d/
RUN apk add zstd
RUN mv /retrosheet/retrosheet.sql /docker-entrypoint-initdb.d/
RUN chmod -R 777 /retrosheet