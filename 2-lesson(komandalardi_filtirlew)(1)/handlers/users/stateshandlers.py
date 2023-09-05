from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp

@dp.message_handler(commands='aliw')
async def text_example(msg: types.Message, state:FSMContext):
    """paydalaniwsgini bit state ishine kiritemiz"""
    await state.set_state('aliw_state')
    await msg.answer("zat tag'lan'")

@dp.message_handler(state='aliw_state')
async def text_example(msg: types.Message, state:FSMContext):
    """paydalaniwsgini bit state ishine kiritemiz"""
    await msg.answer("zat satip alindi")
    await state.finish()