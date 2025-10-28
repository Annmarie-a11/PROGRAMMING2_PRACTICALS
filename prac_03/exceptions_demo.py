"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# 1. When will a ValueError occur?
# The `ValueError` exception is raised whenever the user inputs text for either the numerator or the denominator that cannot be successfully interpreted as a whole number by the `int()` function.

# 2. When will a ZeroDivisionError occur?
# A `ZeroDivisionError` will be encountered precisely when the code attempts the arithmetic operation and the user has input the value of zero (`0`) for the denominator, leading to an impossible or undefined mathematical result.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# It is indeed possible to proactively prevent the `ZeroDivisionError` .
# This can be achieved by implementing an **input validation loop** that forces the user to re-enter the denominator repeatedly until a value other than zero is provided.

try:
    # 3. Modification: The numerator input remains the same.
    numerator = int(input("Enter the numerator: "))

    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero! Please enter a non-zero number.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:

    print("Cannot divide by zero!")
print("Finished.")

