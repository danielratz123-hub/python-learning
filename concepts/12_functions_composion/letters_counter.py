def is_short_words(word):
 letters_number = len(word)
 if letters_number <= 5:
  return True
 else:
  return False
 
def count_short_words(word_list):
 count = 0
 for i in word_list:
    if is_short_words(i):
     count +=1
 return count

     
words = ["cat", "elephant", "dog", "bird", "rhinoceros", "fish"]
result = count_short_words(words)
print(f"Short words: {result}")  