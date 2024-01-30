from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

generates = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Generate Image"),
        ],
    ],

    resize_keyboard=True
)


# back_to_home klaviatura
backHome = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Back to Home"),
        ],
    ],

    resize_keyboard=True
)
