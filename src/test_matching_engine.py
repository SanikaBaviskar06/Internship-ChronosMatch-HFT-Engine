
from matching_engine import MatchingEngine


def test_price_time_priority():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 5)
    engine.add_order(2, "BUY", 100, 5)
    engine.add_order(3, "SELL", 100, 7)

    assert len(engine.buy_orders) == 1
    assert engine.buy_orders[0]["order_id"] == 2
    assert engine.buy_orders[0]["quantity"] == 3

    print("Price-Time Priority Test Passed!")


def test_sell_price_priority():
    engine = MatchingEngine()

    engine.add_order(1, "SELL", 105, 5)
    engine.add_order(2, "SELL", 100, 5)

    assert engine.sell_orders[0]["order_id"] == 2

    print("Sell Price Priority Test Passed!")


if __name__ == "__main__":
    test_price_time_priority()
    test_sell_price_priority()
