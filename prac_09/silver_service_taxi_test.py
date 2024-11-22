from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test the SilverServiceTaxi class."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)

    taxi.drive(18)

    print("Taxi details after driving:")
    print(taxi)

    fare = taxi.get_fare()
    print(f"Total fare: ${fare:.2f}")

main()
