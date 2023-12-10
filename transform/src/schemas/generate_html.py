import markdown
import pymdownx
from pymdownx import superfences

class HtmlGenerator:
    def __init__(self, markdown_string:str, css_classes:str):
        self._markdown_string = markdown_string
        self._css_classes = css_classes

    extensions = ['pymdownx.details','extra','pymdownx.superfences','toc']
    
    superfences_configs = {
        'custom_fences': [
            {
                'name': 'codeblock',
                'class': 'codeblock',
                'format': superfences.fence_code_format
            }
        ]
    }

    extension_configs = {
        'pymdownx.superfences': superfences_configs,
    }

    def _markdown_to_html(self):
        """Return an html string from the given markdown string."""
        html =  markdown.markdown(
            self._markdown_string, 
            extensions=HtmlGenerator.extensions,
            extension_configs=HtmlGenerator.extension_configs
            )
        return  f"<body><style>{self._css_classes}</style>\n{html}</body>"
    
    def write_html_to_file(self, filename:str):
        """Write the given html string to a file."""
        html_string = self._markdown_to_html()
        with open(filename, 'w') as f:
            f.write(html_string)
        return html_string