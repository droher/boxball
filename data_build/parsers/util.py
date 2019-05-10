import logging
from pathlib import Path

import zstd


def compress(file: Path, output_dir: Path) -> None:
    """Replaces the original file with a compressed version"""
    logging.info("Compressing {}".format(file))
    compressed_file = output_dir.joinpath(file.stem).with_suffix(file.suffix + ".zst")
    cctx = zstd.ZstdCompressor()
    with open(file, 'rb') as ifh, open(compressed_file, 'wb') as ofh:
        compression_result = cctx.copy_stream(ifh, ofh)
        print("{} size (uncompressed,compressed): {}".format(file, compression_result))
    return file.unlink()
