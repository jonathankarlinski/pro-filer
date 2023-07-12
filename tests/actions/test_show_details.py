from pro_filer.actions.main_actions import show_details  # NOQA
import unittest.mock as mock
from datetime import datetime


def test_show_details_existing_file_with_extension(capsys):
    context = {"base_path": "/path/to/existing_file.txt"}

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == "File 'existing_file.txt' does not exist\n"


def test_show_details_existing_file_without_extension(capsys):
    context = {"base_path": "/path/to/existing_file"}
    expected_output = """File name: existing_file
File size in bytes: 9876
File type: file
File extension: [no extension]
Last modified date: 2023-06-13\n"""

    with mock.patch(
        "pro_filer.actions.main_actions.os.path.exists", return_value=True
    ), mock.patch(
        "pro_filer.actions.main_actions.os.path.getsize", return_value=9876
    ), mock.patch(
        "pro_filer.actions.main_actions.os.path.isdir", return_value=False
    ), mock.patch(
        "pro_filer.actions.main_actions.os.path.splitext",
        return_value=("/path/to/existing_file", ""),
    ), mock.patch(
        "pro_filer.actions.main_actions.os.path.getmtime",
        return_value=datetime(2023, 6, 13).timestamp(),
    ):
        show_details(context)
        captured_output = capsys.readouterr().out
        assert captured_output == expected_output


def test_show_details_existing_directory(capsys):
    context = {"base_path": "/path/to/existing_directory"}
    expected_output = """File name: existing_directory
File size in bytes: 0
File type: directory
File extension: [no extension]
Last modified date: 2023-06-13\n"""

    with mock.patch(
        "pro_filer.actions.main_actions.os.path.exists", return_value=True
    ), mock.patch(
        "pro_filer.actions.main_actions.os.path.getsize", return_value=0
    ), mock.patch(
        "pro_filer.actions.main_actions.os.path.isdir", return_value=True
    ), mock.patch(
        "pro_filer.actions.main_actions.os.path.splitext",
        return_value=("/path/to/existing_directory", ""),
    ), mock.patch(
        "pro_filer.actions.main_actions.os.path.getmtime",
        return_value=datetime(2023, 6, 13).timestamp(),
    ):
        show_details(context)
        captured_output = capsys.readouterr().out
        assert captured_output == expected_output
