from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#00 Kirish"),
            KeyboardButton(text="#01 Kerakli dasturlar"),
            KeyboardButton(text="#02 Hello Wolrd!"),
        ],
        [
            KeyboardButton(text="Back"),
            KeyboardButton(text="Home"),
        ],
    ],

    resize_keyboard=True
)