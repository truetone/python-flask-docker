import os
from truetone.models import content_slugs


def test_returns_usable_routes_when_given_a_directory_of_markdown_files():
    cwd = os.path.dirname(os.path.realpath(__file__))
    slugs = content_slugs.ContentSlugs.build(f'{cwd}/fixtures/content')
    assert len(slugs.slugs) == 2
    assert slugs.slugs[0].slug == 'path-1'
    assert slugs.slugs[1].slug == 'path-2'
