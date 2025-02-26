from calculator import double

def main():
    test_double()

def test_double():
    assert double(2) == 4
    assert double(3) == 6 #works perfectly, now I will test with an error in the original function (double).

if __name__ == "__main__":
    main()