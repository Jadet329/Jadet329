def main():

    amount_due = 50

    while amount_due > 0:
        print(f"amount Due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            continue

        if coin in [25, 10, 5]:
            amount_due -= coin

    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
