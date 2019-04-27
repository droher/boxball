FROM alpine:3.9
RUN apk add --no-cache \
    libtool \
    wget \
    unzip \
    gcc \
    g++ \
    make \
    autoconf \
    automake \
    clang
RUN wget https://github.com/chadwickbureau/chadwick/archive/master.zip -O chadwick.zip && \
    unzip chadwick.zip && \
    mv chadwick-master chadwick
RUN cd chadwick && \
    autoreconf --install && \
    ./configure && \
    make && \
    make install
RUN wget https://github.com/chadwickbureau/retrosheet/archive/master.zip -O retrosheet.zip && \
    unzip retrosheet.zip && \
    mv retrosheet-master retrosheet
WORKDIR parsed
COPY chadwick.sh .
RUN chmod a+x chadwick.sh && ./chadwick.sh
