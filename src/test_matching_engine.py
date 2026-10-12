
from matching_engine import MatchingEngine


def test_matching_engine():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "SELL", 99, 5)

    assert len(engine.buy_orders) == 1
    assert engine.buy_orders[0]["quantity"] == 5
    assert len(engine.sell_orders) == 0

    print("Matching Engine Test Passed!")


if __name__ == "__main__":
    test_matching_engine()
