from aiogram import types
from aiogram.dispatcher.filters import Command
# from aiogram.types import InputFile

from loader import dp, bot

#
# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def get_file_id(message: types.Message):
#     await message.reply(message.photo[-1].file_id)
#
#
# @dp.message_handler(content_types=types.ContentType.VIDEO)
# async def get_file_id_v(message: types.Message):
#     await message.reply(message.video.file_id)
#
# @dp.message_handler(Command('kitap'))
# async def send_book(message: types.Message):
#     photo_id = "AgACAgIAAxkBAAIDp2TjD5JFMGa1OJ5-Nk0zmgnkvB8bAAJRyjEbCCMYS7qXRUpjuzH7AQADAgADeQADMAQ"
#     photo_url = "https://i.blogs.es/09b647/googlefotos/840_560.jpg"  #aqiri jpg boliw kerek
#     photo_file = InputFile(path_or_bytesio="photos/1679385227FdUMpJwccB.png")
#     await message.reply_photo(photo_file,caption="Python leorning \n Cenasi:50000 so'm ")
#     await message.answer_photo(photo_url,caption="Python leorning \n Cenasi:50000 so'm ")
#     await bot.send_photo(chat_id=message.from_user.id,photo=photo_id,
#                          caption="Python leorning \n Cenasi:50000 so'm ")
#
#
# @dp.message_handler(Command('books'))
# async def send_books(message: types.Message):
#     albom = types.MediaGroup()  #Gruppag'a ashiw
#     photo = "https://cdn.hackr.io/uploads/posts/attachments/1679385227FdUMpJwccB.png"
#     photo1 = "AgACAgIAAxkBAAIDpWTjDu3BSg9F4jw9pKm7F4dcBEllAAJNyjEbCCMYS2NreEFv1SphAQADAgADeQADMAQ"
#     photo2 = "https://www.interviewbit.com/blog/wp-content/uploads/2022/01/Python-Cookbook.jpg"
#     albom.attach_photo(photo)  # gruppag'a qosiw
#     albom.attach_photo(photo1)  # gruppag'a qosiw
#     albom.attach_photo(photo2, caption="python photo")
#
#     await message.reply_media_group(media=albom)
#



#########################################################

from keyboards.inline.buy_book import book_keys


@dp.message_handler(Command('kitap'))
async def send_book(message: types.Message):
    photo_id = "AgACAgIAAxkBAAIDp2TjD5JFMGa1OJ5-Nk0zmgnkvB8bAAJRyjEbCCMYS7qXRUpjuzH7AQADAgADeQADMAQ"
    msg = "<b>Python Basic </b> kitabi.\n"
    msg += "Cenasi: 50000 so'm \n\n"
    msg += "<b>Kitap tomendegi bazarlarda satiladi:</b>\n👉Orayliq Bazar\n👉Kateks\n👉Gane Qala"
    await message.reply_photo(photo_id, caption=msg, reply_markup=book_keys)

