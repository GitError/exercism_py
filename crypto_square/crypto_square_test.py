import pytest
from crypto_square import cipher_text

def test_normal_case():
    assert cipher_text("If man was meant to stay on the ground, god would have given us roots.") == \
           "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau "

def test_empty_string():
    assert cipher_text("") == ""

def test_single_character():
    assert cipher_text("A") == "a"

def test_perfect_square_length():
    assert cipher_text("abcd efgh ijkl mnop") == "aeim bfjn cgko dhlp"

def test_non_square_length():
    assert cipher_text("Hello, World!") == "hwe olr llo d  "

def test_all_spaces_and_punctuation():
    assert cipher_text("   !!!") == ""

def test_long_text():
    text = "The quick brown fox jumps over the lazy dog"
    expected = "tbjrdh eqoouu hfxez  ikwvp  cnlay  krogs  "
    assert cipher_text(text) == expected