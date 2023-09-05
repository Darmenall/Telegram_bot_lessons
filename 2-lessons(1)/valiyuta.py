"""
    Python:Tg_bot

    Avtor: Darmen Allambergenov

    Tema: API
    https://github.com/public-apis/public-apis#currency-exchange
    Exchangerate-api# Documentetion #Pair Conversion#
"""
import requests
from aiogram import Bot, Dispatcher, executor, types
from tokens import TOKEN_API, API_VALYUTA

url = f"https://v6.exchangerate-api.com/v6/{API_VALYUTA}/pair/USD/UZS"
response = requests.get(url)
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalamu aleykum botg'a xosh kelidin'iz")



@dp.message_handler(commands=['valiyuta'])  #teksitli xabarlardi uslaydi
async def sendWiki(message: types.Message):
    try:
        kurs = response.json()['conversion_rate']
        kursi = f"bugingi kurs: 1AQSh dollari {kurs} so'm"
        await message.answer(kursi)
    except:
        pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
