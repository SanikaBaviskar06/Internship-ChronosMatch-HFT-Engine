
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


def test_duplicate_order_id():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 5)

    try:
        engine.add_order(1, "SELL", 100, 5)
        assert False, "Duplicate order ID should be rejected"
    except ValueError as error:
        assert str(error) == "Order ID already exists"


def test_cancel_buy_order():
    engine = MatchingEngine()
    engine.add_order(1, "BUY", 100, 5)

    result = engine.cancel_order(1)

    assert result is True
    assert len(engine.buy_orders) == 0


def test_cancel_sell_order():
    engine = MatchingEngine()
    engine.add_order(2, "SELL", 105, 5)

    result = engine.cancel_order(2)

    assert result is True
    assert len(engine.sell_orders) == 0


def test_cancel_non_existing_order():
    engine = MatchingEngine()

    result = engine.cancel_order(999)

    assert result is False

def test_get_order_book():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 5)
    engine.add_order(2, "SELL", 110, 3)

    order_book = engine.get_order_book()

    assert len(order_book["buy_orders"]) == 1
    assert len(order_book["sell_orders"]) == 1

    assert order_book["buy_orders"][0]["order_id"] == 1
    assert order_book["sell_orders"][0]["order_id"] == 2


def test_get_trade_history():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "SELL", 100, 4)

    history = engine.get_trade_history()

    assert len(history) == 1
    assert history[0]["buy_order_id"] == 1
    assert history[0]["sell_order_id"] == 2
    assert history[0]["quantity"] == 4

    history[0]["quantity"] = 999
    assert engine.trades[0]["quantity"] == 4


def test_get_order_book_summary():
    engine = MatchingEngine()

    engine.add_order(1, "BUY", 100, 10)
    engine.add_order(2, "BUY", 99, 5)
    engine.add_order(3, "SELL", 110, 4)

    summary = engine.get_order_book_summary()

    assert summary["buy_orders_count"] == 2
    assert summary["sell_orders_count"] == 1
    assert summary["total_orders"] == 3
