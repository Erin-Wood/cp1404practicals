def get_valid_password(min_length):
    """
    Continuously prompts for a password until it meets the minimum length.
    """
    while True:
        password = input(f"Enter a password (minimum {min_length} characters): ")
        if len(password) >= min_length:
            return password
        print(f"Password must be at least {min_length} characters long. Try again.")

def display_asterisks(password):
    """
    Prints asterisks equivalent to the length of the password.
    """
    print("*" * len(password))

def main():
    """
    Main function to handle password input and display asterisks.
    """
    min_length = 8
    password = get_valid_password(min_length)
    print("\nPassword accepted.")
    display_asterisks(password)

if __name__ == "__main__":
    main()
