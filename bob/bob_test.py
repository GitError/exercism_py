import pytest
from bob import response

def test_silence():
    assert response("") == "Fine. Be that way!"
    assert response("   ") == "Fine. Be that way!"

def test_shouting():
    assert response("HELLO") == "Whoa, chill out!"
    assert response("WHAT IS THIS") == "Whoa, chill out!"

def test_shouting_question():
    assert response("HOW ARE YOU?") == "Calm down, I know what I'm doing!"
    assert response("WHAT?") == "Calm down, I know what I'm doing!"

def test_question():
    assert response("How are you?") == "Sure."
    assert response("Is this a test?") == "Sure."

def test_statement():
    assert response("This is a statement.") == "Whatever."
    assert response("Hello there.") == "Whatever."