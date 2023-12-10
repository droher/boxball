import markdown
import pymdownx

class HtmlGenerator:
    def __init__(self, markdown_string:str):
        self._markdown_string = markdown_string

    extensions = ['pymdownx.details']
    
    extension_configs = {
    }

    css_classes = """
    .tablestyle {
        font-size: 18px;
        font-weight: bold;
        padding-left: 20px;
    }

    .columnstyle {
        font-size: 14px;
        font-weight: bold;
        padding-left: 40px;
    }

    .keycolumnstyle {
        font-size: 14px;
        font-weight: bold;
        color: rgb(89, 0, 0);
        padding-left: 30px;
    }

    .schemastyle {
        font-size: 24px;
        font-weight: bold;
        padding-left: 10px;
    }

    .databasestyle {
        font-size: 36px;
        font-weight: bold;
    }
    """

    def _markdown_to_html(self):
        """Return an html string from the given markdown string."""
        html =  markdown.markdown(
            self._markdown_string, 
            extensions=HtmlGenerator.extensions,
            extension_configs=HtmlGenerator.extension_configs
            )
        return  f"<style>{HtmlGenerator.css_classes}</style>\n{html}"
    
    def write_html_to_file(self, filename:str):
        """Write the given html string to a file."""
        html_string = self._markdown_to_html()
        with open(filename, 'w') as f:
            f.write(html_string)
        return html_string