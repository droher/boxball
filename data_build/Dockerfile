FROM python:3.7.3-alpine3.9 AS build-common
RUN apk add --no-cache \
    libtool \
    wget \
    unzip \
    pigz \
    gcc \
    g++ \
    make \
    autoconf \
    automake \
    clang \
    postgresql-libs \
    musl-dev \
    postgresql-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONPATH="/"


FROM build-common as build-retrosheet-download
# The trigger copies are a way to force rebuild the data if the repos have been updated
COPY triggers/retrosheet.sha1 .
RUN wget https://github.com/chadwickbureau/retrosheet/archive/master.zip -O retrosheet.zip


FROM build-common as build-retrosheet
# Download and install Chadwick
COPY triggers/chadwick.sha1 .
COPY code_tables/ /code_tables
COPY parsers/ /parsers
RUN wget https://github.com/chadwickbureau/chadwick/archive/master.zip -O chadwick.zip && \
    unzip chadwick.zip && \
    mv chadwick-master chadwick
RUN cd chadwick && \
    autoreconf --install && \
    ./configure && \
    make && \
    make install
COPY --from=build-retrosheet-download retrosheet.zip .
RUN unzip retrosheet.zip && \
    mv retrosheet-master retrosheet
# Assemble parsed Retrosheet files into `/parsed/` for prod container
RUN python -u /parsers/parse_retrosheet.py

FROM build-common as build-baseballdatabank
COPY triggers/baseballdatabank.sha1 .
COPY parsers/ /parsers
# Download the baseball databank (aka the lahman database)
RUN wget https://github.com/chadwickbureau/baseballdatabank/archive/master.zip -O baseballdatabank.zip && \
    unzip baseballdatabank.zip && \
    mv baseballdatabank-master baseballdatabank
# Assemble parsed Retrosheet files into `/parsed/` for prod container
RUN python -u /parsers/parse_baseballdatabank.py

FROM build-common as build-ddl
COPY ddl_generators /ddl_generators
# Builds ddl scripts for prod container
RUN python -u /ddl_generators/ddl_maker.py

# Use a skinny build for deployment
FROM alpine:3.9.3
RUN apk add zstd
WORKDIR data
COPY --from=build-ddl /ddl /ddl
COPY --from=build-baseballdatabank /parsed ./baseballdatabank
COPY --from=build-retrosheet /parsed ./retrosheet
