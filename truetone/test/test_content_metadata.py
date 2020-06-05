import os
from truetone.models import content_metadata


def test_returns_usable_routes_when_given_a_directory_of_markdown_files():
    cwd = os.path.dirname(os.path.realpath(__file__))
    metadata = content_metadata.ContentMetadata.build(
            f'{cwd}/fixtures/content')
    assert type(metadata.metadata) is list
    assert len(metadata.metadata) == 2
    assert metadata.metadata[0].slug == 'path-1'
    assert metadata.metadata[1].slug == 'path-2'


def test_returns_metadata_when_given_a_directory_of_markdown_files():
    cwd = os.path.dirname(os.path.realpath(__file__))
    metadata = content_metadata.ContentMetadata.build(
            f'{cwd}/fixtures/content')
    assert metadata.metadata[0].title == 'Heading 1'
