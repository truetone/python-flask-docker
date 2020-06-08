import markdown
import frontmatter


class Content():
    @classmethod
    def build(cls, path):
        return cls(cls.__load(path))

    @staticmethod
    def __load(path):
        with open(path, "r", encoding="utf-8") as input_file:
            fm = frontmatter.loads(input_file.read())
        return fm

    def __init__(self, frontmatter):
        self.text = frontmatter.content
        self.metadata = frontmatter.metadata
        self.html = self.__get_html()

    def __get_html(self):
        return markdown.markdown(self.text)
