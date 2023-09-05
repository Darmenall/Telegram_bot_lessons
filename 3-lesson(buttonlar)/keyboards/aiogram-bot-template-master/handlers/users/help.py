from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from states.personaldata import PersonalData

@dp.message_handler(CommandHelp(), state=PersonalData.fullname)
async def bot_help(message: types.Message):
    text = ("Atin ha'm fam kirit")
    
    await message.answer(text)
