import frontmatter
from truetone.utils.path_from_file import PathFromFile


class ContentMetadatum:

    @classmethod
    def build(cls, path):
        with open(path, "r", encoding="utf-8") as input_file:
            fm = frontmatter.loads(input_file.read())
        slug = PathFromFile.build(path).slug

        return cls(slug, fm.metadata)

    def __init__(self, slug, metadata):
        self.slug = slug
        self.metadata = metadata
        self.title = metadata["title"]
        self.is_blog_entry = self.__is_blog_entry()

    def __is_blog_entry(self):
        return self.metadata.get('blog_entry', False) is True
