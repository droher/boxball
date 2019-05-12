FROM python:3.7.3-alpine3.9 AS build-common
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

FROM alpine:3.9.3
COPY --from=build-ddl /ddl /ddl
