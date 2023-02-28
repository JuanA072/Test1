import re


def is_email(email):
    # Define regular expression pattern for email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use re.match to check if email matches the pattern
    match = re.match(pattern, email)

    # Return True if match is found, False otherwise
    if match:
        return True
    else:
        return False


# Test the function
email1 = "juanarce@example.com"
email2 = "arce_email"
email3 = "juan.carlos@company.com"
print(is_email(email1))  # True
print(is_email(email2))  # False
print(is_email(email3))  # True

