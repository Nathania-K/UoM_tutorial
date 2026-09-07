import pytest

from SeqKit2026nk.modules.translate_rna import translate_rna

#To test if module correctly cleans input and replaces codons with correct amino acids.
def test_translate_rna_correctly():

    test_rna_sequence = "1 augcucagcu uuguggauac g"

    translated_rna_seq = translate_rna(test_rna_sequence)

    expected_translated_rna = "MLSFVDT"

    assert translated_rna_seq == expected_translated_rna


#To test if module returns None upon empty string.
def test_translate_rna_empty():
    assert translate_rna("") is None


#To Test if module allows for uppercase entry
def test_translate_rna_uppercase_entry():

    test_uppercase_rna_seq = "1 AUGCUCAGCU UUGUGGAUAC G"

    translated_uppercase_seq = translate_rna(test_uppercase_rna_seq)

    expected_translated_uppercase_rna = "MLSFVDT"

    assert translated_uppercase_seq == expected_translated_uppercase_rna


#To test if the module transcribes stop codon correctly to '*'
@pytest.mark.parametrize("stop_codon", ["uga", "uaa", "uag"])
def test_translate_rna_stop_codons(stop_codon):

    translated_stop_seq = translate_rna(stop_codon)

    expected_stop_codon_seq = "*"

    assert translated_stop_seq == expected_stop_codon_seq


#To test if the module transcribes 'x' or 'n' to 'X' in protein sequence.
def test_translate_rna_nx_sequence():

    test_ambigious_seq = "1 augxucngcu uuguggauac g"

    translated_ambigious_seq = translate_rna(test_ambigious_seq)

    expected_ambigious_seq = "MXXFVDT"

    assert translated_ambigious_seq == expected_ambigious_seq


#To test if the module successfully ignores incomplete bases.
def test_translate_rna_ignore_bases():
    
    test_incomplete_bases_seq = "1 augcucagcu uuguggauac gau"

    translated_incomplete_bases = translate_rna(test_incomplete_bases_seq)

    expected_incomplete_bases_seq = "MLSFVDT"

    assert translated_incomplete_bases == expected_incomplete_bases_seq
