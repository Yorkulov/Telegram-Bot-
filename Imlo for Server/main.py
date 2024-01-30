import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from check_word import checkWord

TOKEN = '6792370774:AAEZbC3lt71txFxoY6nzWLr3o9WQ0kjYWnM'

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.reply("Uz imlo lotin krill botiga Xush Kelibsiz!")

# @dp.message(Command('/help'))
# async def help_user(message: types.Message):
    # await message.reply("Botdan foydalanish uchun so'zni yuboring.")

@dp.message()
async def checkImlo(message: types.Message):
    print(message.text, message.from_user.full_name, message.from_user.username)
    words = message.text.split()
    if len(words) > 1:
        answer = ""
        for word in words:
            result = checkWord(word)
            if result['available']:
                answer += word.capitalize() + "\t"
            else:
                response = f"❌ {word.capitalize()}\n"
                for text in result['matches']:
                    response += f"✅ {text.capitalize()}\n"
                answer += "\t...\t"
                await message.answer(response)
        await message.answer(answer)

    else:           
        for word in words:
            result = checkWord(word)
            if result['available']:
                response = f"✅ {word.capitalize()}"
            else:
                response = f"❌ {word.capitalize()}\n"
                for text in result['matches']:
                    response += f"✅ {text.capitalize()}\n"
            await message.answer(response)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
