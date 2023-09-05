from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

@dp.message_handler(content_types="document")
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.answer('bul ne?')

# @dp.message_handler(conten_types="photo")
# async def photo_handler(message: types.Message):
#     await message.answer('bul qanday foto?')







@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def photo_handler(msg: types.Message):
    await msg.answer('😘')

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def photo_handler(msg: types.Message):
    await msg.answer('kim bul adam?')

@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def photo_handler(msg: types.Message):
    await msg.answer('jaqsi esitilmi atir')
