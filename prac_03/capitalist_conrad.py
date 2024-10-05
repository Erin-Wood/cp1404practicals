"""
Stock Price Simulator
- The stock starts at $10.00.
- Each day, there's a 50% chance the price goes up by up to 10%,
  or a 50% chance it goes down by up to 5%.
- The simulation stops when the price is over $1000 or under $0.01.
- Prices are shown with 2 decimal places (e.g. $33.59).
"""

import random

MAX_INCREASE = 0.1
MAX_DECREASE = 0.05
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
FILENAME = "stock_output.txt"

out_file = open(FILENAME, 'w')

price = INITIAL_PRICE
day = 0

print(f"Starting price: ${price:.2f}", file=out_file)


while MIN_PRICE <= price <= MAX_PRICE:
    day += 1

    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)

    print(f"On day {day}, the price is: ${price:.2f}", file=out_file)

out_file.close()
