import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

number_of_picks = int(input("How many quick picks? "))

for _ in range(number_of_picks):

    quick_pick = random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_PICK)

    quick_pick.sort()

    print(" ".join(f"{number:2}" for number in quick_pick))
