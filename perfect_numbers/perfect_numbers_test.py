import pytest
from perfect_numbers import classify

def test_classify_perfect():
    assert classify(6) == "perfect"
    assert classify(28) == "perfect"

def test_classify_abundant():
    assert classify(12) == "abundant"
    assert classify(18) == "abundant"

def test_classify_deficient():
    assert classify(8) == "deficient"
    assert classify(2) == "deficient"

def test_invalid_input():
    with pytest.raises(ValueError, match="Number must be positive"):
        classify(-1)