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

FROM build-common as build-retrosheet-download
# The trigger copies are a way to force rebuild the data if the repos have been updated
COPY triggers/retrosheet.sha1 .
RUN wget https://github.com/chadwickbureau/retrosheet/archive/master.zip -O retrosheet.zip && \
    unzip retrosheet.zip && \
    mv retrosheet-master retrosheet


FROM build-common as build-retrosheet
# Download and install Chadwick
COPY triggers/chadwick.sha1 .
RUN wget https://github.com/chadwickbureau/chadwick/archive/master.zip -O chadwick.zip && \
    unzip chadwick.zip && \
    mv chadwick-master chadwick
RUN cd chadwick && \
    autoreconf --install && \
    ./configure && \
    make && \
    make install
COPY --from=build-retrosheet-download /retrosheet /retrosheet
# Assemble parsed Retrosheet files into `/parsed/` for next container
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ /src
RUN python -u src/parse_retrosheet.py
ENV PYTHONPATH="/"
RUN python -u /src/ddl_maker.py

FROM build-common as build-baseballdatabank
COPY triggers/baseballdatabank.sha1 .
# Download the baseball databank (aka the lahman database)
RUN wget https://github.com/chadwickbureau/baseballdatabank/archive/master.zip -O baseballdatabank.zip && \
    unzip baseballdatabank.zip && \
    mv baseballdatabank-master baseballdatabank
COPY parse-baseballdatabank.sh .
RUN chmod +x parse-baseballdatabank.sh && ./parse-baseballdatabank.sh

# Use a skinny build for deployment
FROM alpine:3.9.3
COPY --from=build-baseballdatabank /parsed /baseballdatabank
COPY --from=build-retrosheet /parsed /retrosheet
