from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard = [
                                    [
                                        KeyboardButton(text="phone",
                                                       request_contact=True),
                                    ],
                               ],
)