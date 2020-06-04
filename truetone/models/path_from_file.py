import os


class PathFromFile:

    def __init__(self, slug):
        self.slug = slug

    @classmethod
    def build(cls, filename_with_path):
        filename = filename_with_path.split('/')[-1]
        slug = os.path.splitext(filename)[0].replace("_", "-")
        return cls(slug)
