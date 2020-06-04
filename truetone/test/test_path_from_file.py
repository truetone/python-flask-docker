import pytest
from truetone.models import path_from_file


def test_slug():
    path = path_from_file.PathFromFile("file-name.md")
    assert path.path == "file-name"
