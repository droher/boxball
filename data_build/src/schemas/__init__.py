from typing import List
from sqlalchemy import MetaData
from src.schemas.baseballdatabank import metadata as baseballdatabank_metadata
from src.schemas.retrosheet import metadata as retrosheet_metadata

all_metadata: List[MetaData] = [baseballdatabank_metadata, retrosheet_metadata]
