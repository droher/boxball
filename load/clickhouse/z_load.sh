#!/bin/bash

set -eu

for d in /data/*
do
    for f in /data/$(basename ${d})/*
    do
        echo ${f}
        cat ${f} | clickhouse-client --database=$(basename ${d}) --query="INSERT INTO $(basename ${f} .parquet) FORMAT Parquet"
        clickhouse-client --database=$(basename ${d}) --query="SELECT COUNT(*) FROM $(basename ${f} .parquet)" | cat
    done
done
