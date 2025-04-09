import pytest
from leap import is_leap_year

def test_leap_year():
    assert is_leap_year(2000) is True
    assert is_leap_year(1996) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2023) is False