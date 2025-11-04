def extract_name_from_email(email: str) -> str:
    """Extracts a suggested name from the email address by splitting the local part."""
    local_part = email.split('@')[0]
    cleaned_parts = local_part.replace('.', ' ').replace('_', ' ')
    suggested_name = " ".join(part.title() for part in cleaned_parts.split())
    return suggested_name


def main():
    """Reads emails and names from the user, stores them, and prints the results."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        suggested_name = extract_name_from_email(email)

        # Get confirmation, strip whitespace, and convert to lowercase for checking
        confirmation = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()

        # Check for default 'Y' (empty input) or explicit 'y'
        if confirmation in ("", "y"):
            name = suggested_name
        else:
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")

    # Print all stored entries
    print("\nStored Entries:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()