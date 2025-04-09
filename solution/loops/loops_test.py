import pytest
from loops import sum_numbers, count_even_numbers

def test_sum_numbers():
    assert sum_numbers([1, 2, 3]) == 6
    assert sum_numbers([]) == 0

def test_count_even_numbers():
    assert count_even_numbers([1, 2, 3, 4]) == 2
    assert count_even_numbers([1, 3, 5]) == 0