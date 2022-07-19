def main():
    answer = input(
        "What is the Answer to the Great Question of Life, the Universe and Everything? ")

    if verify_answer(answer):
        print("Yes")
    else:
        print("No")


def verify_answer(a):
    formatted_answer = a.strip().lower()
    return formatted_answer == "42" or formatted_answer == "forty-two" or formatted_answer == "forty two"


main()
