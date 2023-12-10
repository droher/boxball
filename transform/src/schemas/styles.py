class Stlyes:
    def load(self, path):
        styles = None
        with open(path, 'r') as f:
            styles = f.read()
        return styles
        