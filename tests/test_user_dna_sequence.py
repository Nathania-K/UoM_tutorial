import pytest

from SeqKit2026nk.modules.user_dna_sequence import user_dna_sequence

#To test if the module takes input and converts correctly to upper case.
def test_dna_seq_to_uppercase(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "actgactg")

    result = user_dna_sequence()
    expected_seq = "ACTGACTG"

    assert result == expected_seq


#To test if the module takes input and correctly removes whitespaces.
def test_dna_seq_removes_whitespace(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "actg ac\nt\tg")

    result = user_dna_sequence()
    expected_seq = "ACTGACTG"

    assert result == expected_seq


#To test if the module takes input and correctly accepts allowed characters (!!raises errors for invalid characters!!).
def test_dna_seq_accepts_allowed_characters(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "actgxn")

    result = user_dna_sequence()
    expected_seq = "ACTGXN"

    assert result == expected_seq

#To test if the module retries when given empty input.
def test_dna_seq_retries_empty_input(monkeypatch):
    responses = iter(["   ", "actgactg"])
    monkeypatch.setattr("builtins.input", lambda: next(responses))

    result = user_dna_sequence()
    expected_seq = "ACTGACTG"

    assert result == expected_seq


#To test if the module retries when given incorrect inputs
def test_dna_seq_retries_incorrect_input(monkeypatch):
    responses = iter(["ADTGADTG", "actgactg"])
    monkeypatch.setattr("builtins.input", lambda: next(responses))

    result = user_dna_sequence()
    expected_seq = "ACTGACTG"

    assert result == expected_seq

#To test if the module accepts cancellation and raises None.
@pytest.mark.parametrize("exception_type", [KeyboardInterrupt, EOFError])
def test_user_dna_seq_exception(monkeypatch, exception_type):
    def raise_exception():
        raise exception_type

    monkeypatch.setattr("builtins.input", raise_exception)

    result = user_dna_sequence()

    assert result is None