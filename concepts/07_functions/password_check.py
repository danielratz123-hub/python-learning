# password_check.py
# Validates password strength (upper, lower, digit, min length)
# Concepts: boolean flags, multiple string methods, combining conditions with `and`
# Written during Python learning journey

def password_check(password):
    has_upper = False
    has_lower = False
    has_digit = False
    eight_digits = False

    for w in password:
        if w.isupper():
            has_upper = True
        if w.islower():
            has_lower = True
        if w.isdigit():
            has_digit = True

    if len(password) >= 8:
        eight_digits = True

    return has_upper and has_lower and has_digit and eight_digits

print(password_check("hello"))         # False
print(password_check("password"))      # False
print(password_check("Password"))      # False
print(password_check("Password1"))     # True
print(password_check("MyPass123"))     # True
