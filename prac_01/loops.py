# odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. Count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()  # Move to the next line after printing the numbers

# b. Count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()  # Move to the next line after printing the numbers

# c. Print n stars on one line
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()  # Move to the next line after printing the stars

# d. Print n lines of increasing stars
for i in range(1, number_of_stars + 1):
    print('*' * i)  # Print i stars on each line

