from aiogram import types
from aiogram.dispatcher import FSMContext  # magliwmatlardi, qaerde ekenin saqlap qaliw
from aiogram.dispatcher.filters import Command


from loader import dp
from states.personaldata import PersonalData

@dp.message_handler(Command("anketa"))
async def enter_test(message: types.Message):
    await message.answer("Toliq atin'izdi jazin:")
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message,state: FSMContext):
    fullname = message.text
    # await state.update_data(name=fullname)
    await state.update_data(
        {"name": fullname}
    )
    await message.answer("Email manzildi kiritin:")
    # await PersonalData.email.set()
    await PersonalData.next()

@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(
        {"email": email}
    )
    await message.answer("Telefon nomer kirit:")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.photoNum)
async def answer_phote(message: types.Message, state: FSMContext):
    num = message.text
    await state.update_data(
        {"phone": num}
    )

    # mag'liwmatlardi qayta oqiymiz
    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    msg = "Tomendegi mag'liwmatlar alindi:\n"
    msg += f"name: {name.title()}\n"
    msg += f"Email: {email}\n"
    msg += f"Telefon: {phone}"
    await message.answer(msg)

    await state.finish()
    # await state.reset_state(with_data=False)  #operativ panitte turaberedi

