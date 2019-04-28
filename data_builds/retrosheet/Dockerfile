FROM alpine:3.9 AS build-env
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
    clang
# Download and install Chadwick
RUN wget https://github.com/chadwickbureau/chadwick/archive/master.zip -O chadwick.zip && \
    unzip chadwick.zip && \
    mv chadwick-master chadwick
RUN cd chadwick && \
    autoreconf --install && \
    ./configure && \
    make && \
    make install
# Download Retrosheet files
RUN wget https://github.com/chadwickbureau/retrosheet/archive/master.zip -O retrosheet.zip && \
    unzip retrosheet.zip && \
    mv retrosheet-master retrosheet
# Assemble parsed Retrosheet files into `/parsed/` for next container
COPY ../parse-retrosheet.sh .
RUN chmod a+x parse-retrosheet.sh && ./parse-retrosheet.sh

# Use a skinny build for deployment
FROM alpine:3.9
COPY --from=build-env /parsed /retrosheet