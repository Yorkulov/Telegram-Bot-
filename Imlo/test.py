from transliterate import to_cyrillic, to_latin
from uzwords import words
from difflib import get_close_matches

# print(len(words))
# print(words[134])
# print(words[13334])
# print(words[31134])

# word = "авса"
# x = ""
# x = "Yes" if word in words else "No"
# print(x)

# lotin = to_latin("муваффақият")
# cyril = to_cyrillic("guLim")

# print(lotin)
# print(cyril)

# print(get_close_matches("муваффақия", words, 7))

# lotin_words = []

# for word in words:
#     lotin_words.append(to_latin(word))

# file = open("test.txt", "a+")

# for word in lotin_words:
#     file.write(f'"{word}",\n')

words = "salom joads jkdsf sadlf sadd"
words = words.split()
print(words)