MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter your name: ")


# Function to display the menu and process the choice
def display_menu():
    print(MENU_STRING)
    return input(">>> ").upper()


# Get the first choice
choice = display_menu()

# Process the user's choice until they choose to quit
while choice != "Q":
    if choice == "H":
        print(f"Hello, {name}")
    elif choice == "G":
        print(f"Goodbye, {name}")
    else:
        print("Invalid choice")

    # Get the next choice
    choice = display_menu()

print("Finished.")
