def main():
    m = int(input("m: "))
    to_joules(m)


def to_joules(mass):
    e = mass * pow(300000000, 2)
    print(f"E: {e}")


main()
