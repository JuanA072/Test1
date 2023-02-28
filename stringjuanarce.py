import re

def is_float(string):
    # Define regular expression pattern for floating point literal
    pattern = r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$'

    # Use re.match to check if string matches the pattern
    match = re.match(pattern, string)

    # Return True if match is found, False otherwise
    if match:
        return True
    else:
        return False

# Test the function
string1 = "3.78493"
string2 = "0.1e-5"
string3 = "invalid_string"
print(is_float(string1)) # True
print(is_float(string2)) # True
print(is_float(string3)) # False
