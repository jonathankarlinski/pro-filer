from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_empty_context(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"


def test_show_preview_files_and_dirs(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }
    show_preview(context)
    captured = capsys.readouterr()
    teste = (
      "['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\n"
    )
    expected_output = (
        "Found 3 files and 2 directories\n"
        f"First 5 files: {teste}"
        "First 5 directories: ['src', 'src/utils']\n"
    )
    assert captured.out == expected_output


def test_show_preview_large_lists(capsys):
    context = {
        "all_files": [
            "file1.txt",
            "file2.txt",
            "file3.txt",
            "file4.txt",
            "file5.txt",
            "file6.txt",
        ],
        "all_dirs": ["dir1", "dir2", "dir3", "dir4", "dir5", "dir6"],
    }
    show_preview(context)
    captured = capsys.readouterr()
    teste = (
        "['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']\n"
    )

    expected_output = (
        "Found 6 files and 6 directories\n"
        f"First 5 files: {teste}"
        "First 5 directories: ['dir1', 'dir2', 'dir3', 'dir4', 'dir5']\n"
    )

    assert captured.out == expected_output
