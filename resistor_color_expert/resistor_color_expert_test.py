import pytest
from resistor_color_expert import calculate_resistance

def test_calculate_resistance():
    assert calculate_resistance(["brown", "black", "red", "gold"]) == "1 kiloohms ±5%"
    assert calculate_resistance(["red", "red", "orange", "silver"]) == "22 kiloohms ±10%"
    assert calculate_resistance(["yellow", "violet", "yellow", "none"]) == "470 kiloohms ±20%"