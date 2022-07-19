from plates import is_valid

def test_start():
    assert is_valid("5050") == False

def test_min():
    assert is_valid("H") == False

def test_middle():
    assert is_valid("CS50P") == False

def test_periode():
    assert is_valid("PI3.14") == False

def test_zero():
    assert is_valid("CS05") == False
