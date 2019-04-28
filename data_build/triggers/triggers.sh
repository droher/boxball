#!/usr/bin/env bash
# This file pulls the hash of the master commit from each chadwickbureau repo we use.
# Changes to the hash will cause the corresponding cache in the Docker build to be wiped.

set -eu

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

repos=(baseballdatabank retrosheet chadwick)
for repo in ${repos[@]}; do
    hash=$(git ls-remote "https://github.com/chadwickbureau/${repo}.git" master | cut -f 1)
    echo "${hash}" > "${DIR}/${repo}.sha1"
done
