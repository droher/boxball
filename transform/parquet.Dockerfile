ARG VERSION
FROM doublewick/boxball:extract-${VERSION} as extract

FROM python:3.11-slim-bullseye AS build-common
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONPATH="/"

FROM build-common as build-transform
COPY src/ src/
COPY --from=extract /extract /extract
RUN python -u src/parquet.py

FROM alpine:3.9.3
COPY --from=build-transform /transform /transform
