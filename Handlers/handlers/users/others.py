from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

# IsReplyFilter
@dp.message_handler(is_reply=True, commands='user_id')
async def reply_filter_example(msg: types.Message):
    await msg.reply(msg.reply_to_message.from_user.id)

# IsSenderContact
@dp.message_handler(content_types='contact', is_sender_contact=True)
# @dp.message_handler(filters.IsSenderContact(True), content_types='contact')
async def sender_contact_example(msg: types.Message):
    await msg.answer('Rahmat, kontaktingiz qabul qilindi!')

# ForwardedMessageFilter
@dp.message_handler(is_forwarded=True)
async def forwarded_example(msg: types.Message):
    await msg.reply('Birovning xabarini menga yubormang!')

# ChatTypeFilter
# @dp.message_handler(chat_type='private', commands='is_pm')
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands='shaxsiy')
async def chat_type_example(msg: types.Message):
    await msg.answer('Bu shaxsiy chat')