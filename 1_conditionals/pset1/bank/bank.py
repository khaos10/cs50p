def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    formatted_greeting = greeting.strip().lower()

    if formatted_greeting.startswith("hello"):
        return 0
    elif formatted_greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
