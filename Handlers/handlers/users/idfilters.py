from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

SUPERUSERS = [5994367170, 23453254]
QORAROYXAT = [63563466, 43572723]

@dp.message_handler(filters.IDFilter(chat_id=SUPERUSERS), text_contains="/start")
# @dp.message_handler(chat_id=SUPERUSERS, text='secret')
async def id_filter_example(msg: types.Message):
    await msg.answer("Xush kelibsiz, SuperUser")