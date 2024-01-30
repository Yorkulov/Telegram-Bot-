import asyncio
import logging
import sys
import wikipedia

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Bot token can be obtained via https://t.me/BotFather
TOKEN = '6571477104:AAFgtLNe_b6SS64LRjcIVeiCsb7KRMx0X3I'

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

wikipedia.set_lang("uz")

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
    await message.answer(f"Salom, {hbold(message.from_user.full_name)}!")
    await message.answer("Bu bot sizga kerakli mavzu bo'yicha malumot to'plashda yordam beradi!\nExample: 'Maqola'")


@dp.message()
async def send_maqola(message: types.Message) -> None:

    print(message.text, message.from_user.full_name, message.from_user.username)

    if message.text == "Men tentakman":
        await message.reply(f"To'gri men ham bu fikringga qo'shilaman {message.from_user.full_name}")
        
    else:
        try:
            query = message.text
            maqola = wikipedia.summary(query, sentences=2)
            try:
                page = wikipedia.page(query)
                content = page.content
                if len(content) > 4000:
                    while content:
                        new_answer = content[:4000]
                        content = content[4000:]
                        await message.reply(new_answer + "...")
                else:
                    await message.answer(content)
            except wikipedia.exceptions.DisambiguationError as e:
                await message.reply("Maqola aniqlanmadi. Quyidagi variantlarga o'xshash maqolalar mavjud:\n" + "\n".join(e.options))
            except wikipedia.exceptions.PageError:
                await message.reply("Bu mavzuda maqola mavjud emas!")
        except TypeError:
            # But not all the types are supported to be copied so need to handle it
            await message.answer("Maqola aniqlanmadi, Maqola nomini tekshirib ko'ring!")
        except wikipedia.exceptions.PageError:
            await message.reply("Bu mavzuda maqola mavjud emas!")

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())