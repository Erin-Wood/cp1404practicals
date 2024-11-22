from prac_09.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    print("Testing the cars over several attempts...\n")
    for distance in range(1, 12):  # Loop through distances from 1 to 11 km
        print(f"Trying to drive {distance} km:")
        good_distance = good_car.drive(distance)
        bad_distance = bad_car.drive(distance)
        print(f"{good_car.name} drove {good_distance} km")
        print(f"{bad_car.name} drove {bad_distance} km\n")

    print("Final states of the cars:")
    print(good_car)
    print(bad_car)


main()
