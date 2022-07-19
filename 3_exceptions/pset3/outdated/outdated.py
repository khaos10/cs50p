months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    year, month, day = get_date()
    print(f"{year:04}-{month:02}-{day:02}")


def get_date():
    while True:
        try:
            date = input("Date: ")

            if "/" in date and not " " in date:
                splitted_date = date.split("/")
                year = int(splitted_date[2])
                month = int(splitted_date[0])
                day = int(splitted_date[1])

                if valid_date(month, day):
                    return year, month, day
                else:
                    pass

            elif "," in date:
                splitted_date = date.split()
                year = splitted_date[2]
                month = splitted_date[0]
                day = splitted_date[1]
                if month in months and "," in day:
                    year = int(year)
                    month = months.index(month) + 1
                    day = int(day.replace(",", ""))
                    if valid_date(month, day):
                        return year, month, day
                    else:
                        pass
                else:
                    pass
            else:
                pass

        except (ValueError, TypeError):
            pass


def valid_date(month, day):
    if 0 < month < 13 and 0 < day < 32:
        return True
    else:
        return False


main()
