FROM python:3.7.3-alpine3.9 AS build-ddl
RUN apk add --no-cache \
    gcc \
    postgresql-libs \
    musl-dev \
    postgresql-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONPATH="/"
COPY src/ src/
RUN python -u src/ddl_maker.py

FROM python:3.7.3-slim-stretch as build-parquet
RUN apt-get update && apt-get install -y zstd
RUN pip install pyarrow
COPY src/ src/
COPY --from=doublewick/boxball:csv-latest /data /data

FROM alpine:3.9.3
COPY --from=build-ddl /ddl /ddl
