import markdown


class Content():
    @classmethod
    def build(cls, path):
        return cls(cls.__text(path))

    @staticmethod
    def __text(path):
        with open(path, "r", encoding="utf-8") as input_file:
            text = input_file.read()
        return text

    def __init__(self, text):
        self.text = text
        self.html = self.__get_html()

    def __get_html(self):
        return markdown.markdown(self.text)
