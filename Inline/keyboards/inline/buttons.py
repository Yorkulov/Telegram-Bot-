from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Rasmni yuklash", url="https://google.com"),
            InlineKeyboardButton(text="Batafsil", callback_data="photos")
        ],
        [
            InlineKeyboardButton(text="Ulashish", switch_inline_query="photo"),
        ],
    ]
)