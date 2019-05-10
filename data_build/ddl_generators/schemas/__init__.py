from typing import List
from sqlalchemy import MetaData
from ddl_generators.schemas.baseballdatabank import metadata as baseballdatabank_metadata
from ddl_generators.schemas.retrosheet import metadata as retrosheet_metadata

all_metadata: List[MetaData] = [baseballdatabank_metadata, retrosheet_metadata]
