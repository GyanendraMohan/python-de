import pandas as pd 

df = pd.read_csv("dirty_orders.csv")
print(df)

df["amount"] = df["amount"].fillna(0)
# print("after fillna")
# print(df)   

# typecasing amount column to int
df["amount"] = df["amount"].astype(int)

df["country"] = df["country"].str.lower()
#print("after typecasting and uppercasing")
# print(df)

# groupby and aggregation 

country_summary = (
    df.groupby("country")
    .agg(
        total_amount = ("amount", "sum")
    )
)

print("country summary")
print(country_summary)