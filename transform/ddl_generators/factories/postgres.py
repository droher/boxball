from sqlalchemy import MetaData, Table
from sqlalchemy.dialects import postgresql
from sqlalchemy.engine.interfaces import Dialect

from ddl_generators.target_ddl_factory import DdlString, TargetDdlFactory


class PostgresDdlFactory(TargetDdlFactory):

    @property
    def target_name(self) -> str:
        return "postgres"

    @property
    def dialect(self) -> Dialect:
        return postgresql.dialect()

    def _get_csv_dir(self, table: Table) -> str:
        name = table.fullname
        if "." in name:
            return name.split(".")[0]
        else:
            return name.split("_")[0]

    def _get_csv_stem(self, table: Table) -> str:
        name = table.fullname
        if "." in name:
            return "".join(name.split(".")[1:])
        else:
            return "_".join(name.split("_")[1:])

    def make_copy_ddl(self, metadata: MetaData) -> DdlString:
        copy_ddl_template = "COPY {full_table_name}({column_names}) FROM PROGRAM '{cmd}' CSV;"
        cmd_template = "zstd --rm -cd {csv_file}"
        ddl = []
        for table_obj in metadata.tables.values():
            csv_dir = self.data_path_prefix.joinpath(self._get_csv_dir(table_obj))
            column_names = ", ".join((c.name for c in table_obj.columns.values()
                                      if not (c.autoincrement is True)))
            csv_file = csv_dir.joinpath(self._get_csv_stem(table_obj)).with_suffix(".csv.zst")
            cmd = cmd_template.format(csv_file=csv_file)
            copy_ddl = copy_ddl_template.format(full_table_name=table_obj.fullname, cmd=cmd,
                                                column_names=column_names)
            ddl.append(copy_ddl)
        return "\n".join(ddl) + ";\n"
