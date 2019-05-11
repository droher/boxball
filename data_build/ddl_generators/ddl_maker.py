from ddl_generators import OUTPUT_PATH
from ddl_generators.factories import all_factories
from ddl_generators.schemas import all_metadata


if __name__ == "__main__":
    OUTPUT_PATH.mkdir(exist_ok=True)
    for factory in all_factories:
        factory.build_ddl(*all_metadata)
