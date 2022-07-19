import pytest
from working import convert

def test_valid_time_without_minute():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_valid_time_with_minute():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_at_12am():
    assert convert("12:00 AM to 5:00 PM") == "00:00 to 17:00"

def test_at_12pm():
    assert convert("9:00 AM to 12:00 PM") == "09:00 to 12:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("0:30 AM to 13:00 PM")
