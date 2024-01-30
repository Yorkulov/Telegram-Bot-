import wikipedia

wikipedia.set_lang("uz")

# text = wikipedia.search("Odam")
# print(f"Search results:\n{text}")
# question = text[0]

# answer = wikipedia.summary("Inson")
# print(answer)


try:
    page = wikipedia.page('Men seni sevaman')
    print(page.content)  # Maqola matnini chop etish
except wikipedia.exceptions.DisambiguationError as e:
    print("Maqola aniqlanmadi. Quyidagi variantlarga o'xshash maqolalar mavjud:")
    print(e.options)  # O'xshash variantlarni chop etish
except wikipedia.exceptions.PageError:
    print("Bu mavzuda maqola mavjud emas!")

# if len(answer) > 3500:
#     for i in range(len(answer) // 3500 + 1):
#         new_answer = answer[:3500]
#         answer = answer[3500:]
#         print(new_answer + "\n\n\n\n")
# else:
#     print(answer)
