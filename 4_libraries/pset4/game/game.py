import random
import sys

def main():
    level = get_level("Level: ")
    integer = random.randint(1, level)
    print(integer)
    guess_integer(integer, "Guess: ")


def get_level(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level > 0:
                return level
            else:
                pass
        except ValueError:
            pass

def guess_integer(integer, prompt):
    while True:
        try:
            guess = int(input(prompt))
            if guess < 1:
                pass
            elif guess < integer:
                print("Too small!")
            elif guess > integer:
                print("Too large!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass


main()
