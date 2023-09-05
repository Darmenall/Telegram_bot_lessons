import logging

from keyboards.inline.produckKeyboard import categoryMenu, coursesMenu, telegram_keyboard, booksMenu
from aiogram.types import Message, CallbackQuery
from loader import dp
from keyboards.inline.callback_data import course_callback, book_callback
# from keyboards.inline.produckKeyboard import

@dp.message_handler(text_contains="Zatlar")
async def bot_help(message: Message):
    await message.answer(f"zarlardi saylan'", reply_markup=categoryMenu)

@dp.callback_query_handler(text="courses")
async def bot_call(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")  #logging jardeminde paydalaniwshidan qaytqan mag;liwmatti koriw
    logging.info(f"{call.from_user.username}")
    await call.message.answer(f"Kurslardi tan'la", reply_markup=coursesMenu)
    await call.message.delete()
    await call.answer(cache_time=60)  # oshik turg'an waqitta 60 sek bot ozinde yadinda tutip turadi


@dp.callback_query_handler(text_contains="books")
async def bot_books(call: CallbackQuery):
    await call.message.answer(f"Kitablar", reply_markup=booksMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(course_callback.filter(item_name="telegram"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer(f"Siz Telegram bot kursin sayladiniz",
                              reply_markup=telegram_keyboard)
    await call.answer(cache_time=60)


@dp.callback_query_handler(book_callback.filter(item_name="cpp_book"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Zakaz qabil etildi", cache_time=60, show_alert=True)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    #  aynada jawap qaytaramiz
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer()
