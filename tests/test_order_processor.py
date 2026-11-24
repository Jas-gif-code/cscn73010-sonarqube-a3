import pytest
from src.order_processor import calculate_order_total, generate_receipt_hash


def test_basic_order():
    items = [{"price": 10.0, "qty": 2}, {"price": 5.0, "qty": 1}]
    assert calculate_order_total(items) == 28.25


def test_order_with_discount():
    items = [{"price": 50.0, "qty": 1}]
    assert calculate_order_total(items, discount_amount=10.0) == 45.2


def test_discount_exceeding_subtotal_floors_at_zero():
    items = [{"price": 10.0, "qty": 1}]
    assert calculate_order_total(items, discount_amount=25.0) == 0.0


def test_negative_discount_raises_error():
    items = [{"price": 10.0, "qty": 1}]
    with pytest.raises(ValueError):
        calculate_order_total(items, discount_amount=-5.0)


def test_ignores_non_positive_price_or_qty():
    items = [
        {"price": -5.0, "qty": 2},
        {"price": 10.0, "qty": -1},
        {"price": 10.0, "qty": 1},
    ]
    assert calculate_order_total(items) == 11.3


def test_generate_receipt_hash():
    digest = generate_receipt_hash("ORD-1001")
    assert len(digest) == 64