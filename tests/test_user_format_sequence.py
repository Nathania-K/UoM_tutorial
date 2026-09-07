import pytest

from SeqKit2026nk.modules.user_format_sequence import user_format_sequence


#To test if module correctly formats defualt settings (block_size=10, blocks_per_line=6)
def test_user_format_sequence_default():
    test_default_seq = "A" * 65

    result = user_format_sequence(test_default_seq)

    expected_seq = (
        "        1 AAAAAAAAAA AAAAAAAAAA AAAAAAAAAA "
        "AAAAAAAAAA AAAAAAAAAA AAAAAAAAAA\n"
        "       61 AAAAA"
    )

    assert result == expected_seq

#To test if module correctly formats to custom settings.
def test_user_format_sequence_default():
    test_custom_seq = "ACTGACTGACTG"

    result = user_format_sequence(
        test_custom_seq,
        block_size=4,
        blocks_per_line=2,
        )

    expected_seq = (
        "        1 ACTG ACTG\n"
        "        9 ACTG"
    )

    assert result == expected_seq


#To test if the module returns None if an empty sequence is supplied.
@pytest.mark.parametrize("empty_seq", ["", None])
def test_user_format_sequence_None(empty_seq):

    result = user_format_sequence(empty_seq)

    assert result is None


#To test if module raises error if value of 0 is supplied.
@pytest.mark.parametrize(("block_size", "blocks_per_line"),
    [
        (0, 6),
        (10, 0),
        (-1, 6),
        (10, -1),
    ], 
)
def test_user_format_sequence_exception(block_size, blocks_per_line):

    result = user_format_sequence("ACTGACTG", 
    block_size=block_size,
    blocks_per_line=blocks_per_line,)

    assert result is None