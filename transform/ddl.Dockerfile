FROM python:3.10-slim-bullseye AS build-common
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONPATH="/"

COPY src/ src/
FROM build-common as build-ddl
RUN python -u src/ddl_maker.py

FROM alpine:3.9.3
COPY --from=build-ddl /ddl /ddl
