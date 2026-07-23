# longest_shortest_word.py
# Finds the longest and shortest word in a sentence
# Concepts: comparison-tracking pattern, len() for length comparison, multiple returns
# Written during Python learning journey

def longest_shortest_word(sentence):
    words = sentence.split()
    longest = words[0]
    shortest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
        if len(w) < len(shortest):
            shortest = w
    return longest, shortest

longest, shortest = longest_shortest_word("the quick brown fox jumps over lazy dogs")
print(f"Longest: {longest}")
print(f"Shortest: {shortest}")
