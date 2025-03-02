def main():
    number = int(input("Enter a number to double.\n"))
    print(f"{number} doubled is {double(number)}")

def double(number):
    return number * 2

if __name__ == "__main__":
    main()