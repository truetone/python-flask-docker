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

    def __init__(self, metadata):
        self.metadata = metadata