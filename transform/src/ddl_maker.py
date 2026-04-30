from src import OUTPUT_PATH
from src._logging import get_logger
from src.ddl_factories import all_factories
from src.boxball_schemas import all_metadata

logger = get_logger(__name__)


if __name__ == "__main__":
    OUTPUT_PATH.mkdir(exist_ok=True)
    for factory in all_factories:
        logger.info("Building DDL for target %s", factory.target_name)
        factory.build_ddl(*all_metadata)

