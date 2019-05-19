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


FROM build-common as build-retrosheet-download
ARG RETROSHEET_VERSION
RUN wget https://github.com/chadwickbureau/retrosheet/archive/${RETROSHEET_VERSION}.zip -O retrosheet.zip


FROM build-common as build-retrosheet
ARG CHADWICK_VERSION
# Download and install Chadwick
COPY code_tables/ /code_tables
COPY parsers/ /parsers
RUN wget https://github.com/chadwickbureau/chadwick/archive/${CHADWICK_VERSION}.zip -O chadwick.zip && \
    unzip chadwick.zip && \
    mv chadwick-* chadwick
RUN cd chadwick && \
    autoreconf --install && \
    ./configure && \
    make && \
    make install
COPY --from=build-retrosheet-download retrosheet.zip .
RUN unzip retrosheet.zip && \
    mv retrosheet-* retrosheet
# Assemble parsed Retrosheet files into `/parsed/` for prod container
RUN python -u /parsers/retrosheet.py

FROM build-common as build-baseballdatabank
ARG BASEBALLDATABANK_VERSION
COPY parsers/ /parsers
# Download the baseball databank (aka the lahman database)
RUN wget https://github.com/chadwickbureau/baseballdatabank/archive/${BASEBALLDATABANK_VERSION}.zip -O baseballdatabank.zip && \
    unzip baseballdatabank.zip && \
    mv baseballdatabank-* baseballdatabank
# Assemble parsed Retrosheet files into `/parsed/` for prod container
RUN python -u /parsers/baseballdatabank.py

# Use a skinny build for deployment
FROM alpine:3.9.3
RUN apk add zstd
WORKDIR extract
COPY --from=build-baseballdatabank /parsed ./baseballdatabank
COPY --from=build-retrosheet /parsed ./retrosheet
