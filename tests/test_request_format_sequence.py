import pytest

from SeqKit2026nk.modules.request_format_settings import request_format_settings

#To test if the module can correctly recieve cutom settings for block number/blocks per line.
def test_request_custom_formatting(monkeypatch):
    responses = iter(["5", "4"])
    monkeypatch.setattr("builtins.input", lambda: next(responses))

    result = request_format_settings()
    example_custom_settings = (5, 4)

    assert result == example_custom_settings

#To test if the module can correctly calls default settings upon pressing enter for block number/blocks per line.
def test_request_default_formatting(monkeypatch):
    responses = iter(["", ""])
    monkeypatch.setattr("builtins.input", lambda: next(responses))

    result = request_format_settings()
    default_settings = (10, 6)

    assert result == default_settings

#To test if the module can returns None when entering "q" or "quit" to initiate a cancelled response.
@pytest.mark.parametrize("cancel_response", ["q", "quit"])
def test_request_cancel_formatting(monkeypatch, cancel_response):
    monkeypatch.setattr("builtins.input", lambda: cancel_response)

    result = request_format_settings()

    assert result is None

#To test if the module can returns None when raising a keyboard interrupt/E0FEerror to initiate a cancelled response.
@pytest.mark.parametrize("exception_type", [KeyboardInterrupt, EOFError])
def test_request_formatting_exception(monkeypatch, exception_type):
    def raise_exception():
        raise exception_type

    monkeypatch.setattr("builtins.input", raise_exception)

    result = request_format_settings()

    assert result is None