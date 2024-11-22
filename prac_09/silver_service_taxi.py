from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness and flagfall."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        self.fanciness = fanciness

    def get_fare(self):
        """Calculate the fare, including the flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
