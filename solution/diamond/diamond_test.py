import pytest
from diamond import rows

def test_diamond_for_a():
    assert rows('A') == ["A"]

def test_diamond_for_b():
    assert rows('B') == [
        " A ",
        "B B",
        " A "
    ]

def test_diamond_for_c():
    assert rows('C') == [
        "  A  ",
        " B B ",
        "C   C",
        " B B ",
        "  A  "
    ]

def test_diamond_for_e():
    assert rows('E') == [
        "    A    ",
        "   B B   ",
        "  C   C  ",
        " D     D ",
        "E       E",
        " D     D ",
        "  C   C  ",
        "   B B   ",
        "    A    "
    ]

def test_diamond_for_invalid_input():
    with pytest.raises(ValueError):
        rows('1')  # Invalid input, not a letter

    with pytest.raises(ValueError):
        rows('')  # Empty input

    with pytest.raises(ValueError):
        rows('AA')  # More than one character