import pytest
from atbash_cipher import encode, decode

def test_encode_simple_text():
    assert encode("test") == "gvhg"

def test_encode_with_numbers():
    assert encode("x123 yes") == "c123b vh"

def test_encode_with_punctuation_and_spaces():
    assert encode("hello, world!") == "svool dliow"

def test_encode_empty_string():
    assert encode("") == ""

def test_encode_numbers_only():
    assert encode("12345") == "12345"

def test_decode_simple_text():
    assert decode("gvhg") == "test"

def test_decode_with_spaces():
    assert decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt") == "thequickbrownfoxjumpsoverthelazydog"

def test_decode_empty_string():
    assert decode("") == ""

def test_decode_numbers_only():
    assert decode("12345") == "12345"

def test_encode_and_decode():
    original_text = "The quick brown fox jumps over the lazy dog 123!"
    encoded_text = encode(original_text)
    decoded_text = decode(encoded_text)
    assert decoded_text == "thequickbrownfoxjumpsoverthelazydog123"