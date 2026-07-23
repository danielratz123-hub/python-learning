# count_vowels.py
# Helper function that counts vowels in a word
# Concepts: clean helper function, string iteration
# Written during Python learning journey

def count_vowels(word):
    count = 0
    for w in word:
        if w == "a" or w == "e" or w == "i" or w == "o" or w == "u":
            count += 1
    return count

print(count_vowels("hello"))      # 2
print(count_vowels("sky"))        # 0
print(count_vowels("beautiful"))  # 5
