from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    print(message.text, message.from_user.full_name, message.from_user.username)
    await message.answer(message.text)
