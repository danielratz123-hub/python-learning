# count_word_frequency.py
# Counts how many times each word appears in a sentence
# Concepts: building dictionaries dynamically, the `in` operator on dictionaries
# Written during Python learning journey

def count_word_frequency(sentence):
    word_list = sentence.split()
    counts = {}
    for word in word_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

result = count_word_frequency("the cat and the dog and the bird")
print(result)
# Output: {'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}
