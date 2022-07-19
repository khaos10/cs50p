import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level)
        error_count = 0
        while error_count < 3:
            answer = int(input(f"{x} + {y} = "))
            if answer != (x + y):
                error_count += 1
                print("EEE")
            else:
                score += 1
                break
        if error_count == 3:
            print(f"{x} + {y} = {x + y}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        min = 0
        max = 9
    elif level == 2:
        min = 10
        max = 99
    elif level == 3:
        min = 100
        max = 999
    else:
        raise ValueError
    x = random.randint(min, max)
    y = random.randint(min, max)
    return x, y


if __name__ == "__main__":
    main()
