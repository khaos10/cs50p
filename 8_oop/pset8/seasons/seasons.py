import inflect
import sys
from datetime import date


def main():
    print(in_minutes(input("Date of Birth: ")))


def in_minutes(s):
    try:
        birthday = date.fromisoformat(s)
        today = date.today()
        result = substraction(today, birthday)
        result_in_english = inflect.engine().number_to_words(
            result, andword='').capitalize()
        return f"{result_in_english} minutes"
    except ValueError:
        sys.exit("Invalid date")


def substraction(date1, date2):
    result = date.__sub__(date1, date2)
    return int(result.total_seconds() / 60)


if __name__ == "__main__":
    main()
