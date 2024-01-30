import asyncio
import logging
import sys
import translate

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold    

from aiogram.methods.get_user_profile_photos import GetUserProfilePhotos

# Bot token can be obtained via https://t.me/BotFather
TOKEN = '6731100005:AAFSn7VJGpOrWDtru7LhUy6sk0ud3sQ86Ws'

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"{hbold(message.from_user.full_name)} welcome!\nBotdan foydalanish uchun so'zni kiritasiz.")


@dp.message()
async def send_translate(message: types.Message) -> None:
    print(message.text, message.from_user.full_name, message.from_user.username)
    if message.text == "Men tentakman":
        await message.reply("Tur yuqol unda!")

    word = translate.get_translate(message.text)
    await message.reply(f"{message.text} ---> {word}")

    audios = translate.get_audio(message.text)
    for i in range(len(audios)):
        if i == 0:
            await message.reply_audio(audios[i], caption="American English")
        if i == 1:
            await message.reply_audio(audios[i], caption="British English")

        

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())