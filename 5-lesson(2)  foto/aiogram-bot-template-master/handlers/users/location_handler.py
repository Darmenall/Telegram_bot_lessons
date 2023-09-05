from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram import types
from keyboards.default.location_button import keyboard
from utils.misc.get_distance import choose_shortest
from loader import dp

@dp.callback_query_handler(text="mylocation")  #mylocation callback kelgende
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="location jiberin':", reply_markup=keyboard)  #location jiberin' degen xbdi shig'aramz


@dp.message_handler(content_types=types.ContentType.LOCATION)   #paydalaniwshidan location aliw
async def get_contact(message: Message):
    location = message.location  # Xabardan locationi aldiq
    latitude = location.latitude  # Uzinliq kordinata
    longitude = location.longitude  # kenlik kordinata
    closest_shops = choose_shortest(location)  # eki eng jaqin bazardi qaytaradi

    text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\n Araliq: {distance:.1f} km."
                        for shop_name, distance,url, shop_location in closest_shops])  # bir qatarliq for cikli
                    # shop_name, distance, url, shop_location lar qaytadi

    await message.answer(f"Raxmet. \n"   #teksti paydalaniwshig'a jiberip atirmiz
                         f"Latitude= {latitude}\n"
                         f"Longitude= {longitude}\n\n"
                         f"{text}", disable_web_page_preview=True,reply_markup=ReplyKeyboardRemove())

    for shop_name, distance, url, shop_location in closest_shops:  # paydl. eki locationdida jiberip atirmiz
        await message.answer_location(latitude=shop_location['lat'],
                                      longitude=shop_location['lon'])

