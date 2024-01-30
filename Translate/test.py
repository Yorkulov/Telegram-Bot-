from googletrans import Translator

translator = Translator()

word = translator.translate('ruchka', dest="en").text
print(word, "\n")