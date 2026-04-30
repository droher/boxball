from typing import List
from src.target_ddl_factory import TargetDdlFactory
from src.ddl_factories.postgres import PostgresDdlFactory
from src.ddl_factories.mysql import MySqlDdlFactory
from src.ddl_factories.postgres_columnar import PostgresColumnarDdlFactory
from src.ddl_factories.sqlite import SqliteDdlFactory
from src.ddl_factories.clickhouse import ClickhouseDdlFactory

all_factories: List[TargetDdlFactory] = [PostgresDdlFactory(), MySqlDdlFactory(),
                                         PostgresColumnarDdlFactory(), SqliteDdlFactory(), ClickhouseDdlFactory()]
