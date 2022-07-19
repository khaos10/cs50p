import csv
import sys
from tabulate import tabulate

menu = []


def main():
    read_file()
    print(tabulate(menu, headers="keys", tablefmt="grid"))


def read_file():
    while True:
        try:
            if len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")
            elif not sys.argv[1].endswith(".csv"):
                sys.exit("Not a CSV file")
            else:
                with open(sys.argv[1], "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        menu.append(row)
                break
        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()
