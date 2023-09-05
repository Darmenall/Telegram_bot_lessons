from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp

@dp.message_handler(Text(contains="assalam", ignore_case=True))
@dp.message_handler(Text(equals='assalamu aleykum', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply("Waaleykum assalam")


# @dp.message_handler(Text(contains="assalam", ignore_case=True))
# async def text_example(msg: types.Message):
#     await msg.reply("Waaleykum assalam")

@dp.message_handler(Text(equals='aqmaq', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply("ozin aqmaq")

#startswith
#endswith

