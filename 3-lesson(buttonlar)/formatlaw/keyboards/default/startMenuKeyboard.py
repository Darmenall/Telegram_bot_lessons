from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Zatlar"),
            KeyboardButton(text="📜 Qollanba"),
        ],
    ],
    resize_keyboard=True
)