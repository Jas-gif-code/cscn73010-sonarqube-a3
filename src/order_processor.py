import hashlib


def calculate_order_total(items, discount_amount=0.0, tax_rate=0.13):
    subtotal = 0.0
    for item in items:
        price = item.get("price", 0)
        qty = item.get("qty", 0)
        if price > 0 and qty > 0:
            subtotal += price * qty

    if discount_amount < 0:
        raise ValueError("Discount amount cannot be negative.")
    subtotal = max(0.0, subtotal - discount_amount)

    total = subtotal * (1 + tax_rate)
    return round(total, 2)


def generate_receipt_hash(order_id):
    return hashlib.sha256(str(order_id).encode("utf-8")).hexdigest()