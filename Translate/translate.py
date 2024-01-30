import requests
from googletrans import Translator

translator = Translator()

def get_translate(word):
    lang = translator.detect(word).lang
    if lang == "en":
        translate_world = translator.translate(word, dest="uz").text
    elif lang == "uz":
        translate_world = translator.translate(word, dest="en").text
    else:
        translate_world = "No translate"

    return translate_world


def check_english_word(word):
    lang = translator.detect(word).lang
    if lang == "en":
        return True
     
    return False
       


import requests

def get_audio(word):
    if translator.detect(word).lang == "uz":
        word = translator.translate(word, dest="en").text
    if check_english_word(word):
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        request = requests.get(url)
        
        if request.status_code == 200:
            json_data = request.json()
            try:
                if len(json_data) > 0:
                    phonetics = json_data[0]["phonetics"]
                    audios = []

                    for phonitec in phonetics:
                        audio_url = phonitec.get("audio")
                        if audio_url:
                            audios.append(audio_url)

                    return audios
            except (KeyError, IndexError):
                print("Xatolik: API javobidan ovoz ma'lumotini olishda xatolik yuz berdi")
        else:
            print(f"Xatolik: API so'rovi {request.status_code} holatda muvaffaqiyatsiz tugadi")
    else:
        print("Xatolik: Kiritilgan so'z haqiqiy Inglizcha so'z emas")

    return []


# word --> translate[uz] --> audio [uk - us]