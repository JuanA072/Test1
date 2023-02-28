import re

def is_integer(string):
    # Define regular expression pattern for integer
    pattern = r'^[-+]?[0-9]+$'

    # Use re.match to check if string matches the pattern
    match = re.match(pattern, string)

    # Return True if match is found, False otherwise
    if match:
        return True
    else:
        return False

# Test the function
string1 = "123"
string2 = "-456"
string3 = "invalid_string"
print(is_integer(string1)) # True
print(is_integer(string2)) # True
print(is_integer(string3)) # False
