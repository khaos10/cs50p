def main():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
            if item in grocery_list:
                count = grocery_list.get(item)
                count += 1
                grocery_list[item] = count
            else:
                grocery_list[item] = 1
        except EOFError:
            print()
            sorted_items = sorted(grocery_list)
            for item in sorted_items:
                count = grocery_list.get(item)
                print(f"{ count } { item }")
            break
        except KeyError:
            pass


main()
