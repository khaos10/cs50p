from um import count

def test_only_um():
    assert count("um") == 1

def test_punctuation():
    assert count("um?") == 1

def test_case_insensitive():
    assert count("Um, um, UM") == 3

def test_substring():
    assert count("yummy") == 0
