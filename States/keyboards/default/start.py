from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🕹  Contact', request_contact=True),
            KeyboardButton(text='📞  Location', request_location=True),
        ],
        [
            KeyboardButton(text="🛍  Mahsulotlar"),
            KeyboardButton(text="📑  Qo'llanma"),
        ],
    ],
    resize_keyboard=True
)