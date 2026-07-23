# find_extreme_words.py
# Finds the word with the most and least vowels using a helper function
# Concepts: function composition (using helper function), comparison-tracking on function results
# Written during Python learning journey

def count_vowels(word):
    count = 0
    for w in word:
        if w == "a" or w == "e" or w == "i" or w == "o" or w == "u":
            count += 1
    return count

def find_extreme_words(word_list):
    most = word_list[0]
    least = word_list[0]

    for w in word_list:
        current_count = count_vowels(w)

        if current_count > count_vowels(most):
            most = w

        if current_count < count_vowels(least):
            least = w

    return most, least

most, least = find_extreme_words(["hello", "sky", "beautiful", "rhythm", "queue"])
print(f"Most vowels: {most}")
print(f"Least vowels: {least}")
