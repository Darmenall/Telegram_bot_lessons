from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menukeyboard import menu
from keyboards.default.pythonkeyboard import menuPython

from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message:Message):
    await message.answer("kurslardi tan'la!",reply_markup=menu)
#####
@dp.message_handler(text="Telegram bot")
async def send_link(message:Message):
    await message.answer("Darmenin' kursina xosh kelibsiz t.me/darmen_all")

@dp.message_handler(text="Python")
async def send_link(message:Message):
    await message.answer("temani tan'la", reply_markup=menuPython)

@dp.message_handler(text="00 Kirisiw")
async def send_link(message:Message):
    await message.answer("00 Kirisiw tema....", reply_markup=ReplyKeyboardRemove())  #answer_video

@dp.message_handler(text="Basina")
async def send_link(message:Message):
    await message.answer("kurslardi tan'la!",reply_markup=menu)



