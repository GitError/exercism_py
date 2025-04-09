import pytest
from collatz_conjecture import steps

def test_steps_for_positive_numbers():
    assert steps(1) == 0
    assert steps(2) == 1
    assert steps(3) == 7
    assert steps(4) == 2
    assert steps(16) == 4
    assert steps(12) == 9
    assert steps(19) == 20

def test_large_number():
    assert steps(1000000) == 152

def test_invalid_input_zero():
    with pytest.raises(ValueError, match="Only positive integers are allowed"):
        steps(0)

def test_invalid_input_negative():
    with pytest.raises(ValueError, match="Only positive integers are allowed"):
        steps(-15)