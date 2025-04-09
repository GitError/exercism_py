import pytest
from armstrong_numbers import is_armstrong_number

def test_single_digit_numbers_are_armstrong_numbers():
    for number in range(10):
        assert is_armstrong_number(number) is True

def test_valid_armstrong_numbers():
    assert is_armstrong_number(153) is True
    assert is_armstrong_number(9474) is True
    assert is_armstrong_number(9475) is False
    assert is_armstrong_number(370) is True
    assert is_armstrong_number(371) is True
    assert is_armstrong_number(407) is True

def test_non_armstrong_numbers():
    assert is_armstrong_number(10) is False
    assert is_armstrong_number(123) is False
    assert is_armstrong_number(100) is False

def test_large_armstrong_number():
    assert is_armstrong_number(9926315) is True
    assert is_armstrong_number(9926314) is False