# word_lengths.py
# Builds a dictionary mapping each word to its length
# Concepts: clean dictionary building, edge case handling (empty string)
# Written during Python learning journey

def word_lengths(sentence):
    word_dict = {}
    words = sentence.split()
    for word in words:
        word_dict[word] = len(word)
    return word_dict

print(word_lengths("hello world python"))
# {'hello': 5, 'world': 5, 'python': 6}

print(word_lengths("I love code"))
# {'I': 1, 'love': 4, 'code': 4}

print(word_lengths(""))
# {}
