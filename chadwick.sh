#!/usr/bin/env bash

set -eu

event_parse='cwevent -y {} -f 0-96 -x 0-62 {}* > /parsed/event/{}.csv'
game_parse='cwgame -y {} -f 0-83 -x 0-94 {}* > /parsed/game/{}.csv'
sub_parse='cwsub -y {} {}* > /parsed/sub/{}.csv'
daily_parse='cwdaily -y {} {}* > /parsed/daily/{}.csv'


event_folders=(post regular)
parse_funcs=("${event_parse}" "${game_parse}" "${sub_parse}" "${daily_parse}")

mkdir event
mkdir game
mkdir sub
mkdir daily
mkdir comment

for func in "${parse_funcs[@]}"; do
    echo "${func}"
done

# Event processing
for folder in "${event_folders[@]}"; do
    for func in "${parse_funcs[@]}"; do
        cd /retrosheet/event/"${folder}" && \
            # Find all of the team files and grab the years from each of them
            # Then pass each year as an argument to cwevent, which will process
            # all files in the folder of that year
            find | grep "TEAM" | grep -o '....$' | \
            xargs -P $(nproc) -i sh -c "${func}"
    done
done
