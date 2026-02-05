from bot.orders import place_trade
from bot.validators import validate_symbol, validate_side, validate_quantity

def menu():
    print("\n" + "=" * 40)
    print("🚀 BINANCE SPOT TESTNET BOT")
    print("=" * 40)
    print("1️⃣  Market Order")
    print("2️⃣  Limit Order")
    print("3️⃣  Exit")


def get_input(prompt, cast=str):
    while True:
        try:
            return cast(input(prompt))
        except ValueError:
            print("❌ Invalid input")


def main():
    while True:
        menu()
        choice = get_input("Select option (1-3): ", int)

        if choice == 3:
            print("👋 Goodbye")
            break

        symbol = validate_symbol(get_input("Symbol: "))
        side = validate_side(get_input("Side (BUY/SELL): ").upper())
        quantity = validate_quantity(get_input("Quantity: ", float))

        if choice == 1:
            order_type = "MARKET"
            price = None

        elif choice == 2:
            order_type = "LIMIT"
            price = get_input("Limit Price: ", float)

        else:
            print("Invalid choice")
            continue

        print("\nOrder Summary")
        print(symbol, side, order_type, quantity, price)

        confirm = input("Confirm? (y/n): ").strip().lower()
        if confirm != "y":
            print("❌ Order cancelled")
            continue


        response = place_trade(
            symbol, side, order_type, quantity, price
        )
        print("Order placed successfully!")
        print(response)


if __name__ == "__main__":
    main()
