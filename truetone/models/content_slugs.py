import glob
from truetone.models import path_from_file


class ContentSlugs:

    @classmethod
    def build(cls, directory):
        return cls(cls.__paths(directory))

    @classmethod
    def __paths(cls, directory):
        return list(map(path_from_file.PathFromFile.build,
                    cls.__markdown_files(directory)))

    @staticmethod
    def __markdown_files(directory):
        return sorted(glob.glob(f'{directory}/*.md'))

    def __init__(self, slugs):
        self.slugs = slugs
