from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi simulator program."""
    print("Welcome to the Taxi Simulator!")

    # Create a list of taxis
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    total_bill = 0  # Initialize the total bill
    current_taxi = None  # No taxi selected at the start

    while True:
        print("\nMenu:")
        print("q) Quit")
        print("c) Choose taxi")
        print("d) Drive")
        choice = input("Choose an option: ").lower()

        if choice == "q":
            break
        elif choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                total_bill += drive_taxi(current_taxi)
            else:
                print("You need to choose a taxi before you can drive!")
        else:
            print("Invalid choice. Please choose again.")

        print(f"Total bill so far: ${total_bill:.2f}")

    print("\nGoodbye!")
    print(f"Your total trip cost: ${total_bill:.2f}")


def choose_taxi(taxis):
    """Let the user choose a taxi from the list."""
    print("\nAvailable taxis:")
    for i, taxi in enumerate(taxis):
        print(f"{i}. {taxi}")

    try:
        choice = int(input("Choose a taxi by its number: "))
        if 0 <= choice < len(taxis):
            print(f"You chose {taxis[choice].name}")
            return taxis[choice]
        else:
            print("Invalid choice. Please choose a valid taxi.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return None


def drive_taxi(taxi):
    """Drive the selected taxi and calculate the trip cost."""
    try:
        distance = int(input(f"How far would you like to drive the {taxi.name}? "))
        taxi.start_fare()  # Start a new fare
        taxi.drive(distance)  # Drive the taxi
        trip_cost = taxi.get_fare()
        print(f"Your trip cost: ${trip_cost:.2f}")
        return trip_cost
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0


if __name__ == "__main__":
    main()
