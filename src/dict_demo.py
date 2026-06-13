raw_api_response = {
  "orderId": "ORD001",
  "customer": {
    "id": "CUST101",
    "name": "Gyanendra Mohan Patel"
  },
  "country": {
    "code": "US",
    "name": "United States",
    "currency": "USD"
  },
  "items": [
    {
      "id": "ITEM001",
      "name": "Laptop",
      "quantity": 1,
      "price": 65000
    },
    {
      "id": "ITEM002",
      "name": "Mouse",
      "quantity": 2,
      "price": 500
    },
    {
      "id": "ITEM003",
      "name": "Keyboard",
      "quantity": 1,
      "price": 1500
    }
  ]
}

structured_orders = {
    "order_id" : raw_api_response["orderId"], 
    "customer_id" : raw_api_response["customer"]["id"],
    "customer_name" : raw_api_response["customer"]["name"], 
    "total_amount" :  sum(item["price"] for item in raw_api_response["items"])
}

print(structured_orders)