import re

regex = r'^[a-zA-Z_$][a-zA-Z0-9_$]*$'

def is_java_identifier(string):
    # Returns True if the string matches the regular expression, False otherwise.
    return bool(re.match(regex, string))

# Example usage:
print(is_java_identifier("myVariable"))    # True
print(is_java_identifier("1variable"))     # False
print(is_java_identifier("MyClass()"))     # False
print(is_java_identifier("someMethod()"))  # True
