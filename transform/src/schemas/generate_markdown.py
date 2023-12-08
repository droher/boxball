import inspect
import sys
import retrosheet as retrosheet
import baseballdatabank as baseballdatabank

def is_sqlalchemy_model(obj,base_class):
    """Check if the given object is a SQLAlchemy model."""
    return inspect.isclass(obj) and issubclass(obj, base_class) and obj != base_class

def generate_column_markdown(column):
    """Generate markdown for a single column."""
    column_name = ""
    if column.primary_key:
        column_name = f'  #### &#128273; {column.name}'
        
    else:
        column_name = f'  #### {column.name}'
    column_name += ": " + str(column.type).lower()
    line = ""
    if(column.doc is None):
        line = f'{column_name}'
    else:
        line = f'{column_name}\n   >{column.doc}'
    return line + '\n'

def generate_table_markdown(model):
    """Generate markdown for a single table."""
    markdown_lines = [f'<details>\n <summary> <b>{model.__tablename__}</b></summary>\n\n']
    
    # Sort columns so that primary key columns are listed first
    columns = sorted(model.__table__.columns, key=lambda column: not column.primary_key)
    
    for column in columns:
        markdown_lines.append(generate_column_markdown(column))
    
    table_markdown = ''.join(markdown_lines)
    return table_markdown + '</details><br>\n'



def generate_schema_markdown(models_module):
    """Generate markdown for all tables in the given module."""
    base_class = models_module.Base
    markdown_lines = []
    for name, obj in inspect.getmembers(models_module):
        if is_sqlalchemy_model(obj,base_class):
            markdown_lines.append(generate_table_markdown(obj))
    return ''.join(markdown_lines)

def write_markdown_to_file(filename, markdown):
    """Write the given markdown to a file."""
    with open(filename, 'w') as f:
        f.write(markdown)

# Generate the markdown and write it to a file
retrosheet_markdown = generate_schema_markdown(retrosheet)
baseballdatabank_markdown = generate_schema_markdown(baseballdatabank)

markdown = "# Boxball Schemas\n" + "This document contains the schemas for the boxball database.\n\n" 
markdown += "Columns with a &#128273; next to the name represent the primary keys of the table, and will always be listed first in a given table.\n"
markdown += "## retrosheet\n" + retrosheet_markdown + "\n\n" + "## baseballdatabank\n" + baseballdatabank_markdown

pwd = sys.path[0]
write_markdown_to_file(pwd+'/schemas.md', markdown)