from os.path import splitext
import sys

from PIL import Image, ImageOps

extensions = [".jpg", ".jpeg", ".png"]


def main():
    veryfy_input()
    with Image.open("shirt.png") as shirt:
        size = shirt.size
        with Image.open(sys.argv[1]) as photo:
            photo = ImageOps.fit(photo, size)
            photo.paste(shirt, shirt)
            photo.save(sys.argv[2])


def veryfy_input():
    while True:
        try:
            if len(sys.argv) < 3:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 3:
                sys.exit("Too many command-line arguments")
            else:
                input_root, input_ext = splitext(sys.argv[1])
                output_root, output_ext = splitext(sys.argv[2])
                input_ext.lower()
                output_ext.lower()
                if not input_ext in extensions:
                    sys.exit("Invalid input")
                elif not output_ext in extensions:
                    sys.exit("Invalid output")
                elif input_ext != output_ext:
                    sys.exit("Input and output have different extensions")
                else:
                    break
        except FileNotFoundError:
            sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
