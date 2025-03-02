
#original testing without pytest:
'''
from calculator import double

def main():
    test_double()

def test_double():
    assert double(2) == 4
    assert double(3) == 6

if __name__ == "__main__":
    main()
'''

#with pytest:
from calculator import double
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