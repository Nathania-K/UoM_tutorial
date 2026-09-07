import pytest

from SeqKit2026nk.modules.transcribe_to_rna import transcribe_to_rna

test_dna_input = "1 ACTGACTGAC TGACTGACTG"

#To test if the module correctly replaces "T" bases with "U" and returns a lowercase sequence.
def test_transcribe_to_rna():
    transcribed_rna = transcribe_to_rna(test_dna_input)
    expected_transcribed_dna = test_dna_input.replace("T", "U").lower()

    assert transcribed_rna == expected_transcribed_dna

#To test if the module returns None if an empty string is supplied. 
def test_transcribe_to_rna_empty():
    assert transcribe_to_rna("") is None