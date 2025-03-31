import pytest
from anagram import find_anagrams

def test_find_anagrams_with_valid_anagrams():
    assert find_anagrams("listen", ["enlist", "google", "inlets", "banana"]) == ["enlist", "inlets"]
    assert find_anagrams("master", ["stream", "pigeon", "maters"]) == ["stream", "maters"]

def test_find_anagrams_with_no_anagrams():
    assert find_anagrams("hello", ["world", "python", "java"]) == []
    assert find_anagrams("python", ["java", "ruby", "perl"]) == []

def test_find_anagrams_with_identical_word():
    assert find_anagrams("banana", ["banana", "BANANA", "anaban"]) == ["anaban"]

def test_find_anagrams_case_insensitivity():
    assert find_anagrams("Listen", ["Enlist", "Google", "Inlets", "Banana"]) == ["Enlist", "Inlets"]
    assert find_anagrams("Orchestra", ["cashregister", "Carthorse", "radishes"]) == ["Carthorse"]

def test_find_anagrams_with_empty_candidates():
    assert find_anagrams("word", []) == []

def test_find_anagrams_with_empty_word():
    assert find_anagrams("", ["", "a", "b"]) == [""]

def test_find_anagrams_with_special_characters():
    assert find_anagrams("a-b-c", ["c-b-a", "abc", "cab"]) == ["c-b-a"]

def test_find_anagrams_with_numbers():
    assert find_anagrams("123", ["321", "231", "456"]) == ["321", "231"]