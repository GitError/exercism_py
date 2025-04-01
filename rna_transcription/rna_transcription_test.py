import pytest
from rna_transcription import to_rna

def test_valid_dna_to_rna():
    assert to_rna("G") == "C"
    assert to_rna("C") == "G"
    assert to_rna("T") == "A"
    assert to_rna("A") == "U"
    assert to_rna("ACGTGGTCTTAA") == "UGCACCAGAAUU"

def test_empty_dna_strand():
    assert to_rna("") == ""

def test_mixed_case_dna():
    with pytest.raises(KeyError):
        to_rna("AcGt")

def test_invalid_characters_in_dna():
    with pytest.raises(KeyError):
        to_rna("ACGTX")
    with pytest.raises(KeyError):
        to_rna("1234")
    with pytest.raises(KeyError):
        to_rna("ACGT!")

def test_long_dna_strand():
    dna_strand = "G" * 1000 + "C" * 1000 + "T" * 1000 + "A" * 1000
    expected_rna = "C" * 1000 + "G" * 1000 + "A" * 1000 + "U" * 1000
    assert to_rna(dna_strand) == expected_rna