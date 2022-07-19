import pytest
from fuel import convert, gauge


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("three/four")

def test_percentage():
    assert convert("3/4") == 75

def test_full():
    assert gauge(99) == "F"

def test_empty():
    assert gauge(1) == "E"

def test_gauge():
    assert gauge(50) == "50%"
