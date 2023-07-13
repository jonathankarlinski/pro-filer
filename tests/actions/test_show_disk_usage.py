import pytest
from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path


@pytest.fixture
def context(tmp_path):
    file1 = tmp_path / "app.py"
    file2 = tmp_path / "__init__.py"
    file1.write_text("This is file 1.")
    file2.write_text("This is file 2." * 10)

    return {
        "all_files": [
            str(file1),
            str(file2),
        ]
    }


def test_show_disk_usage_with_files(context, capsys):
    show_disk_usage(context)
    captured = capsys.readouterr()
    output = captured.out

    teste = _get_printable_file_path(context['all_files'][1])
    teste1 = _get_printable_file_path(context['all_files'][0])
    expected_output = (
        f"'{teste}':        150 (90%)\n"
        f"'{teste1}':        15 (9%)\n"
        "Total size: 165\n"
    )

    assert output == expected_output


def test_show_disk_usage_without_files(context, capsys):
    context["all_files"] = []
    show_disk_usage(context)
    captured = capsys.readouterr()
    output = captured.out.strip().split("\n")

    assert output[0] == "Total size: 0"
