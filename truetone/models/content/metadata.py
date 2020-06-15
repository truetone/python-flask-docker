import glob
from truetone.models.content.metadatum import ContentMetadatum


class ContentMetadata:

    @classmethod
    def build(cls, directory):
        return cls(cls.__build_metadata(directory))

    @classmethod
    def __build_metadata(cls, directory):
        return list(map(ContentMetadatum.build,
                    cls.__markdown_files(directory)))

    @staticmethod
    def __markdown_files(directory):
        return sorted(glob.glob(f'{directory}/*.md'))

    @staticmethod
    def __is_blog_entry(entry):
        return entry.is_blog_entry

    def __init__(self, metadata):
        self.metadata = metadata
        self.blog_entries = self.__blog_entries()

    def __blog_entries(self):
        return list(filter(self.__is_blog_entry, self.metadata))
