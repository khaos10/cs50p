from bank import value

def test_lower():
    assert value("hello") == 0

def test_upper():
    assert value("HELLO") == 0

def test_phrase():
    assert value("Hello, what's up?") == 0
