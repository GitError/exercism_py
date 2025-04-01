import pytest
from square_root import square_root

def test_square_root_of_perfect_squares():
    assert square_root(1) == 1
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(16) == 4
    assert square_root(25) == 5
    assert square_root(36) == 6
    assert square_root(49) == 7
    assert square_root(64) == 8
    assert square_root(81) == 9
    assert square_root(100) == 10

def test_large_perfect_square():
    assert square_root(10000) == 100
    assert square_root(1048576) == 1024

def test_invalid_input_negative_number():
    with pytest.raises(ValueError, match="Input must be a positive whole number."):
        square_root(-4)

def test_invalid_input_zero():
    with pytest.raises(ValueError, match="Input must be a positive whole number."):
        square_root(0)

def test_no_integer_square_root():
    with pytest.raises(ValueError, match="No integer square root found for the given number."):
        square_root(2)
    with pytest.raises(ValueError, match="No integer square root found for the given number."):
        square_root(3)
    with pytest.raises(ValueError, match="No integer square root found for the given number."):
        square_root(5)