from calculator import double

def main():
    test_double()

def test_double():
    assert double(2) == 4
    assert double(3) == 6

if __name__ == "__main__":
    main()