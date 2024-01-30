from uzwords import words, lotin_words
from difflib import get_close_matches

def checkWord(word, words=words):
    word = word.lower()
    if detect_alphabet(word) == "Krill":
        matches = set(get_close_matches(word, words, 5))
        avialable = False

        if word in matches:
            avialable = True
            matches = word
        elif 'ҳ' in word:
            word = word.replace('ҳ', 'х')
            matches.update(get_close_matches(word, words))
        elif 'х' in word:
            word = word.replace('х', 'ҳ')
            matches.update(get_close_matches(word, words))
        
        return {'available': avialable, 'matches': matches}
    elif detect_alphabet(word) == 'Lotin':
        matches = set(get_close_matches(word, lotin_words, 5))
        avialable = False

        if word in matches:
            avialable = True
            matches = word

        return {'available': avialable,'matches': matches}


def detect_alphabet(word):
    latin_alphabet = set('abcdefghijklmnopqrstuvwxyz')
    cyrillic_alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    if set(word).issubset(latin_alphabet):
        return 'Lotin'
    elif set(word).issubset(cyrillic_alphabet):
        return 'Krill'
    else:
        return 'Ikkala alifboga tegmagan'
