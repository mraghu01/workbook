import random

def create_multiplication_steps():
    # Generate a random 3-digit and a 2-digit number
    three_digit_number = random.randint(100, 999)
    two_digit_number = random.randint(10, 99)

    # Round the numbers to the nearest hundred and ten
    rounded_three_digit = round(three_digit_number, -2)
    rounded_two_digit = round(two_digit_number, -1)

    # Calculate the steps
    steps = [
        (rounded_three_digit, rounded_two_digit),
        # Fix: Adjust the second step to round to the nearest ten instead of hundred
        (round(three_digit_number, -1), rounded_two_digit),
        (three_digit_number, rounded_two_digit),
        (three_digit_number, two_digit_number)
    ]

    # Print the steps
    for step in steps:
        print(f"{step[0]} * {step[1]} = ____")

# Create and print 2 random examples
for _ in range(2):
    create_multiplication_steps()
    print()  # Print a blank line between examples

