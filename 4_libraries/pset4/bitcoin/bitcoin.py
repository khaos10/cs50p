import json
import requests
import sys


def main():
    num_bitcoins = get_number()
    rate = get_rate()
    print(f"${rate * num_bitcoins:,.4f}")


def get_number():
    while True:
        try:
            if len(sys.argv) < 2:
                sys.exit("Missing command-line argument")
            else:
                return float(sys.argv[1])
        except TypeError:
            sys.exit("Command-line argument is not a number")


def get_rate():
    response = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json")
    return response.json()["bpi"]["USD"]["rate_float"]


main()
