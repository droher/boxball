FROM python:3.7.3-slim-stretch AS build-common
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONPATH="/"

FROM build-common as build-transform
ARG REPO
ARG VERSION
COPY src/ src/
COPY --from=${REPO}:extract-${VERSION} /extract /extract
RUN python -u src/parquet.py

FROM alpine:3.9.3
COPY --from=build-transform /transform/parquet /transform/parquet
