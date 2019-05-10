import fileinput
from pathlib import Path
from typing import Callable
import subprocess
import re
import sys

from parsers.util import compress

# MS-DOS eof character that needs to be specially handled in some files
DOS_EOF = chr(26)

RETROSHEET_PATH = Path("/retrosheet")
CODE_TABLES_PATH = Path("/code_tables")
OUTPUT_PATH = Path("/parsed")

RETROSHEET_SUBDIRS = "gamelog", "schedule", "misc", "rosters", "event"
EVENT_FOLDERS = "asg", "post", "regular"

PARSE_FUNCS = {
    "daily": "cwdaily -q -y {year} {year}*",
    "comment": "cwcomment -q -y {year} {year}*",
    "game": "cwgame -q -y {year} -f 0-83 -x 0-94 {year}*",
    "sub": "cwsub -q -y {year} {year}*",
    "event": "cwevent -q -y {year} -f 0-96 -x 0-62 {year}*"
}


def parse_code_tables() -> None:
    for file in CODE_TABLES_PATH.glob("*.csv"):
        compress(file, OUTPUT_PATH)


def parse_simple_files() -> None:
    def concat_files(input_path: Path, output_file: Path, glob: str = "*",
                     prepend_filename: bool = False,
                     strip_header: bool = False,
                     check_dupes: bool = True):
        files = (f for f in input_path.glob(glob) if f.is_file())
        with open(output_file, 'wt') as fout, fileinput.input(files) as fin:
            lines = set()
            for line in fin:
                # Remove DOS EOF character (CRTL+Z)
                new_line = line.strip(DOS_EOF)
                if not new_line or new_line.isspace():
                    continue
                if fin.isfirstline() and strip_header:
                    continue
                if prepend_filename:
                    year = Path(fin.filename()).stem[-4:]
                    new_line = "{},{}".format(year, new_line)
                if new_line in lines:
                    print("Duplicate row in {}: {}".format(fin.filename(), new_line), file=sys.stderr)
                    continue
                if check_dupes:
                    lines.add(new_line)
                fout.write(new_line)
        return compress(output_file, OUTPUT_PATH)

    retrosheet_base = Path(RETROSHEET_PATH)
    output_base = Path(OUTPUT_PATH)
    output_base.mkdir(exist_ok=True)
    subdirs = {subdir: retrosheet_base / subdir for subdir in RETROSHEET_SUBDIRS}

    print("Writing simple files...")
    concat_files(subdirs["gamelog"], output_base / "gamelog.csv", glob="*.TXT", check_dupes=False)
    concat_files(subdirs["schedule"], output_base / "schedule.csv", glob="*.TXT")
    concat_files(subdirs["misc"], output_base / "park.csv", glob="parkcode.txt", strip_header=True)
    concat_files(subdirs["rosters"], output_base / "roster.csv", glob="*.ROS", prepend_filename=True)


def parse_event_types():
    def parse_events(output_type: str, clean_func: Callable = None):
        event_base = RETROSHEET_PATH / "event"
        output_file = OUTPUT_PATH.joinpath(output_type).with_suffix(".csv")
        command_template = PARSE_FUNCS[output_type]
        f_out_inflated = open(output_file, 'w')
        for folder in EVENT_FOLDERS:
            data_path = event_base.joinpath(folder)
            years = {re.match("[0-9]{4}", f.stem)[0] for f in data_path.iterdir()
                     if re.match("[0-9]{4}", f.stem)}
            for year in sorted(years):
                command = command_template.format(year=year)
                print(data_path, command)
                subprocess.run(command, cwd=data_path, check=True, shell=True, text=True,
                               stdout=f_out_inflated)
        f_out_inflated.close()
        if clean_func:
            clean_func(output_file)
        compress(output_file, OUTPUT_PATH)

    def drop_boxscore_files():
        for f in RETROSHEET_PATH.rglob("*.EB*"):
            f.unlink()

    def find_malformed_comments(file: Path):
        new_output_file = file.with_suffix(file.suffix + ".tmp")
        existing_comments = set()
        with open(file, 'r') as ifh, open(new_output_file, 'w') as ofh:
            for line in ifh:
                if line.count('"') % 2 != 0:
                    print("Bad comment line: {}".format(line), file=sys.stderr)
                else:
                    existing_comments.add(line)
                    ofh.write(line)

        file.unlink()
        new_output_file.rename(file)

    parse_events("sub")
    parse_events("daily")
    drop_boxscore_files()
    parse_events("comment", clean_func=find_malformed_comments)
    parse_events("game")
    parse_events("event")


if __name__ == "__main__":
    OUTPUT_PATH.mkdir(exist_ok=True)
    parse_code_tables()
    parse_simple_files()
    parse_event_types()