from aiogram.types import ContentType, Message
from aiogram.dispatcher import FSMContext

from loader import dp, Bot
from utils.misc.update_image import image_update

download_path = './download/photos'  # Rasmni saqlash uchun joy

@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_handler(message: Message):
    await message.photo[-1].download(destination=download_path)
    photo_id = message.photo[-1].file_id
    photo_path = download_path + photo_id
    photo = await image_update(photo_id)
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=message.text)
