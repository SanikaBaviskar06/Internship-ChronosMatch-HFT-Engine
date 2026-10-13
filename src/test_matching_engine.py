from matching_engine import MatchingEngine


def test_price_time_priority():
    engine = MatchingEngine()
    engine.add_order(1, "BUY", 100, 5)
    engine.add_order(2, "BUY", 100, 5)
    engine.add_order(3, "SELL", 100, 7)

    assert len(engine.buy_orders) == 1
    assert engine.buy_orders[0][2]["order_id"] == 2
    assert engine.buy_orders[0][2]["quantity"] == 3


def test_sell_price_priority():
    engine = MatchingEngine()
    engine.add_order(1, "SELL", 105, 5)
    engine.add_order(2, "SELL", 100, 5)

    assert engine.sell_orders[0][2]["order_id"] == 2


def test_order_validation():
    engine = MatchingEngine()

    try:
        engine.add_order(1, "INVALID", 100, 5)
        assert False
    except ValueError:
        pass

    try:
        engine.add_order(2, "BUY", -10, 5)
        assert False
    except ValueError:
        pass

    try:
        engine.add_order(3, "BUY", 100, 0)
        assert False
    except ValueError:
        pass


def test_buy_order_priority():
    engine = MatchingEngine()
    engine.add_order(1, "BUY", 100, 5)
    engine.add_order(2, "BUY", 105, 5)
    engine.add_order(3, "BUY", 102, 5)

    assert engine.buy_orders[0][2]["order_id"] == 2


def test_sell_order_priority():
    engine = MatchingEngine()
    engine.add_order(1, "SELL", 105, 5)
    engine.add_order(2, "SELL", 95, 5)
    engine.add_order(3, "SELL", 100, 5)

    assert engine.sell_orders[0][2]["order_id"] == 2


def test_trade_history():
    engine = MatchingEngine()
    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "SELL", 100, 4)

    assert len(engine.trades) == 1
    assert engine.trades[0]["buy_order_id"] == 1
    assert engine.trades[0]["sell_order_id"] == 2
    assert engine.trades[0]["quantity"] == 4


def test_partial_order_matching():
    engine = MatchingEngine()
    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "SELL", 100, 4)

    assert len(engine.buy_orders) == 1
    assert engine.buy_orders[0][2]["quantity"] == 6
    assert len(engine.sell_orders) == 0


def test_no_match_when_prices_do_not_cross():
    engine = MatchingEngine()
    engine.add_order(1, "BUY", 90, 5)
    engine.add_order(2, "SELL", 100, 5)

    assert len(engine.trades) == 0
    assert len(engine.buy_orders) == 1
    assert len(engine.sell_orders) == 1


def test_one_order_matches_multiple_orders():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "SELL", 100, 4)
    engine.add_order(3, "SELL", 100, 3)

    assert len(engine.trades) == 2
    assert engine.trades[0]["quantity"] == 4
    assert engine.trades[1]["quantity"] == 3

    assert len(engine.buy_orders) == 1
    assert engine.buy_orders[0][2]["quantity"] == 3
    assert len(engine.sell_orders) == 0


def test_invalid_zero_price():
    engine = MatchingEngine()

    try:
        engine.add_order(1, "BUY", 0, 5)
        assert False, "Zero price should be rejected"
    except ValueError:
        pass


def test_multiple_partial_matches():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "SELL", 100, 6)

    assert len(engine.trades) == 1
    assert engine.trades[0]["quantity"] == 6
    assert len(engine.buy_orders) == 1
    assert engine.buy_orders[0][2]["quantity"] == 4
