import logging

from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from loader import dp
from keyboards.inline.productKeyboard import categoryMenu, coursesMenu, booksMenu, \
                    telegram_keyboard, algorithm_keyboard
                        
from keyboards.inline.callback_data import course_callback, book_callback

@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(message: Message):
    await message.answer(f"Mahsulot tanlang", reply_markup=categoryMenu)

@dp.callback_query_handler(text="courses")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    await call.message.answer("Kurs tanlang", reply_markup=coursesMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="books")
async def buy_books(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kitoblar", reply_markup=booksMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(course_callback.filter(item_name="telegram"))
async def buying_course(call: CallbackQuery, callback_data: dict):

    # logging yordamida foydalanuvchi qaytgan callbackni ko'ramiz
    logging.info(f"{callback_data=}")

    await call.message.answer(f"Siz Mukammal Telegram Bot Kursini tanladingiz.", 
                              reply_markup=telegram_keyboard)
    
    await call.answer(cache_time=60)


@dp.callback_query_handler(course_callback.filter(item_name="algorithm"))
async def buying_course(call: CallbackQuery, callback_data: dict):

    await call.message.answer(f"Siz Algorithm kursini tanladingiz.",
                              reply_markup=algorithm_keyboard)
    
    await call.answer(cache_time=60)


@dp.callback_query_handler(book_callback.filter(item_name="python_book"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=60, show_alert=True)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    # await call.answer()