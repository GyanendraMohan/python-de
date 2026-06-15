# flattening
def transform_orders(raw_orders):
    transformed = []
    for order in raw_orders:
        transformed.append({
            "order_id": order["order_id"],
            "amount": float(order["amount"]),
            "country": order["country"].upper()
        })
    return transformed

sample_orders = [
    {"order_id" : 1, "amount": "100", "country" : "usa"},
    {"order_id" : 2 , "amount" : 200, "country" : "India"}
]

transformed = transform_orders(sample_orders)
print(transformed)