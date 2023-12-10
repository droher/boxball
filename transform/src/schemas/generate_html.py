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
        font-size: 36px;
        font-weight: bold;
        padding-left: 20px;
    }

    .columnstyle {
        font-size: 24px;
        font-weight: bold;
        padding-left: 30px;
    }

    .keycolumnstyle {
        font-size: 24px;
        font-weight: bold;
        color: rgb(89, 0, 0);
        padding-left: 30px;
    }

    h1 {
        font-size: 48px;
        font-weight: bold;
        padding-left: 20px;
    }

    h2 {
        font-size: 36px;
        font-weight: bold;
        padding-left: 40px;
    }

    h3 {
        font-size: 24px;
        font-weight: bold;
        padding-left: 60px;
    }

    p { 
        background-color: rgb(200, 200, 200);
        font-size: 18px;
        padding-left: 80px;
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