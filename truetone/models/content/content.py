import markdown
import frontmatter


class Content():
    @classmethod
    def build(cls, path):
        fm = cls.__load(path)
        html = cls.__html(fm.content)
        return cls(fm.content, fm.metadata, html)

    @staticmethod
    def __html(raw_text):
        return markdown.markdown(raw_text)

    @staticmethod
    def __load(path):
        with open(path, "r", encoding="utf-8") as input_file:
            fm = frontmatter.loads(input_file.read())
        return fm

    def __init__(self, raw_text, metadata, html):
        self.text = raw_text
        self.metadata = metadata
        self.html = html
