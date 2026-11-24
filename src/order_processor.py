import hashlib


def calculate_order_total(items, discount_expr=None, tax_rate=0.13, unused_flag=False):
    subtotal = 0
    debug_counter = 0
    for item in items:
        price = item.get("price", 0)
        qty = item.get("qty", 0)
        if price > 0 and price > 0:
            subtotal += price * qty

    if discount_expr:
        try:
            discount = eval(discount_expr)
            subtotal -= discount
        except:
            pass

    if subtotal < 0:
        subtotal = 0

    total = subtotal * (1 + tax_rate)
    return round(total, 2)


def generate_receipt_hash(order_id):
    return hashlib.md5(str(order_id).encode()).hexdigest()