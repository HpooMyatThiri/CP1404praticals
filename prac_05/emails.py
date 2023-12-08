def main():
    """Establish a dictionary mapping emails to names."""

    email_name_mapping = {}
    user_email_input = input("Enter Email: ")

    while user_email_input != "":
        user_name_result = extract_name_from_email(user_email_input)
        user_confirmation = input(f"Is your name {user_name_result}? (Y/n) ")

        if user_confirmation.upper() != "Y" and user_confirmation != "":
            user_name_result = input("Enter Name: ")

        email_name_mapping[user_email_input] = user_name_result
        user_email_input = input("Enter Email: ")

    for email_address, user_name_result in email_name_mapping.items():
        print(f"{user_name_result} ({email_address})")


def extract_name_from_email(email_address):
    """Retrieve an anticipated name from the given email address."""

    email_prefix = email_address.split('@')[0]
    name_components = email_prefix.split('.')
    user_name_result = " ".join(name_components).title()
    return user_name_result


main()
