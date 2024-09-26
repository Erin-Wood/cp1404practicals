total = 0
number_of_items = int(input("Number of items: "))

# Validate input to ensure number of items is not negative
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Calculate total price
for i in range(number_of_items):
    price = float(input(f"Price of item {i + 1}: "))
    total += price

# Apply 10% discount if total is greater than $100
if total > 100:
    total *= 0.9  # 10% discount

# Output total price with f-string formatting
print(f"Total price for {number_of_items} items is ${total:.2f}")
