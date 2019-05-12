from typing import List
from transform.ddl_generators.factories.target_ddl_factory import TargetDdlFactory
from transform.ddl_generators.factories.postgres import PostgresDdlFactory
from transform.ddl_generators.factories.mysql import MySqlDdlFactory
from transform.ddl_generators.factories.postgres_cstore_fdw import PostgresCstoreFdwDdlFactory
from transform.ddl_generators.factories.sqlite import SqliteDdlFactory

all_factories: List[TargetDdlFactory] = [PostgresDdlFactory(), MySqlDdlFactory(),
                                         PostgresCstoreFdwDdlFactory(), SqliteDdlFactory()]
