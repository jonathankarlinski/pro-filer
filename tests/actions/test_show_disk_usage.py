from pro_filer.actions.main_actions import show_disk_usage  # NOQA
import pytest
from pro_filer.cli_helpers import _get_printable_file_path


@pytest.fixture
def context(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file3 = tmp_path / "file3.txt"
    file1.write_text("Test file 1")
    file2.write_text("Test file 2")
    file3.write_text("Test file 3")

    return {
        "all_files": [str(file1), str(file2), str(file3)],
    }


def test_show_disk_usage_empty(context, capsys):
    context["all_files"] = []
    show_disk_usage(context)
    captured = capsys.readouterr()
    output = captured.out.strip()
    assert output == "Total size: 0"


def test_show_disk_usage_with_files(setup_files, capfd):
    context = {
        "all_files": setup_files,
    }

    show_disk_usage(context)

    captured = capfd.readouterr()
    output = captured.out

    expected_output = (
        f"'{_get_printable_file_path(setup_files[1])}':        150 (90%)\n"
        f"'{_get_printable_file_path(setup_files[0])}':        15 (9%)\n"
        "Total size: 165\n"
    )

    assert output == expected_output
