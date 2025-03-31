import pytest
from conditionals import check_condition

def test_check_condition_true():
    assert check_condition(True) == "Condition is True"

def test_check_condition_false():
    assert check_condition(False) == "Condition is False"

def test_check_condition_invalid():
    with pytest.raises(ValueError, match="Invalid condition"):
        check_condition(None)