# safe_int_convert.py
# Safely converts a string to an int, returning None on failure
# Concepts: try/except, returning None for errors, ValueError handling
# Written during Python learning journey

def safe_int_convert(value):
    try:
        return int(value)
    except ValueError:
        return None

print(safe_int_convert("42"))      # 42
print(safe_int_convert("hello"))   # None
print(safe_int_convert("3.14"))    # None
print(safe_int_convert("100"))     # 100
