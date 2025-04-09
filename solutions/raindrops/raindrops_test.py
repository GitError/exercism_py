import pytest
from raindrops import convert

def test_convert_with_factors():
    assert convert(3) == "Pling"
    assert convert(5) == "Plang"
    assert convert(7) == "Plong"
    assert convert(15) == "PlingPlang"
    assert convert(21) == "PlingPlong"
    assert convert(35) == "PlangPlong"
    assert convert(105) == "PlingPlangPlong"

def test_convert_without_factors():
    assert convert(1) == "1"
    assert convert(8) == "8"
    assert convert(34) == "34"