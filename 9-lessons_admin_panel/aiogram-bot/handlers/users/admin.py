import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from states.admindata import PersonalData, PersonalDataPhoto
from keyboards.default.admin_keyboard import menuAdmin



@dp.message_handler(text="/start", user_id=ADMINS)
async def get_reklama(message: types.Message):
    await message.answer(text="Assalamu Aleykum Adminperson", reply_markup=menuAdmin)


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def get_reklama(message: types.Message):
    await message.answer("reklama textin' jiberin'")
    await PersonalData.reklama.set()


@dp.message_handler(state=PersonalData.reklama)
async def answer_reklama(message: types.Message, state: FSMContext):
    reklama = message.text
    await state.finish()
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=reklama)
        await asyncio.sleep(0.05)


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    for user in users:
        await message.answer(text=user[1])
        await asyncio.sleep(0.05)


@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tazalandi!")


@dp.message_handler(text="/foto_reklama", user_id=ADMINS)
async def get_reklama(message: types.Message):
    await message.answer("reklama fotosin jiberin'")
    await PersonalDataPhoto.foto.set()


@dp.message_handler(state=PersonalDataPhoto.foto, content_types=types.ContentTypes.PHOTO)
async def answer_reklama(message: types.Message, state: FSMContext):
    foto_id = message.photo[-1].file_id
    await state.update_data(
        {"foto_id": foto_id}
    )
    await message.answer("reklama textin' jiberin'")
    await PersonalDataPhoto.next()



@dp.message_handler(state=PersonalDataPhoto.text)
async def answer_phote(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(
        {"text": text}
    )

    # mag'liwmatlardi qayta oqiymiz
    data = await state.get_data()
    foto_id = data.get('foto_id')
    text = data.get('text')
    await state.finish()

    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_photo(chat_id=user_id, caption=text, photo=foto_id)
        await asyncio.sleep(0.05)






















#
# @dp.message_handler(text="/allusers", user_id=ADMINS)
# async def get_all_users(message: types.Message):
#     users = db.select_all_users()
#     for user in users:
#         await message.answer(text=user[1])
#         await asyncio.sleep(0.05)
#
# @dp.message_handler(text="/reklama", user_id=ADMINS)
# async def send_ad_to_all(message: types.Message):
#     users = db.select_all_users()
#     for user in users:
#         user_id = user[0]
#         await bot.send_message(chat_id=user_id, text="inst: darmen_all layk basip ketin!")
#         await asyncio.sleep(0.05)  # bir waqitta 10 sms limit sol ushin
#
# @dp.message_handler(text="/cleandb", user_id=ADMINS)
# async def get_all_users(message: types.Message):
#     db.delete_users()
#     await message.answer("Baza tazalandi!")