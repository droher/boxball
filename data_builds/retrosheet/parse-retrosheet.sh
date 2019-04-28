#!/usr/bin/env bash

set -eu

mkdir parsed
cd parsed

# Easy stuff first: merge files that don't need parsing
echo "Loading gamelog..."
cat /retrosheet/gamelog/*.TXT > /parsed/gamelog.csv
pigz /parsed/gamelog.csv

echo "Loading schedule..."
cat /retrosheet/schedule/*.TXT > /parsed/schedule.csv
pigz /parsed/schedule.csv

# Remove header from park codes (only one file so no merge necessary)
echo "Loading parks..."
tail -n +2 /retrosheet/misc/parkcode.txt > /parsed/parkcode.csv
pigz /parsed/parkcode.csv

# Add a year column to the roster files before merging, since only in filename
# This is the only change to the schema we want to make
echo "Loading rosters..."
for filename in /retrosheet/rosters/*.ROS; do
    year=$(echo "${filename}" | grep -oE '[0-9]{4}')
    sed -i 's/\r//g' "${filename}"
    sed -i "s|^|${year},|g" "${filename}"
    # One blank line at end of file causes extra year write, need to delete
    sed -i '$ d' "${filename}"

done
cat /retrosheet/rosters/*.ROS > /parsed/rosters.csv
pigz rosters.csv

# Now we parse the event files with the Chadwick toolkit
event_parse='cwevent -q -y {} -f 0-96 -x 0-62 {}* >> /parsed/event.csv'
game_parse='cwgame -q -y {} -f 0-83 -x 0-94 {}* >> /parsed/game.csv'
sub_parse='cwsub -q -y {} {}* >> /parsed/sub.csv'
daily_parse='cwdaily -q -y {} {}* >> /parsed/daily.csv'
comment_parse='cwcomment -q -y {} {}* >> /parsed/comment.csv'


event_folders=(asg post regular)
chadwick_output_types=(event game sub daily comment)
parse_funcs=("${event_parse}" "${game_parse}" "${sub_parse}" "${daily_parse}" "${comment_parse}")

# Get rid of box score files (This makes me sad, would like to build a parser for them)
rm /retrosheet/event/**/*.{EBA,EBN}

mkdir "${chadwick_output_types[@]}"

# Parse each event file once per each extraction function
for folder in "${event_folders[@]}"; do
    echo "Loading $folder events..."
    for func in "${parse_funcs[@]}"; do
        cd /retrosheet/event/"${folder}" && \
            # Find all of the team files and grab the years from each of them
            # Then pass each year as an argument to cwevent, which will process
            # all files in the folder of that year
            # Not all years will have data_builds (e.g. 1994 post and 1945 asg),
            # So we allow it to finish even if one command errors out
            find | grep "TEAM" | grep -oE '[0-9]{4}$' | \
            xargs -P $(nproc) -i sh -c "${func} || true"
    done
done

# Merge all yearly files into one and gzip
for type in "${chadwick_output_types[@]}"; do
    echo "Zipping $type output..."
    pigz /parsed/"${type}".csv
done
echo "Finished Retrosheet transform."
