import pytest
from lasagna import expected_minutes_in_oven, remaining_minutes_in_oven, preparation_time_in_minutes, elapsed_time_in_minutes

def test_expected_minutes_in_oven():
    assert expected_minutes_in_oven() == 40

def test_remaining_minutes_in_oven():
    assert remaining_minutes_in_oven(30) == 10
    assert remaining_minutes_in_oven(0) == 40

def test_preparation_time_in_minutes():
    assert preparation_time_in_minutes(2) == 4
    assert preparation_time_in_minutes(0) == 0

def test_elapsed_time_in_minutes():
    assert elapsed_time_in_minutes(2, 30) == 34
    assert elapsed_time_in_minutes(0, 10) == 10