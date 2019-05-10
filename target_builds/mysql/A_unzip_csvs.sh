#!/bin/bash
for filename in /data/**/*.csv.zst; do
    echo "Decompressing ${filename}..."
    zstd --rm -d "${filename}"
done
cat /docker-entrypoint-initdb.d/mysql.sql