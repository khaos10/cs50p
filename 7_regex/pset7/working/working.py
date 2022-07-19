import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d{1,2}):?([0-5][0-9])? ([AP]M) to (\d{1,2}):?([0-5][0-9])? ([AP]M)$", s, re.IGNORECASE):
        start_hour_in_12 = int(matches.group(1))
        finish_hour_in_12 = int(matches.group(4))

        if valid_hour(start_hour_in_12, finish_hour_in_12):
            start_meridiem = matches.group(3)
            finish_meridiem = matches.group(6)

            start_hour_in_24 = to_24_format(start_hour_in_12, start_meridiem)
            finish_hour_in_24 = to_24_format(finish_hour_in_12, finish_meridiem)
        else:
            raise ValueError

        start_minute = format_minute(matches.group(2))
        finish_minute = format_minute(matches.group(5))

        return f"{start_hour_in_24:02}:{start_minute:02} to {finish_hour_in_24:02}:{finish_minute:02}"
    else:
        raise ValueError


def valid_hour(start_hour, finish_hour):
    if 0 < start_hour <= 12 and 0 < finish_hour <= 12:
        return True
    else:
        return False


def to_24_format(hour, meridiem):
    if hour == 12 and meridiem == "AM":
        return 00
    elif hour != 12 and meridiem == "PM":
        return hour + 12
    else:
        return hour

def format_minute(minute):
    return int(minute) if minute != None else 00

if __name__ == "__main__":
    main()
