def main():
    percentage = convert("Fraction: ")
    result = gauge(percentage)
    print(result)


def convert(fraction):
    while True:
        try:
            splitted_fraction = input(fraction).split("/")
            x, y = int(splitted_fraction[0]), int(splitted_fraction[1])
            if x > y:
                continue
            return round((x / y) * 100)
        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
