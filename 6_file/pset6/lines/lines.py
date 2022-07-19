import sys


def main():
    file = open_file()
    count = count_lines(file)
    file.close()
    print(count)


def open_file():
    while True:
        try:
            if len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")
            elif not sys.argv[1].endswith(".py"):
                sys.exit("Not a Python file")
            else:
                return open(sys.argv[1], "r")
        except FileNotFoundError:
            sys.exit("File does not exist")


def count_lines(file):
    count = 0
    for line in file:
        formatted_line = line.lstrip()
        if not formatted_line:
            pass
        elif formatted_line.startswith("#"):
            pass
        else:
            count += 1
    return count


if __name__ == "__main__":
    main()
