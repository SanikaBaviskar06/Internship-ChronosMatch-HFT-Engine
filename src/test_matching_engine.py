
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


if __name__ == "__main__":
    test_price_time_priority()
