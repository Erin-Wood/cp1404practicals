# Task 1
name = input("What is your name? ")
out_file = open("name.txt", "w")
out_file.writelines([name])
out_file.close()

# Task 2
in_file = open("name.txt", "r")
name = in_file.read().strip()  # Use .strip() to remove any extra newline characters
in_file.close()

print(f"Hi {name}!")

# Task 3
with open("numbers.txt", "r") as file:
    number1 = int(file.readline())
    number2 = int(file.readline())

result = number1 + number2
print(result)

# Task 4
total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        total += number

print(total)
