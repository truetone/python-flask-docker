import frontmatter
from truetone.utils.path_from_file import PathFromFile


class ContentMetadatum:

    @classmethod
    def build(cls, path):
        with open(path, "r", encoding="utf-8") as input_file:
            fm = frontmatter.loads(input_file.read())
        slug = PathFromFile.build(path).slug
        is_blog_entry = cls.__is_blog_entry(fm.metadata)

        return cls(slug, fm.metadata, is_blog_entry)

    @staticmethod
    def __is_blog_entry(metadata):
        return metadata.get('blog_entry', False) is True

    def __init__(self, slug, metadata, is_blog_entry):
        self.slug = slug
        self.metadata = metadata
        self.title = metadata["title"]
        self.is_blog_entry = is_blog_entry
