import pytest
from all_your_base import rebase

def test_valid_conversion():
    assert rebase(10, [1, 0], 2) == [1, 0, 1, 0]
    assert rebase(2, [1, 0, 1, 0], 10) == [1, 0]
    assert rebase(16, [1, 15], 10) == [3, 1]

def test_zero_conversion():
    assert rebase(10, [0], 2) == [0]
    assert rebase(2, [0], 10) == [0]

def test_single_digit_conversion():
    assert rebase(10, [5], 2) == [1, 0, 1]
    assert rebase(2, [1], 10) == [1]

def test_invalid_input_base():
    with pytest.raises(ValueError, match="input base must be >= 2"):
        rebase(1, [1, 0], 2)

def test_invalid_output_base():
    with pytest.raises(ValueError, match="output base must be >= 2"):
        rebase(10, [1, 0], 1)

def test_invalid_digits():
    with pytest.raises(ValueError, match="all digits must satisfy 0 <= d < input base"):
        rebase(10, [1, -1], 2)
    with pytest.raises(ValueError, match="all digits must satisfy 0 <= d < input base"):
        rebase(10, [1, 10], 2)

def test_empty_digits():
    assert rebase(10, [], 2) == [0]

def test_large_number_conversion():
    assert rebase(10, [1, 2, 3, 4, 5], 16) == [1, 14, 7, 1]