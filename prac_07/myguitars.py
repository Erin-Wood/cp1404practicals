import csv
from guitar import Guitar

def main():
    """Manage a list of guitars, allowing users to view, sort, and add to the collection."""
    guitars = load_guitars("guitars.csv")
    print("Guitars loaded:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    add_new_guitars(guitars)

    save_guitars("guitars.csv", guitars)
    print("New guitar(s) saved to guitars.csv.")

def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row[0], int(row[1]), float(row[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    """Display a list of Guitar objects."""
    for guitar in guitars:
        print(guitar)

def add_new_guitars(guitars):
    """Prompt user to add new guitars, appending them to the guitars list."""
    print("\nAdd new guitars (leave name blank to stop):")
    while True:
        name = input("Name: ")
        if not name:
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"{new_guitar} added.")
        except ValueError:
            print("Invalid input; please enter a valid year and cost.")

def save_guitars(filename, guitars):
    """Write all guitars to a CSV file."""
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == "__main__":
    main()
