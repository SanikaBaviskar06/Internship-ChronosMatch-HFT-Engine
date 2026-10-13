
from matching_engine import MatchingEngine


def test_price_time_priority():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 5)
    engine.add_order(2, "BUY", 100, 5)
    engine.add_order(3, "SELL", 100, 7)

    assert len(engine.buy_orders) == 1
    assert engine.buy_orders[0]["order_id"] == 2
    assert engine.buy_orders[0]["quantity"] == 3


def test_sell_price_priority():
    engine = MatchingEngine()

    engine.add_order(1, "SELL", 105, 5)
    engine.add_order(2, "SELL", 100, 5)

    assert engine.sell_orders[0]["order_id"] == 2


def test_invalid_orders():
    engine = MatchingEngine()

    try:
        engine.add_order(1, "BUY", -100, 5)
        assert False, "Negative price should be rejected"
    except ValueError:
        pass

    try:
        engine.add_order(2, "SELL", 100, 0)
        assert False, "Zero quantity should be rejected"
    except ValueError:
        pass


def test_buy_order_priority():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 5)
    engine.add_order(2, "BUY", 105, 5)
    engine.add_order(3, "BUY", 102, 5)

    assert engine.buy_orders[0]["order_id"] == 2
    assert engine.buy_orders[1]["order_id"] == 3
    assert engine.buy_orders[2]["order_id"] == 1

    print("Buy Order Priority Test Passed!")


def test_sell_order_priority():
    engine = MatchingEngine()

    engine.add_order(1, "SELL", 105, 5)
    engine.add_order(2, "SELL", 95, 5)
    engine.add_order(3, "SELL", 100, 5)

    assert engine.sell_orders[0]["order_id"] == 2
    assert engine.sell_orders[1]["order_id"] == 3
    assert engine.sell_orders[2]["order_id"] == 1

    print("Sell Order Priority Test Passed!")


def test_partial_order_matching():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "SELL", 100, 4)

    assert len(engine.buy_orders) == 1
    assert engine.buy_orders[0]["quantity"] == 6
    assert len(engine.sell_orders) == 0


def test_partial_order_matching():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "SELL", 100, 4)

    assert len(engine.buy_orders) == 1
    assert engine.buy_orders[0]["quantity"] == 6
    assert len(engine.sell_orders) == 0


def test_trade_history():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "SELL", 100, 4)

    assert len(engine.trades) == 1
    assert engine.trades[0]["buy_order_id"] == 1
    assert engine.trades[0]["sell_order_id"] == 2
    assert engine.trades[0]["price"] == 100
    assert engine.trades[0]["quantity"] == 4
