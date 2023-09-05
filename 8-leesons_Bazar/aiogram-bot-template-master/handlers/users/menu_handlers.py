from typing import Union

from aiogram import types
from aiogram.types import CallbackQuery, Message

from keyboards.inline.menu_keyboards import (
    menu_cd,
    categories_keyboard,
    subcategories_keyboard,
    items_keyboard,
    item_keyboard,
)
from loader import dp, db


# Bas menyu Texti ushin handler
@dp.message_handler(text="Bas menu")
async def show_menu(message: types.Message):
    # paydalaniwshiga ha'mme  kategoriyalardi qaytaramiz
    await list_categories(message)


# Kategoriyalarni qaytaruvchi funksiya. Callback query yaki Message qabil qiliw ha'm mumkin.
# **kwargs jardeminde ese basqa parametrlerdi ha'm qabil qiladi: (category, subcategory, item_id)
async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    # Keyboarddi Shig'aramiz
    markup = await categories_keyboard()

    # Eger Paydalaniwshi Message kelse Keyboarddi Jiberemiz
    if isinstance(message, Message):
        await message.answer("bo'limdi saylan", reply_markup=markup)

    # Eger Paydalaniwshidan Callback kelse Callback natbibi o'zgertiremiz
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


# Ost-kategoriyalardi qaytariwshi funksiya
async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)

    # Xabar textin o'zgertiremiz va keyboardni jiberemiz
    await callback.message.edit_reply_markup(markup)


# Ost-kategoriyaga tiysli zatlardin dizimin jiberiwshi funksiya
async def list_items(callback: CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category, subcategory)

    await callback.message.edit_text(text="zatlardi saylan", reply_markup=markup)


# bir zat ushin satip aliw knopkasi fiberiwshi funksiya
async def show_item(callback: CallbackQuery, category, subcategory, item_id):
    markup = item_keyboard(category, subcategory, item_id)

    # zat haqinda tuwsinik bazadan alamiz
    item = await db.get_product(item_id)

    if item["photo"]:
        text = f"<a href=\"{item['photo']}\">{item['productname']}</a>\n\n"
    else:
        text = f"{item['productname']}\n\n"
    text += f"Cenasi: {item['price']}$\n{item['description']}"

    await callback.message.edit_text(text=text, reply_markup=markup)

######Loatant -> Sariq dev ###########
# joqaridagi ha'mme funksiyalar ushin bir handler
@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Handlerga kelgen Callback query
    :param callback_data: knopka basilg'anda kelgen mag'liwmatlar
    """

    # paydalaniwshi so'ragan Level (qavat)
    current_level = callback_data.get("level")

    # paydalaniwshi so'ragan Kategoriya
    category = callback_data.get("category")

    # Ost-kategoriya (ha'r daim ha'm bo'labermiydi)
    subcategory = callback_data.get("subcategory")

    # zatlar ID sanin (ha'r daim ha'm bo'labermiydi)
    item_id = int(callback_data.get("item_id"))

    # Har bir Level (etalg'a) mas funksiyalarni jiberip shig'amiz
    levels = {
        "0": list_categories,  # Kategoriyalarni qaytaramiz
        "1": list_subcategories,  # Ost-kategoriyalarni qaytaramiz
        "2": list_items,  # zarlardi qaytaramiz
        "3": show_item,  # zarlardi ko'rsetemiz
    }

    # paydalaniwshidan kelgen Level sanina mas funksiyani shaqiramiz
    current_level_function = levels[current_level]

    # Saylang'an funksiyani shaqiramiz ha'm kerekli parametrlerdi jiberemiz
    await current_level_function(
        call, category=category, subcategory=subcategory, item_id=item_id
    )