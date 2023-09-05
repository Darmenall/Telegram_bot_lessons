from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5960175849:AAEzEJMFMkh9h8vj1DcsTdOw6QEWlJOnBX0'

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Xosh kelibsiz menin botima")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
