import os


class PathFromFile:

    def __init__(self, slug):
        self.slug = slug

    @classmethod
    def build(cls, filename_with_path):
        slug = cls.__slug(cls.__filename(filename_with_path))
        return cls(slug)

    @staticmethod
    def __filename(filename_with_path):
        return filename_with_path.split('/')[-1]

    @staticmethod
    def __slug(filename):
        return os.path.splitext(filename)[0].replace("_", "-")
