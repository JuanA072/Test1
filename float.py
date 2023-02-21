import re

def is_float_literal(s):
    # Regular expression for floating point literal
    pattern = r'^[-+]?(?:\d+|\d*\.\d+)(?:[eE][-+]?\d+)?$'
    return re.match(pattern, s) is not None
# Test cases
print(is_float_literal("15.75L")) # Flse
print(is_float_literal("1.575E1")) # True
print(is_float_literal("-42.0")) # True
print(is_float_literal("1e6")) # True
print(is_float_literal("0.5e-7")) # True
print(is_float_literal("invalid")) # False
print(is_float_literal("1575e-2")) # True

