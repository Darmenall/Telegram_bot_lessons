from aiogram.dispatcher.filters.state import StatesGroup,State
"""StatesGroup gruppa jaratiw"""


class PersonalData(StatesGroup):
    fullname = State()
    email = State()
    photoNum = State()

