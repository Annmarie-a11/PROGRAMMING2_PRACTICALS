import random

# Updated constants :
MAX_INCREASE = 0.175  # 17.5% maximum price increase (was 10%)
MAX_DECREASE = 0.05
MIN_PRICE = 1.00      # Minimum allowed price (was $0.01, changed to $1.00)
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "stock_simulator_output.txt"

price = INITIAL_PRICE
number_of_days = 0

# Open file
out_file = open(FILENAME, 'w')

# Print  starting price to  file
starting_message = f"Starting price: ${price:,.2f}"
print(starting_message)
print(starting_message, file=out_file)

#  loop runs while the price is within the allowed bounds
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1  # Increment the day counter

    # generate random integer of 1 or 2 (50% chance)
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)

    # Pint daily price update to the console and file
    daily_message = f"On day {number_of_days} price is: ${price:,.2f}"
    print(daily_message)
    print(daily_message, file=out_file)

# Close the  file
out_file.close()
