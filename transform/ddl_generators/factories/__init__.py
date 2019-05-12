from typing import List
from ddl_generators.target_ddl_factory import TargetDdlFactory
from ddl_generators.factories.postgres import PostgresDdlFactory
from ddl_generators.factories.mysql import MySqlDdlFactory
from ddl_generators.factories.postgres_cstore_fdw import PostgresCstoreFdwDdlFactory
from ddl_generators.factories.sqlite import SqliteDdlFactory

all_factories: List[TargetDdlFactory] = [PostgresDdlFactory(), MySqlDdlFactory(),
                                         PostgresCstoreFdwDdlFactory(), SqliteDdlFactory()]
