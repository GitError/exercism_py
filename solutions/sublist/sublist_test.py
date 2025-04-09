import pytest
from sublist import sublist

def test_sublist_equal():
    assert sublist([1, 2, 3], [1, 2, 3]) == "equal"

def test_sublist_sublist():
    assert sublist([1, 2], [1, 2, 3]) == "sublist"

def test_sublist_superlist():
    assert sublist([1, 2, 3], [2]) == "superlist"

def test_sublist_unequal():
    assert sublist([1, 2, 3], [4, 5, 6]) == "unequal"