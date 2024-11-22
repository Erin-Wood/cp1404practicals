from silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi."""

    # Create a SilverServiceTaxi with fanciness of 2
    taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Drive the taxi 18 km
    taxi.drive(18)

    # Print the details and fare
    print(taxi)
    fare = taxi.get_fare()
    print(f"Fare: ${fare:.2f}")

    # Assert tests to verify the functionality
    assert taxi.get_fare() == 48.78, f"Expected $48.78, got ${fare:.2f}"
    assert str(taxi) == "Hummer, fuel=182, odometer=18, 18km on current fare, $2.46/km plus flagfall of $4.50", \
        f"String mismatch: {taxi}"

if __name__ == "__main__":
    main()
