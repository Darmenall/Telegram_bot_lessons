from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def build_keyboard(product):
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Satip aliw", callback_data=f"product:{product}")
        ],  # product:book korinisinde callback qaytadi
    ])
    return keys
