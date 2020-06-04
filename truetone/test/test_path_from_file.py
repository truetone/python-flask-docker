from truetone.models import path_from_file


def test_slug_from_path_returns_only_slug():
    path = path_from_file.PathFromFile.build("/path/to/file-name.md")
    assert path.slug == "file-name"


def test_slug_from_path_with_under_scores_returns_hyphenated_slug():
    path = path_from_file.PathFromFile.build("/path/to/file_name.md")
    assert path.slug == "file-name"
