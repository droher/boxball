from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Type, Iterator, List, Tuple

import pandas as pd
import pyarrow as pa
from pandas.io.parsers import TextFileReader
from pyarrow import parquet as pq
from sqlalchemy import MetaData as AlchemyMetadata, Table as AlchemyTable
from sqlalchemy import Integer, SmallInteger, Float, String, CHAR, Text, Boolean, Date, DateTime
from sqlalchemy.sql.type_api import TypeEngine

from src.schemas import all_metadata
from src import EXTRACT_PATH_PREFIX, TRANSFORM_PATH_PREFIX

PARQUET_PREFIX = TRANSFORM_PATH_PREFIX.joinpath("parquet")
CSV_PREFIX = TRANSFORM_PATH_PREFIX.joinpath("csv")
# How many rows in each CSV chunk to bring into memory.
# Larger sizes result in better compression and slightly faster time,
# but don't want to risk OOM issues on small build boxes.
# 300K keeps us around 1GB peak execution memory
BUFFER_SIZE_ROWS = 300000


@dataclass
class Types:
    """
    Quick way to handle that Pandas and Arrow have different types sometimes.
    Also an excuse to write my first dataclass.
    """
    pandas_type: str
    arrow_type: str = None

    @property
    def pd(self) -> str:
        return self.pandas_type

    @property
    def pa(self) -> str:
        return self.arrow_type or self.pandas_type


sql_type_lookup: Dict[Type[TypeEngine], Types] = {
    # Pandas doesn't accept null integers, so we have to treat them as floats. Fortunately Arrow has no issue
    # with either null ints or casting Pandas floats to ints.
    Integer: Types('float32', 'int32'),
    SmallInteger: Types('float32', 'int16'),
    Float: Types('float64'),
    String: Types('str'),
    CHAR: Types('str'),
    Text: Types('str'),
    Boolean: Types('bool'),
    # Arrow needs us to take in dates as strings that have gone through Pandas' magic `parse_dates` param
    Date: Types('str', 'date32'),
    DateTime: Types('str', 'date64')
}


def get_fields(table: AlchemyTable) -> List[Tuple[str, Types]]:
    cols = [(c.name, c.type) for c in table.columns.values() if c.autoincrement is not True]
    return [(name, sql_type_lookup[type(dtype)]) for name, dtype in cols]


def get_pandas_fields(table: AlchemyTable) -> List[Tuple[str, str]]:
    return [(name, dtype.pd) for name, dtype in get_fields(table)]


def get_arrow_fields(table: AlchemyTable) -> List[Tuple[str, str]]:
    return [(name, dtype.pa) for name, dtype in get_fields(table)]


def map_to_bytes(*strs: str) -> List[bytes]:
    """
    Helper for weird read_csv parameter that makes you encode the string in bytes first
    """
    return [bytes(s, encoding="utf-8") for s in strs]


def chunked_write(df_iterator: TextFileReader, parquet_writer: pq.ParquetWriter):
    rows_processed = 0
    for df in df_iterator:
        rows_processed += min(BUFFER_SIZE_ROWS, len(df))
        pa_table = pa.Table.from_pandas(df=df, schema=parquet_writer.schema)
        parquet_writer.write_table(pa_table)

        print("Rows processed: {}".format(rows_processed), end="\r", flush=True)
    print()
    parquet_writer.close()


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

        pandas_fields = get_pandas_fields(table)
        arrow_fields = get_arrow_fields(table)
        arrow_schema = pa.schema(get_arrow_fields(table))
        column_names = [name for name, dtype in pandas_fields]
        date_cols = [name for name, dtype in arrow_fields if "date" in dtype]

        # Using both Arrow and Pandas allows each library to cover the other's current shortcomings.
        # Pandas's read_csv can handle chunked/complex reads, while Arrow's WriteParquet can handle chunked writes.
        # Arrow's input streams are capable of handling zstd files, which Pandas hasn't implemented yet.
        in_buf = pa.OSFile(str(extract_file), mode="r")
        reader = pa.CompressedInputStream(in_buf, compression="zstd")

        parquet_writer = pq.ParquetWriter(parquet_file, schema=arrow_schema, compression='zstd',
                                          version="2.0", use_dictionary=True)
        df_iterator: TextFileReader = pd.read_csv(reader, header=None, names=column_names, dtype=dict(pandas_fields),
                                                  true_values=map_to_bytes('T'), false_values=map_to_bytes('F'),
                                                  chunksize=BUFFER_SIZE_ROWS, parse_dates=date_cols)

        chunked_write(df_iterator, parquet_writer)


if __name__ == "__main__":
    for m in all_metadata:
        write_files(m)
