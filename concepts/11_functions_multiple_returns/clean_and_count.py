# clean_and_count.py
# Analyzes a sentence: lowercases it, counts words, counts vowels
# Concepts: multiple return values, string methods (.lower(), .split()), vowel counting
# Written during Python learning journey

def clean_and_count(sentence):
    clean = sentence.lower()
    count = len(sentence.split())
    number = 0
    for w in clean:
        if w == "a" or w == "e" or w == "i" or w == "o" or w == "u":
            number += 1
    return clean, count, number

lowered, words, vowels = clean_and_count("Hello World From Python")
print(lowered)    # hello world from python
print(words)      # 4
print(vowels)     # 5
