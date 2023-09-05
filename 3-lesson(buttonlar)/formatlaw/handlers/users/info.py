from aiogram import types

from loader import dp

### 1-usil
# @dp.message_handler(commands="info_html")
# async def bot_help(message: types.Message):
#     text = ("Buyruqlar: ",
#             "/start - Botni ishga tushirish",
#             "/help - Jardem")
#
#     await message.answer("\n".join(text))


#
# ######2-usil  HTML jardeminde formatlaw
# @dp.message_handler(commands="info_html")
# async def bot_info(message: types.Message):
#     text = f"Assalamu aleykum, {message.from_user.full_name}!\n"
#     text +="Bul <b> qalin text. </b>\n"
#     text += "Bul <i> qiysiq text. </i>\n"
#     text += "Bul <u> astinda sizig'i bar text. </u>\n"
#     text += "Bul <s> oshirilgen text. </s>\n"
#     text += "Bul <a href='https://core.telegram.org/bots/api#formatting-options'> Formatlawdin linki </a>\n"
#     text += "Bul <code> print('Hello World!) </code> kod.\n"
#
#     await message.answer(text)

#
#
###### 3-usil Markdown jardeminde   (loader-types.ParseMode.MARKDOWN_V2)
# @dp.message_handler(commands="info_markdown")
# async def bot_info(message: types.Message):
#     text = f"Assalamu aleykum, {message.from_user.full_name}\!\n" # !
#     text +="Bul *qalin text\.* \n"
#     text += "Bul _qiysiq text\._ \n"
#     text += "Bul __astinda sizigi bar text\.__ \n"
#     text += "Bul ~oshirilgen text\.~ \n"
#     text += "Bul [Darmennin linki](t.me/darmen_all)\n"
#     text += "Bul `print('Hello World)` kod \n"
#     await message.answer(text, parse_mode=types.ParseMode.MARKDOWN_V2)


# #### botg'a jiberiw <s> Salem</s>
#
# ###### 4-usil aiogramnin ozindegi funlar
from aiogram.utils.markdown import hbold,hcode,hitalic,hunderline,hstrikethrough,hlink
@dp.message_handler(commands="info")
async def info(message: types.Message):
    text = f"Assalamu aleykum, {message.from_user.full_name}!\n"
    text +="Bul" + hbold("qalin text. \n")
    text += "Bul "+ hitalic(" qiysiq text.\n")
    text += "Bul "+ hunderline(" astinda sizig'i bar text. \n")
    text += "Bul "+ hstrikethrough(" oshirilgen text.\n")
    text += "Bul "+ hlink('Formatlawdin linki \n', "https://core.telegram.org/bots/api#formatting-options")
    text += "Bul "+ hcode(" print('Hello World!)")

    await message.answer(text)
# #
#
#
