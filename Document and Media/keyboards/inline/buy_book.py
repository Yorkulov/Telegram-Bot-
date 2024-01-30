from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

book_keys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Eng yaqin dukonni topish", callback_data="mylocation"),
            InlineKeyboardButton(text="Kontakt ulashish", callback_data="mycontact"),
        ],
    ],
)