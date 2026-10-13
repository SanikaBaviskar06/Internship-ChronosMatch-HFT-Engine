import heapq


class MatchingEngine:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []
        self.sequence = 0
        self.trades = []

    def add_order(self, order_id, side, price, quantity):
        if not isinstance(side, str):
            raise ValueError("Side must be BUY or SELL")

        side = side.upper()

        if side not in ("BUY", "SELL"):
            raise ValueError("Side must be BUY or SELL")

        if (
            not isinstance(price, (int, float))
            or isinstance(price, bool)
            or price <= 0
        ):
            raise ValueError("Price must be a positive number")

        if (
            not isinstance(quantity, int)
            or isinstance(quantity, bool)
            or quantity <= 0
        ):
            raise ValueError("Quantity must be a positive integer")

        self.sequence += 1

        order = {
            "order_id": order_id,
            "price": price,
            "quantity": quantity,
            "sequence": self.sequence,
        }

        if side == "BUY":
            heapq.heappush(
                self.buy_orders,
                (-price, self.sequence, order)
            )
        else:
            heapq.heappush(
                self.sell_orders,
                (price, self.sequence, order)
            )

        self.match_orders()

    def match_orders(self):
        while self.buy_orders and self.sell_orders:
            buy_price, _, buy = self.buy_orders[0]
            sell_price, _, sell = self.sell_orders[0]

            if -buy_price < sell_price:
                break

            traded_quantity = min(
                buy["quantity"],
                sell["quantity"]
            )

            trade = {
                "buy_order_id": buy["order_id"],
                "sell_order_id": sell["order_id"],
                "price": sell["price"],
                "quantity": traded_quantity,
            }

            self.trades.append(trade)

            print(
                f"Trade: BUY {buy['order_id']} / "
                f"SELL {sell['order_id']} | "
                f"Price: {sell['price']} | "
                f"Quantity: {traded_quantity}"
            )

            buy["quantity"] -= traded_quantity
            sell["quantity"] -= traded_quantity

            if buy["quantity"] == 0:
                heapq.heappop(self.buy_orders)

            if sell["quantity"] == 0:
                heapq.heappop(self.sell_orders)


def main():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "BUY", 101, 5)
    engine.add_order(3, "SELL", 100, 3)
    engine.add_order(4, "SELL", 101, 5)

    print("\nTrade History:")
    for trade in engine.trades:
        print(trade)


if __name__ == "__main__":
    main()