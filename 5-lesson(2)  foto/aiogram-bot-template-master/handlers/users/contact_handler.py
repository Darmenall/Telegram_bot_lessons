from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.default.contact_button import keyboard
from loader import dp

@dp.callback_query_handler(text="mycontact")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="Kontactti jiberin': ", reply_markup=keyboard)

@dp.message_handler(content_types="contact")
async def get_contact(message: Message):
    contact = message.contact
    #  telefon_nomer = contact.phone_number
    #  paydalaniwshi_ati = contact.full_name

    await message.answer(f"Raxmet,<b>{contact.full_name}</b>.\n"
                         f"Sizning {contact.phone_number} nomerindi qabil ettik.\n Adminimiz sizge xabarlasadi",
                         reply_markup=ReplyKeyboardRemove())


