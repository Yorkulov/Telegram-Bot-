import logging
from aiogram import types
from aiogram.types import ContentType, Message

from loader import dp

sticker_id = "AAMCAgADGQEAAgXLZa6IEan4RteTt-vFMl2XsWBiUvIAAr4TAAKMnEBIK1quAhjkb-0BAAdtAAM0BA"


@dp.message_handler(content_types=ContentType.STICKER)
async def stiker_handler(message: Message):
    send_id="CAACAgIAAxkBAAIF02Wujb23rfWnm6HdNZ8EctnD30hAAAKBDwAChIMQSQqeyjbe7uW2NAQ"
    await message.reply_sticker(send_id)


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
