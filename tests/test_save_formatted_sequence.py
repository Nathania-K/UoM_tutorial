import pytest
from pathlib import Path

from SeqKit2026nk.modules.save_formatted_sequence import save_formatted_sequence

#Test to see that function correctly creates and stores a sequence in the named file.
def test_save_formatted_sequence(tmp_path):
    result = save_formatted_sequence(
        "        1 ACTG ACTG",
    filename="sequence.txt",
    output_dir=tmp_path,
    )

    expected_path = tmp_path / "sequence.txt"

    assert result == expected_path
    assert expected_path.exists()
    assert expected_path.read_text(encoding="utf-8") == (
        "        1 ACTG ACTG\n"
        )

#To check if the function creates a directory and confirms a directory path.
def test_save_formatted_sequence_creates_dir(tmp_path):
    output_directory = tmp_path / "nested" / "outputs"

    result = save_formatted_sequence(
        "ACTG",
        filename="sequence.txt",
        output_dir=output_directory,
    )

    assert result == output_directory / "sequence.txt"
    assert output_directory.is_dir()

#To check if the function creates an directory path even if string is empty.
def test_save_formatted_sequence_returns_none(tmp_path):
    result = save_formatted_sequence(
        "",
        filename="sequence.txt",
        output_dir=tmp_path,
    )

    assert result is None
    assert not (tmp_path / "sequence.txt").exists()


#To check if the function creates an directory path even if string is empty.
def test_save_formatted_sequence_defaults(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    result = save_formatted_sequence(
        "ACTG",
        filename="sequence.txt"
    )

    expected_path = tmp_path /"outputs"/"sequence.txt"

    assert result == expected_path
    assert expected_path.read_text(encoding="utf-8") == "ACTG\n"
    

#To check if the function raises error if file write fails.
def test_save_fromatted_sequence_fail_error(tmp_path, monkeypatch):
    def raise_os_error(self, *args, **kwargs):
        raise OSError("Unable to write file")

    monkeypatch.setattr(Path, "write_text", raise_os_error)

    result = save_formatted_sequence(
        "ACTG",
        filename="sequence.txt",
        output_dir=tmp_path
    )

    assert result is None