def main():
    file_name = input("File name: ")
    print(verify_suffix(file_name))


def verify_suffix(name):
    formatted_name = name.strip().lower()

    if formatted_name.endswith(".gif"):
        return "image/gif"
    elif formatted_name.endswith(".jpg") or formatted_name.endswith(".jpeg"):
        return "image/jpeg"
    elif formatted_name.endswith(".png"):
        return "image/png"
    elif formatted_name.endswith(".pdf"):
        return "application/pdf"
    elif formatted_name.endswith(".txt"):
        return "text/plain"
    elif formatted_name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


main()
