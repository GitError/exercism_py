import pytest
from lists import add_item, remove_item, get_item, list_length

def test_add_item():
    assert add_item([], 1) == [1]
    assert add_item([1, 2], 3) == [1, 2, 3]

def test_remove_item():
    assert remove_item([1, 2, 3], 2) == [1, 3]
    assert remove_item([1, 2, 3], 4) == [1, 2, 3]

def test_get_item():
    assert get_item([1, 2, 3], 1) == 2
    with pytest.raises(IndexError):
        get_item([1, 2, 3], 5)

def test_list_length():
    assert list_length([]) == 0
    assert list_length([1, 2, 3]) == 3