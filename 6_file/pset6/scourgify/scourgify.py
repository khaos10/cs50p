import csv
import sys

students = []


def main():
    get_students()
    new_students_list = split_name(students)
    write_to_file(new_students_list)


def get_students():
    while True:
        try:
            if len(sys.argv) < 3:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 3:
                sys.exit("Too many command-line arguments")
            elif not sys.argv[1].endswith(".csv"):
                sys.exit(f"Could not read {sys.argv[1]}")
            else:
                with open(sys.argv[1], "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        students.append(row)
                break
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


def split_name(students):
    new_students_list = []
    for student in students:
        last, first = student["name"].split(", ")
        new_student = {"first": first, "last": last, "house": student["house"]}
        new_students_list.append(new_student)
    return new_students_list


def write_to_file(list):
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in list:
            writer.writerow(
                {"first": student["first"], "last": student["last"], "house": student["house"]})


if __name__ == "__main__":
    main()
