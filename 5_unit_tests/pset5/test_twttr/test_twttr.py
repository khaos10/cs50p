from twttr import shorten


def test_vowels():
    assert shorten("Twitter") == "Twttr"

def test_lower():
    assert shorten("lower") == "lwr"

def test_upper():
    assert shorten("UPPER") == "PPR"

def test_number():
    assert shorten("CS50") == "CS50"

def test_puctuation():
    assert shorten("What's up?") == "Wht's p?"
