import inspect
import sys
import retrosheet as retrosheet
import baseballdatabank as baseballdatabank

def is_sqlalchemy_model(obj,base_class):
    """Check if the given object is a SQLAlchemy model."""
    return inspect.isclass(obj) and issubclass(obj, base_class) and obj != base_class

def generate_table_markdown(model):
    """Generate markdown for a single table."""
    markdown_lines = [f'## {model.__tablename__}\n']
    
    # Sort columns so that primary key columns are listed first
    columns = sorted(model.__table__.columns, key=lambda column: not column.primary_key)
    
    for column in columns:
        # Make primary key column names bold
        column_name = f'**{column.name}**' if column.primary_key else column.name
        line = f'### {column_name}\n- Type: {column.type}\n- Description: {column.doc or "No description"}'
        if column.primary_key:
            line += '\n- Primary Key: Yes'
        markdown_lines.append(line + '\n')
    return ''.join(markdown_lines)

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

markdown = "# retrosheet\n" + retrosheet_markdown + "\n\n" + "# baseballdatabank\n" + baseballdatabank_markdown

pwd = sys.path[0]
write_markdown_to_file(pwd+'/schemas.md', markdown)