import os
from truetone.models.content.metadatum import ContentMetadatum


def test_contains_a_slug_matching_the_file_name():
    cwd = os.path.dirname(os.path.realpath(__file__))
    metadatum_instance = ContentMetadatum.build(
            f'{cwd}/fixtures/content/path-1.md')
    assert metadatum_instance.slug == 'path-1'
    assert metadatum_instance.title == 'Heading 1'
