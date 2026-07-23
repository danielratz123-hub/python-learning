# letter_frequency.py
# Counts how many times each letter appears in a word (ignores spaces)
# Concepts: dictionary building, `continue` statement, edge case handling
# Written during Python learning journey

def letter_frequency(word):
    counts = {}
    for letter in word:
        if letter == " ":
            continue
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

print(letter_frequency("hello"))
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print(letter_frequency("hello world"))
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
