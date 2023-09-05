### iHateRegex
from aiogram import types
from aiogram.dispatcher.filters import Regexp
from loader import dp
EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

@dp.message_handler(Regexp(EMAIL_REGEX))  # darmen@mail.com
async def regexp_email(msg: types.Message):
    await msg.answer("Email qabil qilindi!")

@dp.message_handler(Regexp(PHONE_NUM))  # +998906545438
async def regexp_email(msg: types.Message):
    await msg.answer("Telefon nomer qabil qilindi!")

#
# @dp.message_handler(regexp_commands=[COMMAND_EMAIL_REGEX])  #/email: darmen@gmail.com
# async def regexp_email(msg: types.Message):
#     await msg.answer("Telefon nomer qabil qilindi!")



