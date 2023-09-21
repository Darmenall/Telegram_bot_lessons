from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menuAdmin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="reklama"),
        ],
        [
            KeyboardButton(text="allusers"),
            KeyboardButton(text="cleandb"),
        ]
    ],
    resize_keyboard=True
)