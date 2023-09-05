from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


# @dp.message_handler(Command(['til','waqit']))
@dp.message_handler(commands=['til','waqit'])
async def changeLanguage(message: types.Message):
    await message.answer(f"Til ozgerdi")

