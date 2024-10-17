"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformatted dictionary to follow PEP 8 convention
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

# Print the dictionary contents (for debugging purposes)
print(CODE_TO_NAME)

# Input loop allowing case-insensitive input (e.g., "qld" or "QLD")
state_code = input("Enter short state: ").upper()  # Convert to uppercase
while state_code != "":
    try:
        # Try to access the state name using EAFP approach
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        # Handle the case where the state code is not found
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()  # Convert to uppercase

# Print all states and names neatly lined up
print("\nAll states and their names:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:<3} is {name}")
