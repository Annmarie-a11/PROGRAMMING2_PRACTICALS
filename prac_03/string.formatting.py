"""
CP1404/CP5632 - Practical
String formatting examples and tasks
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# Things to do: f-string with currency formatting
print(f"{year} {name} for about ${cost:,.0f}!")

# Things to do: Make powers of 2
for i in range(11):  # 0 → 10
    print(f"2 ^ {i:2} is {2 ** i:4}")
