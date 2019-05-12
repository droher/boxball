from typing import List
from src.target_ddl_factory import TargetDdlFactory
from src.factories.postgres import PostgresDdlFactory
from src.factories.mysql import MySqlDdlFactory
from src.factories.postgres_cstore_fdw import PostgresCstoreFdwDdlFactory
from src.factories.sqlite import SqliteDdlFactory

all_factories: List[TargetDdlFactory] = [PostgresDdlFactory(), MySqlDdlFactory(),
                                         PostgresCstoreFdwDdlFactory(), SqliteDdlFactory()]
