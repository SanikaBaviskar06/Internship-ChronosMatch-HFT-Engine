
class MatchingEngine:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    def add_order(self, order_id, side, price, quantity):
        order = {
            "order_id": order_id,
            "price": price,
            "quantity": quantity,
        }

        if side.upper() == "BUY":
            self.buy_orders.append(order)
        elif side.upper() == "SELL":
            self.sell_orders.append(order)
        else:
            print("Invalid order side")
            return

        self.match_orders()

    def match_orders(self):
        while self.buy_orders and self.sell_orders:
            buy = self.buy_orders[0]
            sell = self.sell_orders[0]

            if buy["price"] < sell["price"]:
                break

            traded_quantity = min(
                buy["quantity"], sell["quantity"]
            )

            print(
                f"Trade: BUY {buy['order_id']} / "
                f"SELL {sell['order_id']} | "
                f"Price: {sell['price']} | "
                f"Quantity: {traded_quantity}"
            )

            buy["quantity"] -= traded_quantity
            sell["quantity"] -= traded_quantity

            if buy["quantity"] == 0:
                self.buy_orders.pop(0)

            if sell["quantity"] == 0:
                self.sell_orders.pop(0)


def main():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "SELL", 99, 5)
    engine.add_order(3, "SELL", 100, 5)


if __name__ == "__main__":
    main()
