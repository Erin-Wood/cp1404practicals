
class Car:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel

    def add_fuel(self, amount):
        if amount > 0:
            self.fuel += amount

    def drive(self, distance):
        fuel_needed = distance / 10
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
        else:
            print("Not enough fuel!")

    def __str__(self):
        return f"{self.name} - Fuel: {self.fuel}"


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)


main()

# Create a new Car object called "limo" with 100 units of fuel
limo = Car("Limo", 100)

# Add 20 more units of fuel to this new car object
limo.add_fuel(20)

# Print the amount of fuel in the car
print(f"Fuel in {limo.name}: {limo.fuel} units")

# Attempt to drive the car 115 km
limo.drive(115)

# Print the car object to test the __str__ method
print(limo)
