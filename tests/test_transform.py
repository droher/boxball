from src import OUTPUT_PATH
from src.boxball_schemas import retrosheet_metadata, baseballdatabank_metadata, all_metadata
from src.ddl_factories import all_factories
from src.ddl_factories.postgres_columnar import PostgresColumnarDdlFactory
from src.parquet import write_files, PARQUET_PREFIX


class TestSchemas:
    def test_schemas_compile(self):
        assert retrosheet_metadata.tables
        assert baseballdatabank_metadata.tables
        assert "retrosheet.event" in retrosheet_metadata.tables
        assert "baseballdatabank.teams" in baseballdatabank_metadata.tables


class TestDdlFactory:
    def test_ddl_compiles(self):
        for factory in all_factories:
            for metadata in all_metadata:
                transformed_metadata = factory.metadata_transform(metadata)
                assert isinstance(factory.make_create_ddl(transformed_metadata), str)
                assert isinstance(factory.make_copy_ddl(transformed_metadata), str)

    def test_ddl_writes(self):
        OUTPUT_PATH.mkdir(exist_ok=True)
        for factory in all_factories:
            factory.build_ddl(*all_metadata)
            assert OUTPUT_PATH.joinpath("{}.{}".format(factory.target_name, factory.file_format)).exists()

    def test_columnar_ddl_uses_citus_columnar(self):
        factory = PostgresColumnarDdlFactory()
        assert any(isinstance(f, PostgresColumnarDdlFactory) for f in all_factories), \
            "PostgresColumnarDdlFactory must be registered in all_factories"
        for metadata in all_metadata:
            transformed = factory.metadata_transform(metadata)
            create_ddl = factory.make_create_ddl(transformed)
            assert create_ddl.count("CREATE EXTENSION IF NOT EXISTS citus") == 1, \
                "Each emitted columnar metadata block must declare the citus extension exactly once"
            n_tables = len(transformed.tables)
            assert create_ddl.count(" USING columnar") == n_tables, \
                f"Expected {n_tables} USING columnar clauses, got {create_ddl.count(' USING columnar')}"
            ext_idx = create_ddl.index("CREATE EXTENSION IF NOT EXISTS citus")
            first_table_idx = create_ddl.index("CREATE TABLE")
            assert ext_idx < first_table_idx, \
                "CREATE EXTENSION citus must precede the first CREATE TABLE"


class TestParquet:
    def test_parquet_writes(self):
        for m in all_metadata:
            write_files(m)
            for table in m.tables.values():
                table_name = table.name
                assert PARQUET_PREFIX.joinpath(m.schema, table_name).with_suffix(".parquet").exists()
