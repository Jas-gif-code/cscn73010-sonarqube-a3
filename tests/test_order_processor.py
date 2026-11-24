from src.order_processor import calculate_order_total


def test_basic_order():
    items = [{"price": 10.0, "qty": 2}, {"price": 5.0, "qty": 1}]
    assert calculate_order_total(items) == 28.25