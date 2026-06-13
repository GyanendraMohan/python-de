orders = [
    {"order_id":1, "country": "USA"},
    {"order_id":2, "country": "INDIA"},
    {"order_id":3, "country": "NEPAL"},
    {"order_id":4, "country": "ENGLAND"},
    {"order_id":5, "country": "INDIA"},
]

in_orders = []

for order in orders:
    if order["country"] == "INDIA":
        in_orders.append(order)
print(in_orders)