"""
    Python:Tg_bot

    Avtor: Darmen Allambergenov

    Tema: Metodologiya. Wiki_bot

    request arqali serverge xabar
    serverden bizlerge json formatta keledi

    Waterfall Plan:                 Agile Plan:
    1)talablardi aniqlastiriw.      1)Planning
    2)Reje/Dizayn                   2)Analysis
    3)Coding                        3)Design
    4)Test.                         4)Implementation
    5)Deploy-tarqatiw.              5)Testing & Integration
    6)Texnik xizmet korsetiw        6)Maintenance

    Talablardi aniqlaw:
    1)Paydalaniwshi botga xabar jiberedi.
    2)Botimiz xabardi alip wikipediadan sol temag'a bayanisli textti qaytaradi.
    3)Eger onday mag'liwmat joq bolsa "bunday mag'liwmat joq" dep qaytaradi.

    Reje:
    1)Paydalaniwshilar murajaat qiliw ushin bot(Botfather)
    2)wikipedia menen islewdi uyreniw.
    3)bottin backendin' jaratiw ha'm wikipedia menen jalg'aw.
                        aiogram.dev,
                        pipenv install aiogramm
                        pip install wikipedia

"""
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
from tokens import TOKEN_API

wikipedia.set_lang("uz")
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalamu aleykum botg'a xosh kelidin'iz")


@dp.message_handler()  #teksitli xabarlardi uslaydi
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.reply(respond)
    except:
        await message.reply("Bunday mag'liwmat joq!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




