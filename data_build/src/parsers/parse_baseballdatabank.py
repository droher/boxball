
from pathlib import Path
import humps
from src.parsers.util import compress

DOS_EOF = chr(26)


BASEBALLDATABANK_PATH = Path("/baseballdatabank/core")
OUTPUT_PATH = Path("/parsed")


def get_baseballdatabank_files():
    for file in BASEBALLDATABANK_PATH.glob("*.csv"):
        # Just need to change from PascalCase to snake_case to match table names
        # Editing OF to Of to get PascalCasev conformity for all databank filenames
        file_name = file.name.replace("OF", "Of")
        depascalized_file = file.with_name(humps.depascalize(file_name))
        file.rename(depascalized_file)
        compress(file, OUTPUT_PATH)


if __name__ == "__main__":
    OUTPUT_PATH.mkdir(exist_ok=True)
    get_baseballdatabank_files()
