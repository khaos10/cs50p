import pytest
from numb3rs import validate

def test_first_byte():
    assert validate("64.128.256.512") == False

def test_true():
    assert validate("255.255.255.255") == True

def test_false():
    assert validate("512.512.512.512") == False

def test_alpha():
    assert validate("cat") == False
