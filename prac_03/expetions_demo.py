try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # check if the denominator is zero
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Please enter a valid denominator"))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Answer the following questions:
# 1. When will a ValueError occur?
# Will occur if the user inputs something that can't become an integer (letters or symbols instead of numbers)

# 2. When will a ZeroDivisionError occur?
# Occurs if the denominator is 0.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Can change the code to check if the denominator is 0 before attempting the division.
