import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Paydalaniwshinin' atin mb g'a qosip ketip atirmiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=err)

    await message.answer("Xosh kelibsiz!")
    # Adminge xabar beremiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazag'a qosildi.\nBazada {count} paydalaniwshi bar."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
