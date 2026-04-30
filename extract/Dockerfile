ARG BUILD_ENV
ARG RETROSHEET_IMAGE=get-retrosheet-${BUILD_ENV}
ARG BASEBALLDATABANK_IMAGE=get-baseballdatabank-${BUILD_ENV}

FROM python:3.13-alpine3.19 AS build-common
RUN apk add --no-cache \
    parallel \
    libtool \
    wget \
    unzip \
    gcc \
    g++ \
    make \
    autoconf \
    automake \
    clang
COPY requirements.txt .
RUN pip install -r requirements.txt
ARG BOXBALL_LOG_LEVEL=INFO
ENV PYTHONPATH="/"
ENV BOXBALL_PARSED_PATH=/parsed \
    BOXBALL_RETROSHEET_PATH=/retrosheet \
    BOXBALL_CODE_TABLES_PATH=/code_tables \
    BOXBALL_BASEBALLDATABANK_CORE_PATH=/baseballdatabank/core \
    BOXBALL_BASEBALLDATABANK_CONTRIB_PATH=/baseballdatabank/contrib \
    BOXBALL_LOG_LEVEL=${BOXBALL_LOG_LEVEL} \
    BOXBALL_STAGE=extract


# `prod` pulls real upstream data; `test` swaps in tiny fixtures under
# extract/fixtures/raw/. Each branch lands the unpacked tree at /retrosheet/
# (or /baseballdatabank/core/) so the downstream extract-* stages don't care
# which one ran.

FROM build-common as get-retrosheet-prod
ARG RETROSHEET_RELEASE_DATE
ARG RETROSHEET_SHA256
# Canonical Retrosheet archive. URL is mutable in place on each Retrosheet
# release, so reproducibility comes from RETROSHEET_SHA256 rather than a git
# SHA. UA header avoids retrosheet.org's occasional 403s on default wget UAs.
# alldata.zip extracts top-level dirs (gamelogs/, events/, biodata/, ...)
# directly with no wrapper.
RUN wget --user-agent='Mozilla/5.0 (compatible; boxball-build)' \
        https://retrosheet.org/downloads/alldata.zip -O retrosheet.zip && \
    echo "${RETROSHEET_SHA256}  retrosheet.zip" | sha256sum -c - && \
    mkdir /retrosheet && \
    unzip -q retrosheet.zip -d /retrosheet && \
    rm retrosheet.zip

FROM build-common as get-retrosheet-test
COPY fixtures/raw/retrosheet.zip /tmp/retrosheet.zip
RUN mkdir /retrosheet && \
    unzip -q /tmp/retrosheet.zip -d /retrosheet && \
    rm /tmp/retrosheet.zip

FROM build-common as get-baseballdatabank-prod
ARG BASEBALLDATABANK_VERSION
# chadwickbureau/baseballdatabank was retired in 2024. corbtastik/lahman-baseball-db
# hosts the canonical SABR Lahman v2025 release (Dec 10, 2025) as a flat tree
# of CSVs at the repo root; rehome under baseballdatabank/core/ to match the
# BOXBALL_BASEBALLDATABANK_CORE_PATH the parser reads.
RUN wget https://github.com/corbtastik/lahman-baseball-db/archive/${BASEBALLDATABANK_VERSION}.zip \
        -O baseballdatabank.zip && \
    unzip -q baseballdatabank.zip && \
    mkdir -p /baseballdatabank/core && \
    mv lahman-baseball-db-*/*.csv /baseballdatabank/core/ && \
    rm -rf lahman-baseball-db-* baseballdatabank.zip

FROM build-common as get-baseballdatabank-test
COPY fixtures/raw/baseballdatabank.zip /tmp/baseballdatabank.zip
RUN mkdir -p /baseballdatabank/core && \
    unzip -q /tmp/baseballdatabank.zip -d /baseballdatabank/core && \
    rm /tmp/baseballdatabank.zip

# Now alias to abstract the build_env difference away downstream
FROM ${RETROSHEET_IMAGE} as get-retrosheet

FROM ${BASEBALLDATABANK_IMAGE} as get-baseballdatabank


FROM build-common as extract-retrosheet
ARG CHADWICK_VERSION
# Download and install Chadwick
RUN wget https://github.com/chadwickbureau/chadwick/archive/${CHADWICK_VERSION}.zip -O chadwick.zip && \
    unzip chadwick.zip && \
    mv chadwick-* chadwick
WORKDIR /chadwick
RUN autoreconf --install && \
    ./configure && \
    make && \
    make install
WORKDIR /
COPY --from=get-retrosheet /retrosheet /retrosheet
# Assemble parsed Retrosheet files
COPY code_tables/ /code_tables
COPY parsers/ /parsers
RUN python -u /parsers/retrosheet.py

FROM build-common as extract-baseballdatabank
COPY --from=get-baseballdatabank /baseballdatabank /baseballdatabank
COPY parsers/ /parsers
# Assemble parsed Baseball Databank files
RUN python -u /parsers/baseballdatabank.py


# Use a skinny build for deployment
FROM alpine:3.19.0
RUN apk add zstd
WORKDIR /extract
COPY --from=extract-baseballdatabank /parsed ./baseballdatabank
COPY --from=extract-retrosheet /parsed ./retrosheet
