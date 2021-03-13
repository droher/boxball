from pathlib import Path
from typing import Dict, Type, Iterator, List, Tuple

import pyarrow as pa
from pyarrow import csv as pcsv
from pyarrow import parquet as pq
from sqlalchemy import MetaData as AlchemyMetadata, Table as AlchemyTable
from sqlalchemy import Integer, SmallInteger, Float, String, CHAR, Text, Boolean, Date, DateTime
from sqlalchemy.sql.type_api import TypeEngine

from src.schemas import all_metadata
from src import EXTRACT_PATH_PREFIX, TRANSFORM_PATH_PREFIX

PARQUET_PREFIX = TRANSFORM_PATH_PREFIX.joinpath("parquet")
CSV_PREFIX = TRANSFORM_PATH_PREFIX.joinpath("csv")
# How many bytes in each CSV chunk to bring into memory.
# Larger sizes result in better compression and slightly faster time,
# but don't want to risk OOM issues on small build boxes.
BUFFER_SIZE_BYTES = 1000000000

sql_type_lookup: Dict[Type[TypeEngine], str] = {
    Integer: 'int32',
    SmallInteger: 'int16',
    Float: 'float64',
    String: 'str',
    CHAR: 'str',
    Text: 'str',
    Boolean: 'bool',
    # Some Parquet targets can't handle Parquet dates, so we need to parse and pass timestamps
    Date: 'timestamp[ms]',
    DateTime: 'timestamp[ms]'
}


def get_fields(table: AlchemyTable) -> List[Tuple[str, str]]:
    cols = [(c.name, c.type) for c in table.columns.values() if c.autoincrement is not True]
    return [(name, sql_type_lookup[type(dtype)]) for name, dtype in cols]


def write_files(metadata: AlchemyMetadata) -> None:
    """
    Creates a Parquet file for each table in the schema.
    """
    tables: Iterator[AlchemyTable] = metadata.tables.values()
    for table in tables:
        name = table.name
        print(name)

        def get_path(prefix: Path, suffix: str):
            parent_dir = prefix.joinpath(metadata.schema)
            parent_dir.mkdir(exist_ok=True, parents=True)
            return parent_dir.joinpath(name).with_suffix(suffix)

        extract_file = get_path(EXTRACT_PATH_PREFIX, ".csv.zst")
        parquet_file = get_path(PARQUET_PREFIX, ".parquet")

        arrow_schema = pa.schema(get_fields(table))
        column_names = [name for name, dtype in get_fields(table)]

        read_options = pcsv.ReadOptions(column_names=column_names, block_size=1000000000)
        parse_options = pcsv.ParseOptions(newlines_in_values=True)
        convert_options = pcsv.ConvertOptions(column_types=arrow_schema, timestamp_parsers=["%Y%m%d", "%Y-%m-%d"],
                                              true_values=["1", "T"], false_values=["0", "F"], strings_can_be_null=True)

        parquet_writer = pq.ParquetWriter(parquet_file, schema=arrow_schema, compression='zstd',
                                          version="2.0", use_dictionary=True)
        stream_reader = pcsv.open_csv(extract_file, read_options=read_options, parse_options=parse_options,
                                      convert_options=convert_options)
        for batch in stream_reader:
            table = pa.Table.from_batches([batch])
            parquet_writer.write_table(table)
        parquet_writer.close()


if __name__ == "__main__":
    for m in all_metadata:
        write_files(m)
