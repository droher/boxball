from generate_markdown import MarkdownGenerator,JsObject

class PyMDGenerator(MarkdownGenerator):
    def __init__(self, database: JsObject):
        super().__init__(database)

    def _generate_docstring(self, docstring: str):
        """Generate markdown for a single column."""
        if (docstring is None):
            self.add_line(1, "No documentation provided.")
            return

        split_doc_string = docstring.split("\n")
        if len(split_doc_string) == 1:
            self.add_line(1, f'{docstring}')
            return
        
        for line in split_doc_string:
            self.add_line(1, f'{line}')

    def generate_code_line_string(self,indent, code_block: str):
        """Generate a code block line for a single line of code."""
        if (code_block is None or code_block == ""):
            self.add_line(indent, "No documentation provided.")
            return
        pieces = code_block.split("\n")
        for line in pieces:
            self.add_line(indent, f'{line}')

    def generate_code_block(self, indent: int, code: str, classOverride: str = ".codeblock"):
        """Generate markdown for a single column."""
        self.add_line(indent, '```{'+classOverride + "}")
        self.generate_code_line_string(indent, code)
        self.add_line(indent, "```")
        self.add_line(indent, f'\n')

    def generate_column_name_text(self, column: JsObject):
        """Generate markdown for a single column."""
        style = "keycolumnstyle" if column["primary_key"] else "columnstyle"
        """
        name_prepend = "\"&#128273; " if column["primary_key"] else "\""
        text_line = f'??? {style} {name_prepend}{column["name"] + "    (" +column["type"]})"'
        """
        name_postpend= "&#128273;" if column["primary_key"] else ""
        text_line = f'??? {style} "{column["name"] + "    (" +column["type"]}) {name_postpend}"'
        
        return text_line
        
    def generate_column_markdown(self, indent: int, column: JsObject):
        """Generate markdown for a single column."""     
        self.add_line(0, self.generate_column_name_text(column))
        self.generate_code_block(1, column["doc"])
    
    def generate_table_markdown(self, indent: int, table: JsObject):
        """Generate markdown for a single table."""
        self.add_line(indent, f'### {table["table_name"]}\n')
        self.generate_code_block(0, table["table_doc"] )
        for column in table["columns"]:
            self.generate_column_markdown(indent+1,column)
        self.add_line(indent, f'\n')

    def generate_schema_markdown(self, indent: int, schema: JsObject):
        """Generate markdown for all tables in the given schema."""
        self.add_line(indent, f'## {schema["schema_name"]}')
        for table in schema["tables"]:
            self.generate_table_markdown(indent, table)
        self.add_line(indent, f'\n')

    def generate_database_markdown(self, database: JsObject):
        """Generate markdown for all schemas in the given database."""
        self.add_line(0, f'# {database["database_name"]} Schemas')
        self.add_line(0, f'[TOC]')

        for schema in database["schemas"].values():
            self.generate_schema_markdown(0, schema)

