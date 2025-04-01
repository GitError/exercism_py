import pytest
from binary_search import find

def test_value_in_middle():
    assert find([1, 2, 3, 4, 5], 3) == 2

def test_value_at_start():
    assert find([1, 2, 3, 4, 5], 1) == 0

def test_value_at_end():
    assert find([1, 2, 3, 4, 5], 5) == 4

def test_value_not_in_list():
    with pytest.raises(ValueError, match="value not in array"):
        find([1, 2, 3, 4, 5], 6)

def test_empty_list():
    with pytest.raises(ValueError, match="value not in array"):
        find([], 1)

def test_single_element_list_value_present():
    assert find([42], 42) == 0

def test_single_element_list_value_absent():
    with pytest.raises(ValueError, match="value not in array"):
        find([42], 7)

def test_large_list():
    large_list = list(range(1, 10001))
    assert find(large_list, 5000) == 4999

def test_value_in_left_half():
    assert find([10, 20, 30, 40, 50], 20) == 1

def test_value_in_right_half():
    assert find([10, 20, 30, 40, 50], 40) == 3