from truetone.utils.path_from_file import PathFromFile


def test_slug_from_path_returns_only_slug():
    path = PathFromFile.build("/path/to/file-name.md")
    assert path.slug == "file-name"


def test_slug_from_path_with_under_scores_returns_hyphenated_slug():
    path = PathFromFile.build("/path/to/file_name.md")
    assert path.slug == "file-name"
