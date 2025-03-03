#original testing without pytest:
from calculator import double

def main():
    test_double()

def test_double():
    try:
        assert double(2) == 4
    except:
        print("2 failed")
    try:
        assert double(3) == 6
    except:
        print("3 failed")
    try:
        assert double(0) == 0
    except:
        print("0 failed")

if __name__ == "__main__":
    main()

