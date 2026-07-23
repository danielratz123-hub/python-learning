# count_uppercase.py
# Counts how many uppercase letters are in a string
# Concepts: string iteration, .isupper() method, counter pattern
# Written during Python learning journey

def count_uppercase(word):
    count = 0
    for letter in word:
        if letter.isupper():
            count += 1
    return count

print(count_uppercase("Hello World"))    # 2
print(count_uppercase("PYTHON"))         # 6
print(count_uppercase("hello"))          # 0
print(count_uppercase("Daniel123"))      # 1
