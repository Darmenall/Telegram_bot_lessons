from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, CommandSettings

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyriqlar: ",
            "/start - Botti iske qosiw",
            "/help - jardem")
    
    await message.answer("\n".join(text))


@dp.message_handler(CommandSettings())
async def bot_settings(message: types.Message):
    text = ("Sazlamalar")

    await message.answer(text)