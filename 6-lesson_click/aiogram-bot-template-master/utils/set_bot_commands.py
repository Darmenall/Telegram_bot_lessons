from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botti iske qosiw"),
            types.BotCommand("help", "Jardem"),
            types.BotCommand("kitap", "Kitap satip aliw"),
            types.BotCommand("lesson", "Videouroklardi satip aliw"),
            types.BotCommand("zatlar", "Satip aliw mumkin bolg'an zatlar"),
        ]
    )
