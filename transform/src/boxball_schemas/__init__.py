from typing import List
from sqlalchemy import MetaData
from .retrosheet import metadata as retrosheet_metadata
from .baseballdatabank import metadata as baseballdatabank_metadata

all_metadata: List[MetaData] = [baseballdatabank_metadata, retrosheet_metadata]
