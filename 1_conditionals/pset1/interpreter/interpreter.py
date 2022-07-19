def main():
    expression = input("Expression: ")
    result = calculate(expression)
    print(f"{result:.1f}")


def calculate(e):
    x, y, z = e.split(" ")

    if y == "+":
        return int(x) + int(z)
    elif y == "-":
        return int(x) - int(z)
    elif y == "*":
        return int(x) * int(z)
    elif y == "/":
        return int(x) / int(z)


main()
