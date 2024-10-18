COLOR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "Bistre": "#3d2b1f",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "Bone": "#e3dac9",
    "Boysenberry": "#873260"
}

color_name = input("Enter color name: ").title()  # Convert to title case
while color_name != "":
    try:
        print(f"{color_name} has the code {COLOR_TO_HEX[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").title()  # Convert to title case

print("Program exited.")
