from generate_markdown import MarkdownGenerator,JsObject

class GitHubMDGenerator(MarkdownGenerator):
    """Generate markdown for the Boxball schema."""
    def __init__(self, database: JsObject):
        """Initialize the MarkdownGenerator with the given schema json."""
        super().__init__(database)
    
    def _column_title_string(self, column: JsObject) -> str:
        """Return a string for the given column title."""
        titleString=""
        if column["primary_key"]:
            titleString+="&#128273; "
        titleString+=f'**{column["name"]}**'
        titleString+=f' : ({column["type"]})'
        return titleString

    def generate_column_markdown(self, indent: int, column: JsObject):
        """Generate markdown for a single column."""
        self.add_line(indent, f'<detail>')
        self.add_line(indent, f'  <summary>{self._column_title_string(column)}</summary>\n')
        self.add_line(indent, f'  {column["doc"]}')
        self.add_line(indent, f'</detail>')
    
    
    def generate_table_markdown(self, indent: int, table: JsObject):
        """Generate markdown for a single table."""
        self.add_line(indent, f'### {table["table_name"]}')
        for column in table["columns"]:
            self.generate_column_markdown(indent+2,column)

    def generate_schema_markdown(self, indent: int, schema: JsObject):
        """Generate markdown for all tables in the given schema."""
        self.add_line(indent, f'## {schema["schema_name"]}')
        for table in schema["tables"]:
            self.generate_table_markdown(indent+2, table)

    def generate_database_markdown(self, database: JsObject):
        """Generate markdown for all schemas in the given database."""
        self.add_line(0, f'# {database["database_name"]}')
        for schema in database["schemas"].values():
            self.generate_schema_markdown(1, schema)
