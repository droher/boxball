from sqlalchemy.schema import MetaData
from sqlalchemy_fdw import ForeignTable


def create_fdw_metadata(existing_metadata: MetaData, **kwargs) -> MetaData:
    metadata = MetaData()
    for table in existing_metadata.tables.values():
        ForeignTable(table.name, metadata, *[c.copy() for c in table.columns.values()], **kwargs)
    return metadata
