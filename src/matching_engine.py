
import heapq


class MatchingEngine:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []
        self.sequence = 0
        self.trades = []
        self.order_ids = set()

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

        if order_id in self.order_ids:
            raise ValueError("Order ID already exists")

        self.order_ids.add(order_id)
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

    def cancel_order(self, order_id):
        for index, item in enumerate(self.buy_orders):
            if item[2]["order_id"] == order_id:
                self.buy_orders.pop(index)
                heapq.heapify(self.buy_orders)
                return True

        for index, item in enumerate(self.sell_orders):
            if item[2]["order_id"] == order_id:
                self.sell_orders.pop(index)
                heapq.heapify(self.sell_orders)
                return True

        return False

    def get_order_book(self):
        buy_orders = [
            {
                "order_id": item[2]["order_id"],
                "price": item[2]["price"],
                "quantity": item[2]["quantity"],
            }
            for item in sorted(self.buy_orders)
        ]

        sell_orders = [
            {
                "order_id": item[2]["order_id"],
                "price": item[2]["price"],
                "quantity": item[2]["quantity"],
            }
            for item in sorted(self.sell_orders)
        ]

        return {
            "buy_orders": buy_orders,
            "sell_orders": sell_orders,
        }

    def get_order_book_summary(self):
        order_book = self.get_order_book()

        buy_count = len(order_book["buy_orders"])
        sell_count = len(order_book["sell_orders"])

        return {
            "buy_orders_count": buy_count,
            "sell_orders_count": sell_count,
            "total_orders": buy_count + sell_count,
        }

    
    def get_best_buy_price(self):
        if not self.buy_orders:
            return None

        return -self.buy_orders[0][0]

    def get_best_sell_price(self):
        if not self.sell_orders:
            return None

        return self.sell_orders[0][0]


    def get_trade_history(self):
        return [trade.copy() for trade in self.trades]

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

    print("\nOrder Book Summary:")
    print(engine.get_order_book_summary())

    print("\nTrade History:")
    for trade in engine.get_trade_history():
        print(trade)


def test_get_best_buy_and_sell_price():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "BUY", 101, 5)

    engine.add_order(3, "SELL", 105, 4)
    engine.add_order(4, "SELL", 103, 6)

    assert engine.get_best_buy_price() == 101
    assert engine.get_best_sell_price() == 103


def test_best_price_when_order_book_is_empty():
    engine = MatchingEngine()

    assert engine.get_best_buy_price() is None
    assert engine.get_best_sell_price() is None


if __name__ == "__main__":
    main()