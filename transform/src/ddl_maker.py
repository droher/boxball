from src import OUTPUT_PATH
from src.ddl_factories import all_factories
from src.schemas import all_metadata


if __name__ == "__main__":
    OUTPUT_PATH.mkdir(exist_ok=True)
    for factory in all_factories:
        factory.build_ddl(*all_metadata)
