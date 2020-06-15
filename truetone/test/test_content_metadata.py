import os
from truetone.models.content.metadata import ContentMetadata


def test_returns_usable_routes_when_given_a_directory_of_markdown_files():
    cwd = os.path.dirname(os.path.realpath(__file__))
    metadata = ContentMetadata.build(
            f'{cwd}/fixtures/content')
    assert type(metadata.metadata) is list
    assert len(metadata.metadata) == 2
    assert metadata.metadata[0].slug == 'path-1'
    assert metadata.metadata[1].slug == 'path-2'


def test_returns_metadata_when_given_a_directory_of_markdown_files():
    cwd = os.path.dirname(os.path.realpath(__file__))
    metadata = ContentMetadata.build(
            f'{cwd}/fixtures/content')
    assert metadata.metadata[0].title == 'Heading 1'


def test_does_not_return_routes_when_frontmatter_has_blog_entry_false():
    cwd = os.path.dirname(os.path.realpath(__file__))
    metadata = ContentMetadata.build(
            f'{cwd}/fixtures/content/entries')
    assert len(metadata.blog_entries) == 1
    assert metadata.blog_entries[0].is_blog_entry is True
