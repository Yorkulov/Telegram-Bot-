from aiogram import types

from loader import dp

from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink

@dp.message_handler(commands="info")
async def bot_info(message: types.Message):
    text = "Tayyor functionlar \n" + hbold("Salom\n")
    text += hitalic("Salom\n")
    text += hunderline("Salom\n")
    text += hstrikethrough("Salom\n")
    text += hlink("Salom", url="https://google.com")

    await message.reply(text)

@dp.message_handler(commands='info_html')
async def bot_help(message: types.Message):
    text = f"Assalomu alaykum, {message.from_user.full_name}!\n"
    text += "Bu <b>qalin matn.</b>\n"
    text += "Bu esa <i>egri matn.</i>\n"
    text += "Bu <u>ostiga chizilgan matn</u>\n"
    text += "Bu esa <s>o'chirilgan matn</s>\n"
    text += "Bu esa <a href='https://google.com'>Google ketdik</a>\n"
    text += "Bu esa <code>print('Hello World')</code> kod.\n\n"

    await message.reply(text)

