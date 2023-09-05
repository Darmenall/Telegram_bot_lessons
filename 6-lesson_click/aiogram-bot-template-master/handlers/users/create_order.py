from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from loader import dp, bot
from data.products import python_lessons, python_book, FAST_SHIPPING,  REGULAR_SHIPPING, PICKUP_SHIPPING
from keyboards.inline.product_keys import build_keyboard
from data.config import ADMINS


@dp.message_handler(Command('kitap'))
async def show_invoices(message: types.Message):
    caption = "<b>Python Dasturlew </b> kitabi. \n\n"
    caption += "Bul kitap ti satip aliwdi maslahat beremen\n"
    caption += "Cenasi: <b>50000 so'm</b>"
    await message.answer_photo(photo="AgACAgIAAxkBAAIDp2TjD5JFMGa1OJ5-Nk0zmgnkvB8bAAJRyjEbCCMYS7qXRUpjuzH7AQADAgADeQADMAQ",
                               caption=caption, reply_markup=build_keyboard("book"))


@dp.message_handler(Command("lessons"))
async def show_lessons(message: types.Message):
    caption = "<b>Python leorning</b> kursi.\n\n"
    caption += "3 ayda eng jaqsi Dasturshi bolin.\n\n"
    caption += "✔ Python Basic (2-ay)\n"
    caption += "✔ Telegram Bot (1-ay)\n"
    caption += "Cenasi: <b>150000 so'm</b>"

    await message.answer_photo(photo="AgACAgIAAxkBAAIDp2TjD5JFMGa1OJ5-Nk0zmgnkvB8bAAJRyjEbCCMYS7qXRUpjuzH7AQADAgADeQADMAQ",
                               caption=caption, reply_markup=build_keyboard("lessons"))

@dp.message_handler(Command("zatlar"))
async def book_invoice(message: types.Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **python_book.generate_invoice(),
                           payload="123456")
    await bot.send_invoice(chat_id=message.from_user.id,
                           **python_lessons.generate_invoice(),
                           payload="1234567")


@dp.callback_query_handler(text="product:book")
async def book_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **python_book.generate_invoice(),
                           payload="payload:KItap")

    await call.answer()


@dp.callback_query_handler(text="product:lessons")
async def lessons_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **python_lessons.generate_invoice(),
                           payload="payload: Lessons")   # imenno ne zat satilip atirgani qalese index qoysa boladi

    await call.answer()


@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Shet elge jetkizip berealmaymis!!!")
    elif query.shipping_address.city.lower() == "nukus":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[FAST_SHIPPING,  REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGULAR_SHIPPING],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)

    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Tolew ushin raxmet!")

    await bot.send_message(chat_id=522087906,
                           text=f"Tomendegi zat satildi: {pre_checkout_query.invoice_payload}\n"
                                f"ID: {pre_checkout_query.id}\n"
                                f"Telegram user: {pre_checkout_query.from_user.full_name}"
                                f"Klient: {pre_checkout_query.order_info.name}, "  # order_info.name = Satip aliwga jazilg'an ati, from_user.name = paydalaniwshinin ati
                                f"tel: {pre_checkout_query.order_info.phone_number}")


                            #    f"adres: {pre_checkout_query.order_info.shipping_address.city}"





