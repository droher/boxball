FROM python:3.13-slim-bookworm AS build-common
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONPATH="/"
ENV BOXBALL_OUTPUT_PATH=/ddl \
    BOXBALL_EXTRACT_PATH=/extract \
    BOXBALL_TRANSFORM_PATH=/transform

COPY src/ src/
FROM build-common as build-ddl
RUN python -u src/ddl_maker.py

FROM alpine:3.19.0
COPY --from=build-ddl /ddl /ddl
