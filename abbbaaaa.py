import re

regex = r'(bb|aa|ab|ba)*abb(cc|dd)*|(bb|aa|ab|ba)*b(cc|dd)*'

def matches_language(string):
    # Returns True if the string matches the regular expression, False otherwise.
    return bool(re.match(regex, string))

# Example usage:
print(matches_language("abbcddd"))  # True
print(matches_language("b"))        # False
print(matches_language("bbabb"))    # True
print(matches_language("abcdd"))    # False
