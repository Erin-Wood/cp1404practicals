numbers = []
for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# Output information about the numbers

print("The first number is:", numbers[0])
print("The last number is:", numbers[-1])
print("The smallest number is:", min(numbers))
print("The largest number is:", max(numbers))
print("The average of the numbers is:", sum(numbers) / len(numbers))

# 2. Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Enter your username: ")

if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")
