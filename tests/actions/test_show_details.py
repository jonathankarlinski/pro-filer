from pro_filer.actions.main_actions import show_details  # NOQA
import os
from datetime import datetime


def test_show_details_existing_file_with_extension(capsys):
    context = {"base_path": "/path/to/existing_file.txt"}
    expected_output = """File name: existing_file.txt
File size in bytes: 12345
File type: file
File extension: .txt
Last modified date: 2023-06-13\n"""

    os.path.exists = lambda path: True
    os.path.getsize = lambda path: 12345
    os.path.isdir = lambda path: False
    os.path.splitext = lambda path: ("/path/to/existing_file", ".txt")
    os.path.getmtime = lambda path: datetime(2023, 6, 13).timestamp()

    show_details(context)
    captured_output = capsys.readouterr().out
    assert captured_output == expected_output


def test_show_details_existing_file_without_extension(capsys):
    context = {"base_path": "/path/to/existing_file"}
    expected_output = """File name: existing_file
File size in bytes: 9876
File type: file
File extension: [no extension]
Last modified date: 2023-06-13\n"""

    os.path.exists = lambda path: True
    os.path.getsize = lambda path: 9876
    os.path.isdir = lambda path: False
    os.path.splitext = lambda path: ("/path/to/existing_file", "")
    os.path.getmtime = lambda path: datetime(2023, 6, 13).timestamp()

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

    os.path.exists = lambda path: True
    os.path.getsize = lambda path: 0
    os.path.isdir = lambda path: True
    os.path.splitext = lambda path: ("/path/to/existing_directory", "")
    os.path.getmtime = lambda path: datetime(2023, 6, 13).timestamp()

    show_details(context)
    captured_output = capsys.readouterr().out
    assert captured_output == expected_output
