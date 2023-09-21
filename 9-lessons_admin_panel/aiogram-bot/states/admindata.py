from aiogram.dispatcher.filters.state import StatesGroup,State
"""StatesGroup gruppa jaratiw"""


class PersonalData(StatesGroup):
    reklama = State()


class PersonalDataPhoto(StatesGroup):
    foto = State()
    text = State()
