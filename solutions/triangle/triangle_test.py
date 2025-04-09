import pytest
from triangle import is_equilateral, is_isosceles, is_scalene

def test_is_equilateral():
    assert is_equilateral(2, 2, 2) is True
    assert is_equilateral(2, 3, 4) is False

def test_is_isosceles():
    assert is_isosceles(2, 2, 3) is True
    assert is_isosceles(2, 3, 4) is False

def test_is_scalene():
    assert is_scalene(2, 3, 4) is True
    assert is_scalene(2, 2, 3) is False