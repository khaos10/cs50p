def main():
    variable = input("camelCase: ")
    convert(variable)


def convert(variable):
    print("snake_case: ", end="")

    for letter in variable:
        if letter.isupper():
            print(f"_{letter.lower()}", end="")
        else:
            print(letter, end="")

    print()


main()
