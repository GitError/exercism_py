import pytest
from matching_brackets import is_paired

def test_balanced_brackets():
    assert is_paired("()") is True
    assert is_paired("[]") is True
    assert is_paired("{}") is True
    assert is_paired("{[()]}") is True
    assert is_paired("{what is (42)}?") is True
    assert is_paired("a + b - (c * d) / e") is True

def test_unbalanced_brackets():
    assert is_paired("(") is False
    assert is_paired(")") is False
    assert is_paired("{[}]") is False
    assert is_paired("{[(])}") is False
    assert is_paired("[text}") is False
    assert is_paired("{[}") is False

def test_empty_string():
    assert is_paired("") is True

def test_only_opening_brackets():
    assert is_paired("(((") is False
    assert is_paired("[[[") is False
    assert is_paired("{{{") is False

def test_only_closing_brackets():
    assert is_paired(")))") is False
    assert is_paired("]]]") is False
    assert is_paired("}}}") is False

def test_mixed_characters():
    assert is_paired("function() { return [1, 2, 3]; }") is True
    assert is_paired("if (x > y) { [z] } else { }") is True
    assert is_paired("while (true) { do_something(); }") is True