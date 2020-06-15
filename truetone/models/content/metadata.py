import glob
from truetone.models.content.metadatum import ContentMetadatum


class ContentMetadata:

    @classmethod
    def build(cls, directory):
        metadata = cls.__build_metadata(directory)
        blog_entries = cls.__blog_entries(metadata)
        return cls(metadata, blog_entries)

    @classmethod
    def __build_metadata(cls, directory):
        return list(map(ContentMetadatum.build,
                    cls.__markdown_files(directory)))

    @classmethod
    def __blog_entries(cls, metadata):
        return list(filter(cls.__is_blog_entry, metadata))

    @staticmethod
    def __markdown_files(directory):
        return sorted(glob.glob(f'{directory}/*.md'))

    @staticmethod
    def __is_blog_entry(entry):
        return entry.is_blog_entry

    def __init__(self, metadata, blog_entries):
        self.metadata = metadata
        self.blog_entries = blog_entries
