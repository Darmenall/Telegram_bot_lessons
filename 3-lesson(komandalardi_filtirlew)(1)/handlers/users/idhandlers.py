from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

SUPERUSERS = [522087906, 6516516]
CHERNISPISOK = [4545645]


@dp.message_handler(chat_id=SUPERUSERS,commands="lesson")
async def id_filter_example(msg: types.Message):
    await msg.answer("Xosh kelibsiz, SuperUSER! ")


@dp.message_handler(chat_id=CHERNISPISOK)
async def id_filter_example(msg: types.Message):
    await msg.answer("Sizge kiriw qadag'an!")

