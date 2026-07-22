def long_words_filter(word_list, length):
   new_word_list = []
   for w in word_list:
        if length < len(w):
           new_word_list.append(w)
   return new_word_list

result =  long_words_filter(["cat", "elephant", "dog", "rhinoceros"], 4)
print(result)

result2 = long_words_filter(["hello", "hi", "hey", "howdy", "greetings"], 3)
print(result2)