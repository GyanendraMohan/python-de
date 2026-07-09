# try:
#     with open("missng_file.csv", "r") as f:
#         data = f.read()
# except FileNotFoundError as e:
#     print(f"Error: {e}")
# finally:
#     print("cleanup complete")

with open("missing_file.csv", "r") as f:
    data = f.read()