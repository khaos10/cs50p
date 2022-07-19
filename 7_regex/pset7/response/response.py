from validator_collection import checkers


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    return "Valid" if checkers.is_email(s) else "Invalid"


if __name__ == "__main__":
    main()
