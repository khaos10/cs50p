import pytest
from seasons import in_minutes, substraction

def test_invalid_date():
    with pytest.raises(SystemExit):
        in_minutes("January 1, 1999")
