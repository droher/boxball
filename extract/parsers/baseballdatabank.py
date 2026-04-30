import humps

from parsers._logging import get_logger
from parsers.util import compress, OUTPUT_PATH, resolve_path

logger = get_logger(__name__)

DOS_EOF = chr(26)
BASEBALLDATABANK_PATHS = (
    resolve_path("BOXBALL_BASEBALLDATABANK_CORE_PATH", "baseballdatabank/core"),
    resolve_path("BOXBALL_BASEBALLDATABANK_CONTRIB_PATH", "baseballdatabank/contrib"),
)


def get_baseballdatabank_files():
    files = [f for path in BASEBALLDATABANK_PATHS
             for f in path.glob("*.csv")]
    logger.info("Processing %d Baseball Databank files", len(files))
    logger.debug("Baseball Databank files: %s", files)
    for file in files:
        # Just need to change from PascalCase to snake_case to match table names
        # Editing OF fielding files to get PascalCasev conformity for all databank filenames
        file_name = file.name.replace("OFs", "OfS").replace("OF", "Of")
        depascalized_file = OUTPUT_PATH.with_name(humps.depascalize(file_name))
        try:
            with open(file, 'r') as f_in, open(depascalized_file, 'w') as f_out:
                f_in.readline()
                f_out.write(f_in.read())
        except OSError:
            logger.exception("Failed to depascalize %s", file)
            raise
        file.unlink()
        compress(depascalized_file, OUTPUT_PATH)


if __name__ == "__main__":
    OUTPUT_PATH.mkdir(exist_ok=True)
    get_baseballdatabank_files()
