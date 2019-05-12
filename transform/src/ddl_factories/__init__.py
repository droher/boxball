from typing import List
from src.target_ddl_factory import TargetDdlFactory
from src.ddl_factories.postgres import PostgresDdlFactory
from src.ddl_factories.mysql import MySqlDdlFactory
from src.ddl_factories.postgres_cstore_fdw import PostgresCstoreFdwDdlFactory
from src.ddl_factories.sqlite import SqliteDdlFactory

all_factories: List[TargetDdlFactory] = [PostgresDdlFactory(), MySqlDdlFactory(),
                                         PostgresCstoreFdwDdlFactory(), SqliteDdlFactory()]
