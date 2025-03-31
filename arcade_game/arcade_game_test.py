import pytest
from arcade_game import eat_ghost, score, lose, win

def test_eat_ghost():
    assert eat_ghost(True, True) is True
    assert eat_ghost(True, False) is False
    assert eat_ghost(False, True) is False
    assert eat_ghost(False, False) is False

def test_score():
    assert score(True, True) is True
    assert score(True, False) is True
    assert score(False, True) is True
    assert score(False, False) is False

def test_lose():
    assert lose(False, True) is True
    assert lose(True, True) is False
    assert lose(False, False) is False
    assert lose(True, False) is False

def test_win():
    assert win(True, False, False) is True
    assert win(True, True, False) is True
    assert win(True, False, True) is False
    assert win(False, False, False) is False
    assert win(False, True, True) is False