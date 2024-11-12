"""
guitars.py
This program allows the user to enter multiple guitars and displays each guitar's details.

Module: guitars.py
Estimated time to complete: 50 minutes
Current time: 11am
Time to complete: 1 hours (including guitar.py, guitar_test.py)

"""

from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
