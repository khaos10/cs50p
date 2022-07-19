import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()


def main():
    if verify_argv(sys.argv):
        text = input("Input: ")
        f = choice_font(sys.argv)
        figlet.setFont(font=f)
        print(f"Output:\n\n{figlet.renderText(text)}")


def verify_argv(argv):
    if len(argv) == 2 or len(argv) > 3:
        sys.exit("Invalid usage")
    elif len(argv) == 3:
        if not (argv[1] == "-f" or argv[1] == "--font") or not argv[2] in fonts:
            sys.exit("Invalid usage")
    return True


def choice_font(argv):
    if len(argv) == 1:
        return random.choice(fonts)
    else:
        return argv[2]


main()
