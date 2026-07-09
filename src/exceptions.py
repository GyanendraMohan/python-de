# try:
#     with open("missng_file.csv", "r") as f:
#         data = f.read()
# except FileNotFoundError as e:
#     print(f"Error: {e}")
# finally:
#     print("cleanup complete")

# with open("missing_file.csv", "r") as f:
#     data = f.read()

try:
    amout = "100"
    total = amout + 50
except TypeError as e:
    print(f"Error: {e}")
    amount = int("100")
    total = amount + 50
    print("\nAfter conversion\n")
    print(f"Total: {total}\n")
finally:
    print("cleanup complete\n")