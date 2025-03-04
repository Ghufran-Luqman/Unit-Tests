#with pytest:
from main import double
import pytest

def test_two():
    assert double(2) == 4
def test_three():
    assert double(3) == 6
def test_zero():
    assert double(0) == 0
def test_str():
    with pytest.raises(ValueError):
        double("two")