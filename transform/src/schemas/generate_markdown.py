import json
from typing import Dict, Any
import json
from typing import Dict, Any, List
JsObject = Dict[str, Any]

class MarkdownGenerator(object):
    """Generate markdown for the Boxball schema."""
    def __init__(self, database: JsObject):
        """Initialize the MarkdownGenerator with the given schema json."""
        self._lines = []
        self.generate_database_markdown(database)

    def _indent(self, indent: int) -> str:
        """Return a string of spaces for the given indent level."""
        return '    ' * indent
    
    def add_line(self, indent: int, line: str) -> None:
        """Add a line to the given markdown."""
        self._lines.append(self._indent(indent) + line)
    
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

    def generate_markdown_string(self):
        """Return a markdown string from the given data."""
        return '\n'.join(self._lines)
    
    def write_markdown_to_file(self, filename: str):
            """
            Writes the generated markdown string to a file.

            Args:
                filename (str): The name of the file to write the markdown to.
            """
            retStr = self.generate_markdown_string()
            with open(filename, 'w') as f:
                f.write(retStr)
            return retStr
    
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

        

    def generate_column_markdown(self, indent: int, column: JsObject):
        """Generate markdown for a single column."""       
        style = "columnstyle" if not column["primary_key"] else "keycolumnstyle"
        self.add_line(0, f'??? {style} "{column["name"] + "    (" +column["type"]})"')
        self.add_line(1, "```{.codeblock}")
        self._generate_docstring(column["doc"])
        #self.add_line(indent+1, "")
        self.add_line(1, "```")
        self.add_line(indent, f'\n')
    
    
    def generate_table_markdown(self, indent: int, table: JsObject):
        """Generate markdown for a single table."""
        self.add_line(indent, f'### {table["table_name"]}\n')
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

