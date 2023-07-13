from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import os
import pytest


@pytest.fixture
def create_temp_files(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file3 = tmp_path / "file3.txt"

    file1.write_text("Content 1")
    file2.write_text("Content 2")
    file3.write_text("Content 1")

    return str(tmp_path)


def test_find_duplicate_files_no_duplicates(create_temp_files):
    context = {
        "all_files": [
            os.path.join(create_temp_files, "file1.txt"),
            os.path.join(create_temp_files, "file2.txt"),
            os.path.join(create_temp_files, "file3.txt")
        ]
    }

    duplicates = find_duplicate_files(context)
    expected_duplicates = [
        (
            os.path.join(create_temp_files, "file1.txt"),
            os.path.join(create_temp_files, "file3.txt")
        )
    ]
    assert duplicates == expected_duplicates


def test_find_duplicate_files_with_duplicates(create_temp_files):
    context = {
        "all_files": [
            os.path.join(create_temp_files, "file1.txt"),
            os.path.join(create_temp_files, "file2.txt"),
            os.path.join(create_temp_files, "file3.txt"),
        ]
    }

    duplicates = find_duplicate_files(context)
    expected_duplicates = [
        (
            os.path.join(create_temp_files, "file1.txt"),
            os.path.join(create_temp_files, "file3.txt"),
        )
    ]
    assert duplicates == expected_duplicates


def test_find_duplicate_files_missing_file():
    context = {"all_files": ["file1.txt", "file2.txt", "file3.txt"]}

    with pytest.raises(ValueError):
        find_duplicate_files(context)
