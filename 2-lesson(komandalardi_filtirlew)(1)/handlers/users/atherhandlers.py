from aiogram import types
from aiogram.dispatcher import filters
from loader import dp


#IsReplyFilter xabarga otv qaytariw
@dp.message_handler(is_reply=True, commands="user_id")
async def reply_filter_example(msg: types.Message):
    await msg.answer(msg.reply_to_message.from_user.id)


# IsSenderContact paydalaniwshi ozinin kontaktin jiberse orinlanadi
@dp.message_handler(content_types='contact', is_sender_contact=True)
async def sender_contact_example(msg: types.Message):
    await msg.answer("Raxmet, kontaktin'iz qabil etildi!")


#ForwardedMessageFilter birewdin xabarin botg'a jibergen bolsa
@dp.message_handler(is_forwarded=True)
async def forwarded_example(msg: types.Message):
    await msg.answer("Birewdinxabarin magan jiberip atirsizba?")


#ChatTypeFilter chattin turleri ms:PRIVATE bot pn licni jazisiw, GRUP, CHANNEL,SUPER_GROUP
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands='lichka')
async def chat_type_example(msg: types.Message):
    await msg.answer("Bul licni chat")



