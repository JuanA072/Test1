import re

def is_integer_literal(s):
    pattern = r'^[+-]?\d+$'
    return bool(re.match(pattern, s))

# Example cases:
print(is_integer_literal("123"))    #True
print(is_integer_literal("+123"))   #rue
print(is_integer_literal("-123"))   #True
print(is_integer_literal("0"))      #True
print(is_integer_literal("007"))    #True
print(is_integer_literal("123.0"))  #False
print(is_integer_literal("123a"))   #Fase

#check if the string matches the pattern of an integer literal, which is an optional sign (+/-) followed by one or more digits (0-9).If the match is successful, the function returns True, otherwise it returns False.