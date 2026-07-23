# most_common_word.py
# Finds the most frequently occurring word in a sentence
# Concepts: combining frequency counting with comparison-tracking
# Written during Python learning journey

def most_common_word(sentence):
    words = sentence.split()
    counts = {}
    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1

    most_common = list(counts.keys())[0]
    for word in counts:
        if counts[word] > counts[most_common]:
            most_common = word

    return most_common

print(most_common_word("the cat and the dog and the bird"))    # "the"
print(most_common_word("dog cat cat cat cat"))                 # "cat"
