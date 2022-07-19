def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if start_with_2_letters(s) and contain_2_to_6_letters(s) and numbers_at_end(s) and no_symbol(s):
        return True
    else:
        return False


def start_with_2_letters(s):
    if s[0:2].isalpha():
        return True
    else:
        return False


def contain_2_to_6_letters(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


def numbers_at_end(s):
    if s.isalpha():
        return True
    else:
        for i in range(len(s)):
            if s[i].isnumeric():
                if s[i] == "0":
                    return False
                elif not s[i:len(s)].isnumeric():
                    return False
                else:
                    return True


def no_symbol(s):
    for char in s:
        if not char.isalnum():
            return False
    return True


if __name__ == "__main__":
    main()
