import os
from truetone.models import content_metadatum


def test_contains_a_slug_matching_the_file_name():
    cwd = os.path.dirname(os.path.realpath(__file__))
    metadata = content_metadatum.ContentMetadatum.build(
            f'{cwd}/fixtures/content/path-1.md')
    assert metadata.slug == 'path-1'
    assert metadata.title == 'Heading 1'
