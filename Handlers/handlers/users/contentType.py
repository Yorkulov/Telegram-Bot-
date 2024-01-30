from aiogram import types

from loader import dp

@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    await msg.answer('O\'zingni rasminmi bu!')

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.answer("Kim bu alvasti!")

@dp.message_handler(content_types='sticker')
@dp.message_handler(content_types=types.ContentType.STICKER)
async def emoji_handler(msg: types.Message):
    await msg.answer('😄')

@dp.message_handler(content_types=types.ContentType.CONTACT)
@dp.message_handler(content_types='contact')
async def contact_handler(msg: types.Message):
    await msg.answer('Kimni raqami bu!')

@dp.message_handler(content_types=types.ContentType.VOICE)
async def audio_handler(msg: types.Message):
    await msg.answer('Yaxshi eshitmadim!')