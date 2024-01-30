import os
import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot

from utils.misc import image_generate
from keyboards.default.image_button import generates, backHome
from states.generation import Generation


@dp.message_handler(text_contains="Generate Image", state=None)
async def generate_image(message: types.Message):
    await message.answer("<b>Foydalanish uchun kerakli rasmni tarifini kiriting</b>", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("<i>Bosh sahifaga qaytish uchun</i>: <b>Bosh sahifaga qaytish</b>", reply_markup=backHome)
    await Generation.text_to_image.set()


@dp.message_handler(text_contains="Back to Home", state=Generation.text_to_image)
async def back_to_home(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, "Kerakli bo'limni tanlang", reply_markup=generates)
    await state.finish()
    await state.reset_state()

@dp.message_handler(state=Generation.text_to_image)
async def sendImage(message: types.Message, state: FSMContext):
    await message.reply("Rasm yuklanmoqda...")
    text = message.text
    logging.info(message)
    photo_path = await image_generate(text)
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=message.text)
    # os.remove(photo_path)  # Rasmni xotiradan o'chirib tashlash

