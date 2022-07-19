def main():
    text = input("Input a message with emoticons!\n")
    convert(text)


def convert(text):
    text_converted = text.replace(":)", "🙂").replace(":(", "🙁")
    print(text_converted)


main()
