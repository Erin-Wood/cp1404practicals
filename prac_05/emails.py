def extract_name_from_email(email):
    """
    Function to extract a name from the given email.
    It assumes the email format is in the form 'name@domain.com'.
    """
    name_part = email.split('@')[0]
    name = ' '.join(name_part.split('.')).title()
    return name

def store_emails_and_names():
    """
    Function to store users' emails and names in a dictionary.
    It prompts the user for their email, extracts a name from the email, and allows
    for manual name correction if needed.
    """
    email_dict = {}

    while True:
        email = input("Enter your email (or press Enter to finish): ")
        if not email:
            break

        extracted_name = extract_name_from_email(email)
        print(f"Is your name {extracted_name}? (Y/n) ", end='')

        response = input().strip().lower()

        if response in ['', 'y']:
            name = extracted_name
        else:
            name = input("Please enter your name: ")

        email_dict[email] = name

    print("\nStored email and names:")
    for email, name in email_dict.items():
        print(f"{email} : {name}")

store_emails_and_names()
