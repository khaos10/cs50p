def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    shorten_word = word

    for char in word:
        if char.lower() in (vowels):
            shorten_word = shorten_word.replace(char, "")

    return shorten_word


if __name__ == "__main__":
    main()
