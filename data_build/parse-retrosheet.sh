#!/bin/bash

set -eu

mkdir parsed
cd parsed

## Easy stuff first: merge files that don't need parsing
#echo "Loading gamelog..."
#cat /retrosheet/gamelog/*.TXT > /parsed/gamelog.csv
#pigz /parsed/gamelog.csv
#
#echo "Loading schedule..."
#cat /retrosheet/schedule/*.TXT > /parsed/schedule.csv
#pigz /parsed/schedule.csv
#
## Remove header from park codes (only one file so no merge necessary)
#echo "Loading parks..."
#tail -n +2 /retrosheet/misc/parkcode.txt > /parsed/parkcode.csv
#pigz /parsed/parkcode.csv
#
## Add a year column to the roster files before merging, since only in filename
## This is the only change to the schema we want to make
#echo "Loading rosters..."
#for filename in /retrosheet/rosters/*.ROS; do
#    year=$(echo "${filename}" | grep -oE '[0-9]{4}')
#    sed -i 's/\r//g' "${filename}"
#    sed -i "s|^|${year},|g" "${filename}"
#    # One blank line at end of file causes extra year write, need to delete
#    sed -i '$ d' "${filename}"
#
#done
#cat /retrosheet/rosters/*.ROS > /parsed/rosters.csv
#pigz rosters.csv

# Now we parse the event files with the Chadwick toolkit
daily_parse='cwdaily -q -y {} {}* >> /parsed/daily.csv'
comment_parse='cwcomment -q -y {} {}* >> /parsed/comment.csv'
game_parse='cwgame -q -y {} -f 0-83 -x 0-94 {}* >> /parsed/game.csv'
sub_parse='cwsub -q -y {} {}* >> /parsed/sub.csv'
event_parse='cwevent -q -y {} -f 0-96 -x 0-62 {}* >> /parsed/event.csv'

event_folders=(asg post regular)
chadwick_output_types=(daily comment event game sub)
parse_funcs=("${daily_parse}" "${comment_parse}" "${sub_parse}" "${game_parse}" "${event_parse}")

# Parse each event file once per each extraction function
for func in "${parse_funcs[@]}"; do
    # Only the first two funcs (daily/comment) handle box score files, so we remove them once we're done
    # Ideally want to do this with regex without removing
    # but can't figure it out inside the shell string commands above
    if [[ "${func}" == "${comment_parse}" ]]; then
        echo "Removing box score files from parsing tree as not needed for remaining parsers"
        rm /retrosheet/event/**/*.{EBA,EBN}
    fi
    echo "Parsing: '"${func}"'"
    for folder in "${event_folders[@]}"; do
        echo "Loading $folder events..."
        cd /retrosheet/event/"${folder}" && \
            # Find all of the team files and grab the years from each of them
            # Then pass each year as an argument to cwevent, which will process
            # all files in the folder of that year
            find | grep "TEAM" | grep -oE '[0-9]{4}$' | sort | \
            xargs -P $(nproc) -i bash -c "shopt -s nullglob && ${func}"
    done
done

# Merge all yearly files into one and gzip
for type in "${chadwick_output_types[@]}"; do
    echo "Zipping $type output..."
    pigz /parsed/"${type}".csv
done
echo "Finished Retrosheet transform."
