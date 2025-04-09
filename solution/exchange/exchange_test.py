import pytest
from exchange import exchange_money, get_change, get_value_of_bills

def test_exchange_money():
    assert exchange_money(100, 1.2) == 120
    assert exchange_money(200, 0.8) == 160

def test_get_change():
    assert get_change(100, 45) == 55
    assert get_change(50, 50) == 0

def test_get_value_of_bills():
    assert get_value_of_bills(10, 5) == 50
    assert get_value_of_bills(0, 5) == 0