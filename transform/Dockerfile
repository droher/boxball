FROM python:3.7.3-slim-stretch AS build-common
COPY requirements.txt .
COPY src/ src/
RUN pip install -r requirements.txt
ENV PYTHONPATH="/"

FROM build-common as build-ddl
RUN python -u src/ddl_maker.py

FROM build-ddl as build-parquet
COPY --from=doublewick/boxball:csv-latest /data /data
RUN python -u src/parquet.py


FROM alpine:3.9.3
COPY --from=build-ddl /ddl /ddl
COPY --from=build-parquet /data/parquet /parquet
