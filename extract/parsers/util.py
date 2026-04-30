import logging
import os
from pathlib import Path

import zstandard as zstd


def resolve_path(env_key: str, default_subdir: str) -> Path:
    """
    Returns Path from env var if set; otherwise repo-anchored default.
    Default is computed lazily so containers (which set the env var) never
    rely on resolving a repo root that may not exist at /.
    """
    val = os.environ.get(env_key)
    if val:
        return Path(val)
    return Path(__file__).resolve().parents[2] / default_subdir


OUTPUT_PATH = resolve_path("BOXBALL_PARSED_PATH", "parsed")


def compress(file: Path, output_dir: Path, remove_original=True) -> None:
    """Replaces the original file with a compressed version"""
    logging.info("Compressing {}".format(file))
    compressed_file = output_dir.joinpath(file.stem).with_suffix(file.suffix + ".zst")
    cctx = zstd.ZstdCompressor()
    with open(file, 'rb') as ifh, open(compressed_file, 'wb') as ofh:
        compression_result = cctx.copy_stream(ifh, ofh)
        print("{} size (uncompressed,compressed): {}".format(file, compression_result))
    if remove_original:
        return file.unlink()
