from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

@dp.message_handler(CommandStart(deep_link='kunuz'))   # https://t.me/wiki_1sl_bot?start=kunuz
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"Salem, {message.from_user.full_name}!\n"
    text += f"Sizge {args} masalaqat berdi"
    await message.answer(text)

# @dp.message_handler(commands="start")  #ekewi bir zat
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salem, {message.from_user.full_name}!")
