import os
from truetone.models import content


def test_retrieves_text_from_file_matching_a_path():
    cwd = os.path.dirname(os.path.realpath(__file__))
    path = f'{cwd}/fixtures/content/path-1.md'
    markdown = content.Content.build(path)
    assert markdown.text == "# Heading 1"


def test_renders_html_from_file_matching_a_path():
    cwd = os.path.dirname(os.path.realpath(__file__))
    path = f'{cwd}/fixtures/content/path-1.md'
    markdown = content.Content.build(path)
    assert markdown.html == "<h1>Heading 1</h1>"


def test_loads_frontmatter_from_file_matching_a_path():
    cwd = os.path.dirname(os.path.realpath(__file__))
    path = f'{cwd}/fixtures/content/path-1.md'
    markdown = content.Content.build(path)
    assert markdown.metadata["title"] == "Heading 1"
