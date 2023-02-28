import re

regex = r'^/\*([^*]|\*(?!/))*\*/$'

def is_cpp_multiline_comment(string):
    # Returns True if the string matches the regular expression, False otherwise.
    return bool(re.match(regex, string))

# Example usage:
print(is_cpp_multiline_comment("/* This is a\nmultiline comment */"))  # True
print(is_cpp_multiline_comment("/* Not a\nmultiline comment *"))      # False
print(is_cpp_multiline_comment("/* Another multiline\ncomment */"))   # True
print(is_cpp_multiline_comment("Not a /* comment */"))                # False
