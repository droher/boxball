import csv
from collections.abc import Callable
from pathlib import Path
from typing import IO

import humps

from parsers._logging import get_logger
from parsers.util import compress, OUTPUT_PATH, resolve_path

logger = get_logger(__name__)

DOS_EOF = chr(26)
BASEBALLDATABANK_PATHS = (
    resolve_path("BOXBALL_BASEBALLDATABANK_CORE_PATH", "baseballdatabank/core"),
    resolve_path("BOXBALL_BASEBALLDATABANK_CONTRIB_PATH", "baseballdatabank/contrib"),
)

# Per-table row-level fixups applied after the header strip. Keyed by the
# depascalized table name. The callable rewrites a single CSV row in-place.
RowFixup = Callable[[list[str]], list[str]]


def _strip_multi_position_starting_pos(row: list[str]) -> list[str]:
    """Lahman v2025 AllstarFull.csv encodes Negro Leagues multi-position starts
    as ``9;9``-style values in column 7 (``startingPos``). The schema keeps
    ``starting_pos`` as a SmallInteger for query compatibility, so collapse
    the value to the first integer. Affects ~65 rows (1947-vintage NLB
    all-star records); the second-position datapoint is dropped intentionally
    pending a follow-up that adds proper multi-position support.
    """
    starting_pos_idx = 7
    if len(row) > starting_pos_idx and ";" in row[starting_pos_idx]:
        original = row[starting_pos_idx]
        row[starting_pos_idx] = original.split(";", 1)[0]
        logger.debug("Collapsed multi-position starting_pos %r → %r", original, row[starting_pos_idx])
    return row


ROW_FIXUPS: dict[str, RowFixup] = {
    "allstar_full": _strip_multi_position_starting_pos,
}


def _copy_with_fixup(f_in: IO[str], f_out: IO[str], fixup: RowFixup) -> None:
    reader = csv.reader(f_in)
    # csv.writer defaults to '\r\n' line terminator (RFC 4180). Postgres COPY
    # accepts CRLF transparently; MySQL LOAD DATA with LINES TERMINATED BY
    # '\n' leaves a stray \r in the trailing field, breaking the integer
    # NULL guard for empty trailing columns. Force LF to match the
    # passthrough path (text-mode write of a universally-newlined string).
    writer = csv.writer(f_out, lineterminator="\n")
    for row in reader:
        writer.writerow(fixup(row))


def get_baseballdatabank_files():
    files = [f for path in BASEBALLDATABANK_PATHS
             for f in path.glob("*.csv")]
    logger.info("Processing %d Baseball Databank files", len(files))
    logger.debug("Baseball Databank files: %s", files)
    for file in files:
        # Just need to change from PascalCase to snake_case to match table names
        # Editing OF fielding files to get PascalCasev conformity for all databank filenames
        file_name = file.name.replace("OFs", "OfS").replace("OF", "Of")
        depascalized_name = humps.depascalize(file_name)
        depascalized_file = OUTPUT_PATH.with_name(depascalized_name)
        table_name = Path(depascalized_name).stem
        fixup = ROW_FIXUPS.get(table_name)
        try:
            with open(file, 'r') as f_in, open(depascalized_file, 'w', newline='') as f_out:
                f_in.readline()
                if fixup is None:
                    f_out.write(f_in.read())
                else:
                    _copy_with_fixup(f_in, f_out, fixup)
        except OSError:
            logger.exception("Failed to depascalize %s", file)
            raise
        file.unlink()
        compress(depascalized_file, OUTPUT_PATH)


if __name__ == "__main__":
    OUTPUT_PATH.mkdir(exist_ok=True)
    get_baseballdatabank_files()
