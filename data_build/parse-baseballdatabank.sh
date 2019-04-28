#!/usr/bin/env bash

set -eu

mkdir parsed

for filename in /baseballdatabank/core/*.csv; do
    lower=$(basename "${filename}" | tr '[:upper:]' '[:lower:]')
    mv "${filename}" "/parsed/${lower}"
    pigz "/parsed/${lower}"
done