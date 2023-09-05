from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menuPython = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="00 Kirisiw"),
            KeyboardButton(text="01 kerekli daslurler"),
            KeyboardButton(text="02 Hello World!")
        ],
        [
            KeyboardButton(text="artg'a"),
            KeyboardButton(text="Basina")
        ]
    ],
    resize_keyboard=True
)

