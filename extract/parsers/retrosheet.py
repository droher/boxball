import re
import subprocess
import sys
from functools import lru_cache
from pathlib import Path
import shutil

import fileinput
from typing import Callable, Set

from parsers.util import compress, OUTPUT_PATH

# MS-DOS eof character that needs to be specially handled in some files
DOS_EOF = chr(26)

RETROSHEET_PATH = Path("retrosheet")
CODE_TABLES_PATH = Path("code_tables")

RETROSHEET_SUBDIRS = "gamelogs", "schedules", "rosters"
EVENT_FOLDERS = "allstar", "postseason", "events"

PARSE_FUNCS = {
    "daily": "cwdaily -q -y {year} {year}*",
    "comment": "cwcomment -q -y {year} {year}*",
    "game": "cwgame -q -y {year} -f 0-83 -x 0-94 {year}*",
    "sub": "cwsub -q -y {year} {year}*",
    "event": "cwevent -q -y {year} -f 0-96 -x 0-62 {year}*"
}


def _pbp_game_ids(pattern) -> Set[str]:
    print(f"Searching for game ids under pattern {pattern}...")
    ids = set()
    files = RETROSHEET_PATH.glob(pattern)
    with fileinput.input(files) as fin:
        for line in fin:
            if line.startswith("id,"):
                ids.add(line.split(",")[1].strip())
    print(f"Found {len(ids)} games under pattern {pattern}")
    return ids


@lru_cache(maxsize=1)
def event_game_ids() -> Set[str]:
    return _pbp_game_ids("**/*.EV*")


@lru_cache(maxsize=1)
def deduced_game_ids() -> Set[str]:
    deduced_games = _pbp_game_ids("**/*.ED*")
    dupes = deduced_games & event_game_ids()
    if dupes:
        raise ValueError(f"Deduced games already appear in non-deduced files: {dupes}")
    return deduced_games


@lru_cache(maxsize=1)
def all_pbp_game_ids() -> Set[str]:
    return event_game_ids() | deduced_game_ids()


def remove_redundant_box_score_files() -> None:
    pbp_ids = all_pbp_game_ids()
    # Un-lazify the generator to prevent it picking up new file
    boxfiles = list(RETROSHEET_PATH.glob("**/*.EB*"))
    for boxfile in sorted(boxfiles):
        temp_path = boxfile.with_suffix(".tmp")
        keep = True
        removed_all = True
        removed = 0
        print(f"Searching {boxfile} for box scores already existing in PBP accounts...")
        with open(boxfile, "r") as f_in, open(temp_path, "w") as f_out:
            for line in f_in:
                if line.startswith("id,"):
                    game_id = line.split(",")[1]
                    if game_id in pbp_ids:
                        removed += 1
                        keep = False
                    else:
                        keep = True
                if keep:
                    removed_all = False
                    f_out.write(line)
        print(f"Removing {removed} accounts from {boxfile}")
        boxfile.unlink()
        if removed_all:
            print(f"Removed all accounts, not rewriting {boxfile}")
            temp_path.unlink()
        else:
            temp_path.rename(boxfile)


class RetrosheetParser:
    """
    Class for running Retrosheet extract. Mostly in a class for testing convenience.
    """

    @staticmethod
    def write_deduced_gamelist():
        tmpfile = OUTPUT_PATH / "deduced_game.csv"
        tmpfile.write_text("\n".join(sorted(deduced_game_ids())) + "\n")
        print("Writing list of deduced PBP game IDs...")
        compress(tmpfile, OUTPUT_PATH)

    @staticmethod
    def parse_code_tables() -> None:
        for file in CODE_TABLES_PATH.glob("*.csv"):
            compress(file, OUTPUT_PATH)

    @staticmethod
    def parse_simple_files() -> None:
        def concat_files(input_path: Path, output_file: Path, glob: str = "*",
                         prepend_filename: bool = False,
                         strip_header: bool = False,
                         check_dupes: bool = True):
            files = [f for f in input_path.glob(glob) if f.is_file()]
            if not files:
                raise ValueError(f"No files found under {input_path} with glob {glob}")
            with open(output_file, 'wt') as fout, fileinput.input(files) as fin:
                lines = set()
                for line in fin:
                    year = Path(fin.filename()).stem[-4:]
                    # Remove DOS EOF character (CRTL+Z)
                    new_line = line.strip(DOS_EOF)
                    original_line = new_line
                    if not new_line or new_line.isspace():
                        continue
                    if fin.isfirstline() and strip_header:
                        continue
                    if prepend_filename:
                        new_line = f"{year},{new_line}"
                    if new_line in lines:
                        print(f"Duplicate row in {fin.filename()}: {original_line.strip()}")
                        continue
                    # TODO: Fix NLB roster file shape in raw data
                    if "roster" in output_file.name and len(new_line.split(",")) == 7:
                        print(f"Fixing row in file {fin.filename()} with missing data: " + original_line.strip())
                        new_line = new_line.strip() + ","
                    elif "roster" in output_file.name and len(new_line.split(",")) < 7:
                        print(f"Skipping row in file {fin.filename()} with missing data: " + original_line.strip())
                        continue
                    if check_dupes:
                        lines.add(new_line)
                    fout.write(new_line.strip() + "\n")
                return compress(output_file, OUTPUT_PATH)

        retrosheet_base = Path(RETROSHEET_PATH)
        output_base = Path(OUTPUT_PATH)
        output_base.mkdir(exist_ok=True)
        subdirs = {subdir: retrosheet_base / subdir for subdir in RETROSHEET_SUBDIRS}

        print("Writing simple files...")
        concat_files(subdirs["gamelogs"], output_base / "gamelog.csv", glob="gl*.txt", check_dupes=False)
        # TODO: Figure out how to integrate 2020-orig (leave out for now)
        concat_files(subdirs["schedules"], output_base / "schedule.csv", glob="*schedule.csv", strip_header=True)
        concat_files(retrosheet_base, output_base / "park.csv", glob="ballparks.csv", strip_header=True)
        concat_files(retrosheet_base, output_base / "bio.csv", glob="biofile.csv", strip_header=True)
        concat_files(subdirs["rosters"], output_base / "roster.csv", glob="*.ROS", prepend_filename=True)

    @staticmethod
    def parse_event_types(use_parallel=True) -> None:
        def parse_events(output_type: str, clean_func: Callable = None):
            event_base = RETROSHEET_PATH
            output_file = OUTPUT_PATH.joinpath(output_type).with_suffix(".csv")
            command_template = PARSE_FUNCS[output_type]
            f_out_inflated = open(output_file, 'w')
            for folder in EVENT_FOLDERS:
                # Copy (not move) all teamfiles to each subdir
                for teamfile in event_base.glob("teams/TEAM*"):
                    shutil.copy(teamfile, event_base.joinpath(folder))
                data_path = event_base.joinpath(folder)
                years = {re.match("[0-9]{4}", f.stem)[0] for f in data_path.iterdir()
                         if re.match("[0-9]{4}", f.stem)}
                commands = [command_template.format(year=year) for year in years]
                runner = lambda x: subprocess.run(x, cwd=data_path, check=True, shell=True, text=True,
                                                  stdout=f_out_inflated)

                if use_parallel:
                    command = "echo -e '{commands}' | parallel -k --will-cite".format(commands="\n".join(commands))
                    runner(command)
                else:
                    for command in commands:
                        runner(command)

            f_out_inflated.close()
            if clean_func:
                clean_func(output_file)
            compress(output_file, OUTPUT_PATH)

        def drop_boxscore_files() -> None:
            for f in RETROSHEET_PATH.glob("**/*.EB*"):
                f.unlink()

        def find_malformed_comments(file: Path) -> None:
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

        remove_redundant_box_score_files()
        parse_events("daily")
        drop_boxscore_files()
        parse_events("sub")
        parse_events("comment", clean_func=find_malformed_comments)
        parse_events("game")
        parse_events("event")

    def run(self, use_parallel=True):
        self.write_deduced_gamelist()
        self.parse_code_tables()
        self.parse_simple_files()
        self.parse_event_types(use_parallel=use_parallel)


if __name__ == "__main__":
    OUTPUT_PATH.mkdir(exist_ok=True)
    RetrosheetParser().run()
