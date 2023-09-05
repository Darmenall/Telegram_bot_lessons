from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

book_keys = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🔍 Eng jaqin Bazardi aniqlaw", callback_data="mylocation"),
        InlineKeyboardButton(text="📲 Nomerdi jiberiw", callback_data="mycontact"),
    ]
])