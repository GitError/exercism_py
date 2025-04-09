import pytest
from resistor_color_duo import value

def test_value():
    assert value(["brown", "black"]) == 10
    assert value(["blue", "grey"]) == 68
    assert value(["yellow", "violet"]) == 47
    assert value(["orange", "orange"]) == 33