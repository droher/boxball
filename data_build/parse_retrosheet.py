import fileinput
from pathlib import Path
import subprocess
import re
import gzip

RETROSHEET_PATH = Path("/retrosheet")
OUTPUT_PATH = Path("/parsed")
OUTPUT_PATH.mkdir(exist_ok=True)

RETROSHEET_SUBDIRS = "gamelog", "schedule", "parks", "rosters", "event"
EVENT_FOLDERS = "asg", "post", "regular"

PBP_SUFFIXES = "EDA", "EDN", "EVA", "EVN"
PBP_SUFFIX_GLOB = ".{" + ",".join(PBP_SUFFIXES) + "}"

PARSE_FUNCS = {
    "daily": "cwdaily -q -y {year} {year}*",
    "comment": "cwcomment -q -y {year} {year}*",
    "game": "cwgame -q -y {year} -f 0-83 -x 0-94 {year}*",
    "sub": "cwsub -q -y {year} {year}*",
    "event": "cwevent -q -y {year} -f 0-96 -x 0-62 {year}*"
}


def parse_simple_files():

    def concat_files(input_path: Path, output_path: Path, glob: str = "*",
                     prepend_filename: bool = False,
                     strip_header: bool = False):
        files = (f for f in input_path.glob(glob) if f.is_file())
        with gzip.open(output_path, 'wt') as fout, fileinput.input(files) as fin:
            for line in fin:
                if fin.isfirstline() and strip_header:
                    continue
                if prepend_filename:
                    year = Path(fin.filename()).stem
                    modified_line = "{},{}".format(year, line)
                    fout.write(modified_line)
                else:
                    fout.write(line)

    retrosheet_base = Path(RETROSHEET_PATH)
    output_base = Path(OUTPUT_PATH)
    output_base.mkdir(exist_ok=True)
    subdirs = {subdir: retrosheet_base / subdir for subdir in RETROSHEET_SUBDIRS}

    print("Writing simple files...")
    concat_files(subdirs["gamelog"], output_base / "gamelog.csv.gz", glob="*.TXT")
    concat_files(subdirs["schedule"], output_base / "schedule.csv.gz", glob="*.TXT")
    concat_files(subdirs["parks"], output_base / "parks.csv.gz", glob="parkcode.txt", strip_header=True)
    concat_files(subdirs["rosters"], output_base / "schedule.csv.gz", glob="*.ROS", prepend_filename=True)


def parse_event_types():
    def parse_events(output_type: str):
        event_base = RETROSHEET_PATH / "event"
        output_path = OUTPUT_PATH.joinpath(output_type).with_suffix(".csv.gz")
        command_template = PARSE_FUNCS[output_type]
        fout = gzip.open(output_path, 'wt')
        for folder in EVENT_FOLDERS:
            data_path = event_base.joinpath(folder)
            years = {re.match("[0-9]{4}", f.stem)[0] for f in data_path.iterdir()
                     if re.match("[0-9]{4}", f.stem)}
            for year in sorted(years):
                command = command_template.format(year=year, pbp_only=PBP_SUFFIX_GLOB)
                print(data_path, command)
                process = subprocess.run(command, capture_output=True, cwd=data_path, check=True, shell=True,
                                         text=True)
                fout.write(process.stdout)
        fout.close()

    def drop_boxscore_files():
        for f in RETROSHEET_PATH.rglob("*.EB*"):
            f.unlink()

    parse_events("sub")
    parse_events("daily")
    drop_boxscore_files()
    parse_events("comment")
    parse_events("game")
    parse_events("event")


parse_simple_files()
parse_event_types()
