import pytest
from darts import score

def test_score_inner_circle():
    assert score(0, 0) == 10

def test_score_middle_circle():
    assert score(3, 3) == 5

def test_score_outer_circle():
    assert score(7, 7) == 1

def test_score_outside_target():
    assert score(10, 10) == 0

def test_score_on_boundary():
    assert score(1, 0) == 10
    assert score(5, 0) == 5
    assert score(8, 0) == 1