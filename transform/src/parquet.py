from dataclasses import dataclass
import io
from typing import Dict, Type, Iterator, List, Tuple, BinaryIO

import pandas as pd
import numpy as np
import pyarrow as pa
import zstandard as zstd
from pyarrow import parquet as pq
from sqlalchemy import MetaData as AlchemyMetadata, Table as AlchemyTable
from sqlalchemy import Integer, SmallInteger, Float, String, CHAR, Text, Boolean, Date, DateTime
from sqlalchemy.sql.type_api import TypeEngine

from src.schemas import all_metadata
from src import DEFAULT_CSV_PATH_PREFIX

BUFFER_SIZE_ROWS = 500000


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
    cols = [(c.name, c.type) for c in table.columns().values() if c.autoincrement is not True]
    return [(c.name, sql_type_lookup[dtype]) for c, dtype in cols]


def get_pandas_fields(table: AlchemyTable) -> List[Tuple[str, str]]:
    return [(name, dtype.pd) for name, dtype in get_fields(table)]


def get_arrow_fields(table: AlchemyTable) -> List[Tuple[str, str]]:
    return [(name, dtype.pa) for name, dtype in get_fields(table)]


def csv_stream(zstd_io: BinaryIO) -> io.TextIOWrapper:
    """

    :param zstd_io:
    :return:
    """
    dctx = zstd.ZstdDecompressor()
    reader = dctx.stream_reader(zstd_io)
    return io.TextIOWrapper(reader)


def map_to_bytes(*strs: str) -> List[bytes]:
    return [bytes(s, encoding="utf-8") for s in strs]


def write_parquet_files(metadata: AlchemyMetadata):
    tables: Iterator[AlchemyTable] = metadata.tables.values()
    for table in tables:
        name = table.name
        print(name)
        files_location = DEFAULT_CSV_PATH_PREFIX.joinpath(metadata.schema, name)
        csv_file = files_location.with_suffix(".csv.zst")
        parquet_file = files_location.with_suffix(".parquet")

        csv_buffer = csv_stream(open(csv_file, 'rb'))

        pandas_fields = get_pandas_fields(table)
        arrow_fields = get_arrow_fields(table)
        arrow_schema = pa.schema(get_arrow_fields(table))
        column_names = [name for name, dtype in pandas_fields]
        # We
        date_cols = [name for name, dtype in arrow_fields if "date" in dtype]

        writer = pq.ParquetWriter(parquet_file, schema=arrow_schema, compression='zstd',
                                  version="2.0", use_dictionary=True)
        df_iterator = pd.read_csv(csv_buffer, header=None, names=column_names, dtype=dict(pandas_fields),
                                  true_values=map_to_bytes('T'), false_values=map_to_bytes('F'),
                                  chunksize=BUFFER_SIZE_ROWS, parse_dates=date_cols)
        rows_processed = 0
        for i, df in enumerate(df_iterator):
            pa_table = pa.Table.from_pandas(df=df, schema=arrow_schema)
            rows_processed += min(BUFFER_SIZE_ROWS, len(df))
            writer.write_table(pa_table)
            print("Rows processed: {}".format(rows_processed), end="\r", flush=True)
        print()
        csv_buffer.close()
        writer.close()


if __name__ == "__main__":
    for m in all_metadata:
        write_parquet_files(m)
