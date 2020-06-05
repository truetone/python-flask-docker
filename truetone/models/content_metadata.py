import glob
from truetone.models import content_metadatum


class ContentMetadata:

    @classmethod
    def build(cls, directory):
        return cls(cls.__build_metadata(directory))

    @classmethod
    def __build_metadata(cls, directory):
        return list(map(content_metadatum.ContentMetadatum.build,
                    cls.__markdown_files(directory)))

    @staticmethod
    def __markdown_files(directory):
        return sorted(glob.glob(f'{directory}/*.md'))

    def __init__(self, metadata):
        self.metadata = metadata
