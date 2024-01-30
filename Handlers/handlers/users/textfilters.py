from aiogram import types

from aiogram.dispatcher import filters

from loader import dp

FORBIDDEN_PHRASE = [
    'ahmoq',
    'telba',
]

@dp.message_handler(text_contains='ahmoq')  # text tarkibida bo'lsa
async def text_axample(msg: types.Message):
    await msg.reply("Nimaga sukyabsan taviya!")


@dp.message_handler(filters.Text(equals="tentak", ignore_case = True))  # text shunga teng bo'lsa
async def text_example(msg: types.Message):
    await msg.reply("Nega sukinyabsan molbashara")

@dp.message_handler(filters.Text(equals='assalom alaykum', ignore_case=True))
@dp.message_handler(filters.Text(contains='assalom', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('Waalaykum assalom')


# boshqa parametrlar
# startswith
# endswith