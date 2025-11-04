"""
CP1404/CP5632 Practical
Hexadecimal colour lookup program
"""

# Constant dictionary of 12 colour names and their hex codes.
NAME_TO_CODE = {
    "AliceBlue": "#f0f8ff",
    "Acid Green": "##b0bf1a",
    "Bubble Gum": "##ffc1cc",
    "Burnt Orange": "##cc5500",
    "Camel": "##c19a6b",
    "Dark Sky Blue": "#8cbed6",
    "Grey27": "#454545",
    "Ginger": "#b06500",
    "Maroon": "#b03060",
    "GhostWhite": "#f8f8ff"
}

# Print all available colours for the user
print("Available Colours:")
for name, code in NAME_TO_CODE.items():
    print(f"{name:<10} is {code}")


color_name = input("\nEnter colour name: ").title()

while color_name != "":

    try:
        # Look up the color code
        code = NAME_TO_CODE[color_name]
        print(f"The code for {color_name} is {code}")

    except KeyError:

        print("Invalid colour name")


    color_name = input("Enter colour name: ").title()

print("End of the Program")