FROM python:3.7.3-alpine3.9 AS build-common
RUN apk add --no-cache \
    gcc \
    postgresql-libs \
    musl-dev \
    postgresql-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONPATH="/"

FROM build-common as build-ddl
COPY src/ src/
# Builds ddl scripts for prod container
RUN python -u src/ddl_maker.py