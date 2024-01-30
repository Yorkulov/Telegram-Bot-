from aiogram.types import ContentType, Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot


download_path = 'path/to/download/folder'  # Rasmni saqlash uchun joy

@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_handler(message: Message):
    await message.photo[-1].download(destination=download_path)
    photo_id = message.photo[-1].file_id
    await message.reply("Rasm qabul qilindi\n"
                        f"file_id = {photo_id}")
    
