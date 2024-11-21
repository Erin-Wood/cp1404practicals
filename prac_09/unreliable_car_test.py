from unreliable_car import UnreliableCar


def main():
    car1 = UnreliableCar("Almost Always Reliable", 100, 90)
    car2 = UnreliableCar("Somewhat Reliable", 100, 50)
    car3 = UnreliableCar("Unreliable", 100, 10)

    print(f"Attempting to drive 40 km with '{car1.name}'")
    print(f"Distance driven: {car1.drive(40)} km")
    print(car1)

    print(f"\nAttempting to drive 40 km with '{car2.name}'")
    print(f"Distance driven: {car2.drive(40)} km")
    print(car2)

    print(f"\nAttempting to drive 40 km with '{car3.name}'")
    print(f"Distance driven: {car3.drive(40)} km")
    print(car3)


if __name__ == "__main__":
    main()
