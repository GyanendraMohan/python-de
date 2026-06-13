import csv

# list of lists
rows = [
  ["order_id", "customer", "amount", "country"],
  ["1", "John Doe", 2500, "US"],
  ["2", "Alice Smith", 1800, "CA"],
  ["3", "Bob Johnson", 3200, "US"],
  ["4", "Emma Brown", 1500, "UK"],
  ["5", "Michael Lee", 2750, "AU"]
]

# write CSV to a file named orders.csv
with open("orders.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)