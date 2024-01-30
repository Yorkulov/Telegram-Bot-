from loader import dp, bot
from aiogram.types import ContentType, Message
from pathlib import Path
from aiogram.types import InputFile
from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.inline.buy_book import book_keys



send_id="CAACAgIAAxkBAAIDq2Wqix-TtWaHzljw0WJnfz6dsar3AAKBDwAChIMQSQqeyjbe7uW2NAQ"

download_path = Path().joinpath("downloads", "categories")
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(commands=["kitob"])
async def send_book(message: types.Message):
    # photo_id = "AgACAgUAAxkBAAIHUWErOgOL_YUiW1bawxdvEJM8mUd9AAK4rDEbXltZVRPBqDf39UdmAQADAgADeQADIAQ"
    photo_id = "AgACAgIAAxkBAAIDz2WqkWFC5mdVk8TUS0eogrpLmH10AALh1TEbz2hZSTVfKU8U0soyAQADAgADeQADNAQ"
    msg = "<b>Pythonda Dasturlash Asoslari</b> kitobi.\n"
    msg += "Narxi: 50000 so'm\n\n"
    msg += "<b>Kitob quyidagi do'konlarda sotiladi:</b>\n👉Akademnashr\n👉Hilol nashr\n👉Azon kitoblar\n👉Kitoblar dunyosi"
    await message.reply_photo(photo_id, caption=msg, reply_markup=book_keys)


@dp.message_handler(commands=['rasm'])
async def send_images(message: Message):
    photo_id = "AgACAgIAAxkBAAIDz2WqkWFC5mdVk8TUS0eogrpLmH10AALh1TEbz2hZSTVfKU8U0soyAQADAgADeQADNAQ"
    photo_url = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGhvdG98ZW58MHx8MHx8fDA%3D"
    # photo_file = InputFile(path_or_bytesio="send_photo/black.jpg")
    await message.answer_photo(photo_id, caption="Rasm")
    await message.answer_photo(photo_url, caption="Rasm")
    # await message.answer_photo(photo_file, caption="Rasm")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_id, caption="Rasm")


@dp.message_handler(commands=['albom'])
async def send_albom(message: Message):
    album = types.MediaGroup()
    photo1 = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGhvdG98ZW58MHx8MHx8fDA%3D"
    photo2 = "AgACAgIAAxkBAAIDz2WqkWFC5mdVk8TUS0eogrpLmH10AALh1TEbz2hZSTVfKU8U0soyAQADAgADeQADNAQ"
    video1 = "https://youtu.be/GAvr5_EtOnI?list=PLgutwGMAW6_Tu0j-OzDt__S1IiBaZOWrO"
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_video(video=video1, caption="Grupa bulib tushila!")

    await message.reply_media_group(media=album)

@dp.message_handler()
async def text_handler(message: Message):
    await message.reply("Siz matn yubordingiz!")

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download(destination=download_path)
    doc_id = message.document.file_id
    await message.reply("Siz hujjat yubordingiz!\n"
                        f"file_id = {doc_id}")
    
@dp.message_handler(content_types='video')
async def video_handler(message: Message):
    await message.video.download(destination=download_path)
    video_id = message.message_id
    await message.reply("Video qabul qilindi\n"
                        f"file_id = {video_id}")

@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_handler(message: Message):
    await message.photo[-1].download(destination=download_path)
    photo_id = message.photo[-1].file_id
    await message.reply("Rasm qabul qilindi\n"
                        f"file_id = {photo_id}")
    

@dp.message_handler(content_types=ContentType.STICKER)
async def stiker_handler(message: Message):
    await message.sticker.download(destination=download_path)
    stikr_id = message.sticker.file_id
    send_id="CAACAgIAAxkBAAIDq2Wqix-TtWaHzljw0WJnfz6dsar3AAKBDwAChIMQSQqeyjbe7uW2NAQ"
    await message.reply("Stikir qabul qilindi\n"
                         f"file_id = {stikr_id}")
    # await message.reply_sticker(send_id)

@dp.message_handler(content_types=ContentType.ANY)
async def any_handler(message: Message):
    send_id="CAACAgIAAxkBAAIDq2Wqix-TtWaHzljw0WJnfz6dsar3AAKBDwAChIMQSQqeyjbe7uW2NAQ"
    await message.reply_sticker(send_id)
    # await message.reply((f"{message.content_type} qabul qilindi"))
