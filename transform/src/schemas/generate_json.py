import inspect
import sys
import retrosheet as retrosheet
import baseballdatabank as baseballdatabank
import json
from generate_markdown import MarkdownGenerator, PyMDGenerator
from generate_html import HtmlGenerator

def is_sqlalchemy_model(obj,base_class):
    """Check if the given object is a SQLAlchemy model."""
    return inspect.isclass(obj) and issubclass(obj, base_class) and obj != base_class

def cleanup_docstring(docstring):
    """Return a cleaned up docstring."""
    if(docstring == None):
        return None

    docstring_pieces = docstring.split("\n")
    if (len(docstring_pieces) == 1):
        return docstring
    
    if (len(docstring_pieces) > 1 and docstring_pieces[0] == ""):
        docstring_pieces = docstring_pieces[1:]
        replacement_docstring = ""
        initial_indent = docstring_pieces[1][0:len(docstring_pieces[1]) - len(docstring_pieces[1].lstrip())]

        for piece in docstring_pieces:
            if piece.startswith(initial_indent):
                replacement_docstring += piece[len(initial_indent):] + "\n"
                continue
            replacement_docstring +=  piece.strip() + "\n"  #strip initial indent, but leave later indents

        if replacement_docstring.endswith("\n"): 
            return replacement_docstring[:-1] #strip final newline
        return replacement_docstring
    
    if len(docstring_pieces) > 1:
        replacement_docstring = ""
        for piece in docstring_pieces:
            replacement_docstring += piece.strip() + " "
        return replacement_docstring.strip()
    return ""

def generate_column_json(column):
    """Generate json for a single column."""
    column_json = {
        "name": column.name,
        "type": str(column.type).lower(),
        "primary_key": column.primary_key,
        "doc": cleanup_docstring(column.doc)
    }
    return column_json

def generate_table_json(model):
    """Generate json for a single table."""
    table_json = {
        "table_name": model.__tablename__,
        "columns": []
    }
    
    # Sort columns so that primary key columns are listed first
    columns = sorted(model.__table__.columns, key=lambda column: not column.primary_key)
    
    for column in columns:
        table_json["columns"].append(generate_column_json(column))
    
    return table_json

def generate_schema_json(schema_name, models_module):
    """Generate json for all tables in the given module."""
    base_class = models_module.Base
    
    schema_cols = []
    for name, obj in inspect.getmembers(models_module):
        if is_sqlalchemy_model(obj,base_class):
            schema_cols.append(generate_table_json(obj))
    
    schema_json = {
        "schema_name": schema_name,
        "tables": schema_cols
    }
    return schema_json

def write_json_to_file(filename, data):
    """Write the given json data to a file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_json_string(data):
    """Return a json string from the given data."""
    return json.dumps(data, indent=4)

# Generate the json and write it to a file
retrosheet_json = generate_schema_json("retrosheet", retrosheet)
baseballdatabank_json = generate_schema_json("baseballdatabank", baseballdatabank)

database_json = {
    "database_name": "Boxball",
    "schemas": {
        "retrosheet": retrosheet_json,
        "baseballdatabank": baseballdatabank_json
    }
}

pwd = sys.path[0]

write_json_to_file(pwd+'/schemas.json', database_json)
github_markdown = MarkdownGenerator(database_json).write_markdown_to_file(pwd + "/schemas.md")
python_markdown = PyMDGenerator(database_json).write_markdown_to_file(pwd + "/schemas.py.md")
HtmlGenerator(python_markdown).write_html_to_file(pwd + "/schemas.html")

