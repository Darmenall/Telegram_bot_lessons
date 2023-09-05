from aiogram import types

from loader import dp

@dp.message_handler(hashtags='money')
async def hashtag_example(msg: types.Message):
    await msg.answer("Eeee, akang kuchaydi!")