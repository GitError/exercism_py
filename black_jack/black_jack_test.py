import pytest
from black_jack import (
    value_of_card,
    higher_card,
    value_of_ace,
    is_blackjack,
    can_split_pairs,
    can_double_down,
)

def test_value_of_card():
    assert value_of_card("2") == 2
    assert value_of_card("10") == 10
    assert value_of_card("J") == 10
    assert value_of_card("Q") == 10
    assert value_of_card("K") == 10
    assert value_of_card("A") == 1

def test_higher_card():
    assert higher_card("10", "5") == "10"
    assert higher_card("A", "K") == "K"
    assert higher_card("5", "5") == ("5", "5")

def test_value_of_ace():
    assert value_of_ace("5", "5") == 11
    assert value_of_ace("10", "A") == 1
    assert value_of_ace("A", "9") == 1
    assert value_of_ace("2", "3") == 11

def test_is_blackjack():
    assert is_blackjack("A", "10") is True
    assert is_blackjack("10", "A") is True
    assert is_blackjack("A", "5") is False
    assert is_blackjack("10", "9") is False

def test_can_split_pairs():
    assert can_split_pairs("5", "5") is True
    assert can_split_pairs("10", "K") is True
    assert can_split_pairs("A", "A") is True
    assert can_split_pairs("10", "5") is False

def test_can_double_down():
    assert can_double_down("5", "4") is True
    assert can_double_down("10", "9") is False
    assert can_double_down("A", "8") is False
    assert can_double_down("6", "3") is True