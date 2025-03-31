import pytest
from resistor_color_trio import label

def test_label():
    assert label(["orange", "orange", "black"]) == "33 ohms"
    assert label(["blue", "grey", "brown"]) == "680 ohms"
    assert label(["red", "black", "red"]) == "2 kiloohms"
    assert label(["green", "brown", "orange"]) == "51 kiloohms"