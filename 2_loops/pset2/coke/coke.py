def main():
    get_coin(50)


def get_coin(amount):

    while True:
        print(f"Amount due: {amount}")
        coin = int(input("Insert coin: "))

        if coin == 5 or coin == 10 or coin == 25:
            amount -= coin

        if amount <= 0:
            print(f"Change owed: {abs(amount)}")
            break

main()
