import csv
from pathlib import Path
from sqlalchemy import MetaData, Table
from marshmallow_sqlalchemy import TableSchema
import zstandard as zstd
import io

from ddl_generators.schemas.retrosheet import metadata as retrosheet_metadata

ERROR_FILE_HEADER = ["file", "row_number", "pk", "errors"]


def make_error_file_stub(path: Path) -> None:
    """
    Creates the error validation file and adds a header.
    :param path: Full filename to the error csv.
    """
    with open(str(path), "w") as error_file:
        writer = csv.writer(error_file)
        writer.writerow(ERROR_FILE_HEADER)


def get_validator(table_obj: Table) -> TableSchema:
    """
    Returns a Marshmallow schema given a SQLAlchemy table.
    """
    class Validator(TableSchema):
        class Meta:
            table = table_obj
    return Validator()


def validate_csvs_against_metadata(metadata: MetaData, csv_dir: Path) -> None:
    """
    Given a SQLAlchemy MetaData object containing models, and a folder containing
    gzipped csvs that match the table names of the models, validates all rows of all
    files, and outputs errors to a logfile.
    """
    error_filepath: Path = csv_dir.with_name("_validation_errors").with_suffix(".csv")
    make_error_file_stub(error_filepath)

    for table_name, table_obj in metadata.tables.items():
        print(table_name)
        columns = [c.name for c in table_obj.columns]
        validator = get_validator(table_obj)
        data_filepath = csv_dir.joinpath(table_name).with_suffix(".csv.zstd")
        with open(data_filepath, 'rb') as data_file, open(str(error_filepath), "a") as error_file:
            dctx = zstd.ZstdDecompressor()
            stream_reader = dctx.stream_reader(data_file)
            text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
            reader = csv.DictReader(text_stream, fieldnames=columns, dialect=csv.unix_dialect)
            writer = csv.writer(error_file, dialect=csv.unix_dialect)
            for i, row in enumerate(reader):
                results = validator.validate(row)
                if results:
                    pk = {c.name: results.get(c.name, "MISSING PK") for c in table_obj.primary_key}
                    error_row = [table_name, i, pk, results]
                    writer.writerow(error_row)
                    print(row)
                    break


validate_csvs_against_metadata(retrosheet_metadata, Path.cwd())
