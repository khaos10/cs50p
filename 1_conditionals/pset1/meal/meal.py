def main():
    time = input("What time is it? ")
    converted_time = convert(time)

    if 7 <= converted_time <= 8:
        meal = "breakfast"
    elif 12 <= converted_time <= 13:
        meal = "lunch"
    elif 18 <= converted_time <= 19:
        meal = "dinner"
    else:
        return

    print(f"{meal} time")


def convert(time):
    if time.endswith("a.m."):
        time = time.replace(" a.m.", "")
        hours, minutes = time.split(":")
    elif time.endswith("p.m."):
        time = time.replace(" p.m.", "")
        hours, minutes = time.split(":")
        hours = float(hours) + 12
    else:
        hours, minutes = time.split(":")

    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
