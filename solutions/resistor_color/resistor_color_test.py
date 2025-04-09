import pytest
from resistor_color import color_code, colors

def test_color_code():
    assert color_code("black") == 0
    assert color_code("brown") == 1
    assert color_code("red") == 2
    assert color_code("green") == 5
    assert color_code("white") == 9

def test_colors():
    assert colors() == [
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"
    ]