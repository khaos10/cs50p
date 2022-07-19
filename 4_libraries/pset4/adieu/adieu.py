import inflect
p = inflect.engine()

names = []

def main():
    names = get_name()
    print(f"Adieu, adieu, to { p.join(names) }")

def get_name():
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            return names


main()
