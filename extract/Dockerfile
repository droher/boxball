ARG BUILD_ENV
ARG RETROSHEET_IMAGE=get-retrosheet-${BUILD_ENV}
ARG BASEBALLDATABANK_IMAGE=get-baseballdatabank-${BUILD_ENV}

FROM python:3.7.3-alpine3.9 AS build-common
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
ENV PYTHONPATH="/"


# `prod` gets the full datasets, while `test` provides fixtures with small sample data for each file
FROM build-common as get-retrosheet-prod
ARG RETROSHEET_VERSION
RUN wget https://github.com/chadwickbureau/retrosheet/archive/${RETROSHEET_VERSION}.zip -O retrosheet.zip

FROM build-common as get-retrosheet-test
COPY fixtures/raw/retrosheet.zip .

FROM build-common as get-baseballdatabank-prod
ARG BASEBALLDATABANK_VERSION
RUN wget https://github.com/chadwickbureau/baseballdatabank/archive/${BASEBALLDATABANK_VERSION}.zip -O baseballdatabank.zip

FROM build-common as get-baseballdatabank-test
COPY fixtures/raw/baseballdatabank.zip .

# Now alias to abstract the build_env difference away downstream
FROM ${RETROSHEET_IMAGE} as get-retrosheet

FROM ${BASEBALLDATABANK_IMAGE} as get-baseballdatabank


FROM build-common as extract-retrosheet
ARG CHADWICK_VERSION
COPY code_tables/ /code_tables
COPY parsers/ /parsers
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
COPY --from=get-retrosheet retrosheet.zip .
RUN unzip retrosheet.zip && \
    mv retrosheet-* retrosheet
# Assemble parsed Retrosheet files
RUN python -u /parsers/retrosheet.py

FROM build-common as extract-baseballdatabank
ARG BASEBALLDATABANK_VERSION
COPY parsers/ /parsers
COPY --from=get-baseballdatabank baseballdatabank.zip .
RUN unzip baseballdatabank.zip && \
    mv baseballdatabank-* baseballdatabank
# Assemble parsed Baseball Databank files
RUN python -u /parsers/baseballdatabank.py


# Use a skinny build for deployment
FROM alpine:3.9.3
RUN apk add zstd
WORKDIR /extract
COPY --from=extract-baseballdatabank /parsed ./baseballdatabank
COPY --from=extract-retrosheet /parsed ./retrosheet
