import pytest
from pig_latin import translate

def test_translate_single_word():
    assert translate("apple") == "appleay"
    assert translate("banana") == "ananabay"

def test_translate_multiple_words():
    assert translate("eat pie") == "eatay iepay"
    assert translate("hello world") == "ellohay orldway"

def test_translate_with_consonant_clusters():
    assert translate("chair") == "airchay"
    assert translate("school") == "oolschay"