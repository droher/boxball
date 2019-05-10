
from pathlib import Path
import humps
from parsers.util import compress

DOS_EOF = chr(26)


BASEBALLDATABANK_PATH = Path("/baseballdatabank/core")
OUTPUT_PATH = Path("/parsed")


def get_baseballdatabank_files():
    for file in BASEBALLDATABANK_PATH.glob("*.csv"):
        # Just need to change from PascalCase to snake_case to match table names
        # Editing OF fielding files to get PascalCasev conformity for all databank filenames
        file_name = file.name.replace("OFs", "OfS").replace("OF", "Of")
        depascalized_file = file.with_name(humps.depascalize(file_name))
        with open(file, 'r') as f_in, open(depascalized_file, 'w') as f_out:
            f_in.readline()
            f_out.write(f_in.read())
        file.unlink()
        compress(depascalized_file, OUTPUT_PATH)


if __name__ == "__main__":
    OUTPUT_PATH.mkdir(exist_ok=True)
    get_baseballdatabank_files()
