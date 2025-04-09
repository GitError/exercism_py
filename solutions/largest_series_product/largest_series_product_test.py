import pytest
from largest_series_product import largest_product

def test_valid_series():
    assert largest_product("63915", 3) == 162
    assert largest_product("123456789", 2) == 72
    assert largest_product("10203", 2) == 6

def test_empty_series():
    assert largest_product("", 0) == 1

def test_zero_span():
    assert largest_product("12345", 0) == 1

def test_span_equal_to_series_length():
    assert largest_product("12345", 5) == 120

def test_series_with_zeros():
    assert largest_product("102030405", 2) == 20

def test_invalid_characters_in_series():
    with pytest.raises(ValueError, match="digits input must only contain digits"):
        largest_product("12a34", 2)

def test_negative_span():
    with pytest.raises(ValueError, match="span must not be negative"):
        largest_product("12345", -1)

def test_span_larger_than_series():
    with pytest.raises(ValueError, match="span must be smaller than string length"):
        largest_product("123", 5)

def test_large_series():
    series = "123456789" * 1000
    assert largest_product(series, 5) == 15120