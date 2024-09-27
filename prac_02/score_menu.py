def get_valid_score():
    """Prompt the user to enter a valid score between 0 and 100 inclusive."""
    while True:
        try:
            score = float(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def evaluate_score(score):
    """Evaluate the score and return the result as a string."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print stars corresponding to the score."""
    if score >= 0:
        print('*' * int(score))


def main():
    """Main function to run the program."""
    score = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Choose an option: ").strip().upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = evaluate_score(score)
            print(f"Score result: {result}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
