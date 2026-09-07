from datetime import datetime

import pytest

from SeqKit2026nk.utils import util_mods

#################################
### Tests for choose_filename ###
#################################

#To test extensions (.txt) functioning with variety of inputs
@pytest.mark.parametrize(
    ("response", "expected"),
    [("sequence", "sequence.txt"),
    ("sequence.txt", "sequence.txt"),
    ("sequence.TXT", "sequence.TXT"),
    ]
)
def test_choose_filename_extensions_check(monkeypatch, response, expected):
    monkeypatch.setattr("builtins.input", lambda: response)

    result  = util_mods.choose_filename()

    assert result == expected


#To test timestamped filename functions correctly
def test_choose_filename_timestamp_default(monkeypatch):
    class FixedDatetime: 
        @classmethod
        def now(cls):
            return datetime(2026, 9, 7, 14, 21, 00)

    monkeypatch.setattr(util_mods, "datetime", FixedDatetime)
    monkeypatch.setattr("builtins.input", lambda: "")

    result = util_mods.choose_filename("formatted_dna")

    assert result == "formatted_dna_2026-09-07-14-21-00.txt"


#To test if paths are rejected/retried
def test_choose_filename_rejects_path(monkeypatch):
    responses = iter(["output/sequence.txt", "sequence.txt"])

    monkeypatch.setattr("builtins.input", lambda: next(responses))

    result = util_mods.choose_filename()

    assert result == "sequence.txt"


#To test if modules correctly cancels file save upon request.abs
@pytest.mark.parametrize("response", ["q", "Q", "quit", "QUIT"])
def test_choose_filename_cancel(monkeypatch, response):
    monkeypatch.setattr("builtins.input", lambda: response)

    assert util_mods.choose_filename() is None


####################################
### Tests for prompt_to_continue ###
####################################

#To test if function correctly cancels continuation upon request
@pytest.mark.parametrize(
    ("response", "expected"),
    [
        ("", True),
        ("q", False),
        ("Q", False),
        ("quit", False),
        ("QUIT", False),
    ],
)
def test_prompt_to_continue_expected_results(monkeypatch, response, expected):
    monkeypatch.setattr("builtins.input", lambda: response)

    result = util_mods.prompt_to_continue()

    assert result is expected

#To test if function correctly retries upon invalid response
def test_prompt_to_continue_retries(monkeypatch):
    responses = iter(["maybe", ""])

    monkeypatch.setattr("builtins.input", lambda: next(responses))

    assert util_mods.prompt_to_continue() is True


#################################
### Tests for request_integer ###
#################################

#To test if function correctly recieves custom integer input
def test_user_integer_accepts_positive(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "5")

    result = util_mods.request_integer("block size", 10)

    assert result == 5


#To test if function correctly reverts to default integer upon input
def test_user_integer_defaults(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "")

    result = util_mods.request_integer("block size", 10)

    assert result == 10


#To test if function retries upon invalid inputs (string/0/-integers)
def test_request_integer_retries(monkeypatch):
    responses = iter(["abc", "0", "-2", "5"])

    monkeypatch.setattr("builtins.input", lambda: next(responses))

    result = util_mods.request_integer("block size", 10)

    assert result == 5 

#To test if function cancels correctly upon request.
@pytest.mark.parametrize("response", ["q", "Q", "quit", "QUIT"])
def test_request_integer_cancel(monkeypatch, response):
    monkeypatch.setattr("builtins.input", lambda: response)

    result = util_mods.request_integer("block size", 10)

    assert result is None

################################
### Tests for request_yes_no ###
################################

#To test if function correctly returns True/False upon input
@pytest.mark.parametrize("response", ["y", "Y", "yes", "YES"])
def test_request_yes_no_accepts_yes(monkeypatch, response):
    monkeypatch.setattr("builtins.input", lambda: response)

    assert util_mods.request_yes_no() is True

@pytest.mark.parametrize("response", ["n", "N", "no", "NO"])
def test_request_yes_no_accepts_no(monkeypatch, response):
    monkeypatch.setattr("builtins.input", lambda: response)

    assert util_mods.request_yes_no() is False

#To test if function retries on incorrect input until valid input supplied
def test_request_yes_no_retries(monkeypatch):
    responses = iter (["maybe", "yes"])
    monkeypatch.setattr("builtins.input", lambda: next(responses))

    assert util_mods.request_yes_no() is True

####################################
### Tests for exception_handling ###
####################################

#To test if all functions handle exceptions correctly

@pytest.mark.parametrize ("exception_type", [KeyboardInterrupt, EOFError])
@pytest.mark.parametrize(
    ("function", "arguments", "expected"),
    [
        (util_mods.choose_filename, (), None),
        (util_mods.prompt_to_continue, (), False),
        (
            util_mods.request_integer,
            ("block size", 10),
            None,
        ),
        (util_mods.request_yes_no, (), False),
    ],
)

def test_functions_handle_exceptions(
    monkeypatch,
    exception_type,
    function,
    arguments,
    expected,
):
    def raise_exception(): 
        raise exception_type

    monkeypatch.setattr("builtins.input", raise_exception)

    result = function(*arguments)

    assert result is expected