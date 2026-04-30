ARG VERSION
FROM doublewick/boxball:extract-${VERSION} as extract

FROM python:3.13-slim-bookworm AS build-common
COPY requirements.txt .
RUN pip install -r requirements.txt
ARG BOXBALL_LOG_LEVEL=INFO
ENV PYTHONPATH="/"
ENV BOXBALL_OUTPUT_PATH=/ddl \
    BOXBALL_EXTRACT_PATH=/extract \
    BOXBALL_TRANSFORM_PATH=/transform \
    BOXBALL_LOG_LEVEL=${BOXBALL_LOG_LEVEL} \
    BOXBALL_STAGE=transform-parquet

FROM build-common as build-transform
COPY src/ src/
COPY --from=extract /extract /extract
RUN python -u src/parquet.py

FROM alpine:3.19.0
COPY --from=build-transform /transform /transform
