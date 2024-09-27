import random

def evaluate_score(score):
    """Evaluate the score and return the result as a string."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    # Ask user for their score
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)

    # Generate a random score between 0 and 100
    random_score = random.uniform(0, 100)
    random_result = evaluate_score(random_score)
    print(f"Random score: {random_score:.2f} - {random_result}")

if __name__ == "__main__":
    main()
