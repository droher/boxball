import json
from typing import Dict, Any
import json
from typing import Dict, Any, List
from abc import ABC, abstractmethod
JsObject = Dict[str, Any]

class MarkdownGenerator(ABC):
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

    @abstractmethod
    def generate_database_markdown(self, database: JsObject):
        """Abstract method to generate markdown for the database."""
        pass

