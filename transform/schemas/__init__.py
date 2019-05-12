from typing import List
from sqlalchemy import MetaData
from schemas.retrosheet import metadata as baseballdatabank_metadata
from schemas.retrosheet import metadata as retrosheet_metadata

all_metadata: List[MetaData] = [baseballdatabank_metadata, retrosheet_metadata]
