import pytest
from grains import square, total

def test_square():
    assert square(1) == 1
    assert square(2) == 2
    assert square(3) == 4
    assert square(64) == 9223372036854775808

def test_square_invalid():
    with pytest.raises(ValueError, match="square must be between 1 and 64"):
        square(0)
    with pytest.raises(ValueError, match="square must be between 1 and 64"):
        square(65)

def test_total():
    assert total() == 18446744073709551615