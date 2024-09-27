def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

# Example usage:
if __name__ == "__main__":
    # Get user input
    celsius_input = float(input("Enter temperature in Celsius: "))
    fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

    # Perform conversions
    fahrenheit_output = celsius_to_fahrenheit(celsius_input)
    celsius_output = fahrenheit_to_celsius(fahrenheit_input)

    # Print the results
    print(f"{celsius_input}°C is {fahrenheit_output}°F")
    print(f"{fahrenheit_input}°F is {celsius_output}°C")
