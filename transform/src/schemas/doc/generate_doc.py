from generate_json import JsonGenerator
from generate_html import HtmlGenerator
from PyMDGenerator import PyMDGenerator
from GitHubMDGenerator import GitHubMDGenerator
import sys

#Modules to generate schemas for
import sys
import os

# Add the parent directory to the module search path
pathToAppend = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(pathToAppend)

# Import the modules to generate schemas for
import retrosheet
import baseballdatabank

schema_modules = [
    retrosheet, 
    baseballdatabank
]

# Generate the json and write it to a file
schemas = {}
for module in schema_modules:
    schemas[module.__name__] = JsonGenerator.generate_schema_json(module.__name__, module)

database_json = {
    "database_name": "Boxball",
    "schemas": schemas
}



pwd = sys.path[0]

JsonGenerator.write_json_to_file(pwd+'/schemas.json', database_json)
github_markdown = GitHubMDGenerator(database_json).write_markdown_to_file(pwd + "/schemas.md")
python_markdown = PyMDGenerator(database_json).write_markdown_to_file(pwd + "/schemas.py.md")
HtmlGenerator(
        python_markdown,
        HtmlGenerator.load_styles(pwd + "/styles.css")
    ).write_html_to_file(pwd + "/schemas.html")