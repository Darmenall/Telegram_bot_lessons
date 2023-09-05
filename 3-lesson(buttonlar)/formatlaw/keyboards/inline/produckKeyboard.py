from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import course_callback, book_callback

# 1-usil
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
      [
          InlineKeyboardButton(text="💻 Kurslar", callback_data="courses"),
          InlineKeyboardButton(text="📚 Kitablar", callback_data="books"),
      ],
      [
          InlineKeyboardButton(text="Darmennin kursi", url="t.me/darmen_all"),
      ],
      [
          InlineKeyboardButton(text="🔎 Qidiriw", switch_inline_query_current_chat=""),
      ],
      [
          InlineKeyboardButton(text="✉️ Tarqatiw", switch_inline_query="Zo'r bot eken"),
      ],
    ])





# Kurslar ushin keyboard 2-usil
coursesMenu = InlineKeyboardMarkup(row_width=1)

python = InlineKeyboardButton(text="🐉 Python Dasturlew tili", callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)

django = InlineKeyboardButton(text="🌍 Django Web Dasturlew", callback_data=course_callback.new(item_name ="django"))
coursesMenu.insert(django)

telegram = InlineKeyboardButton(text="📱 Telegram bot ", callback_data="course:telegram")
coursesMenu.insert(telegram)

algoritm = InlineKeyboardButton(text="📈Mag'liwmat structurasi ha'm algoritm", callback_data="course:algoritm")
coursesMenu.insert(algoritm)

back_button = InlineKeyboardButton(text="🔙 artg'a", callback_data="cancel")
coursesMenu.insert(back_button)






# 3-usil


books = {
    "Python.Daslurlew tili": "python_book",
    "C++. Dasturlew tili": "cpp_book",
    "Puxta Dasturlew. JavaScript": "js_book",
}


booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
booksMenu.insert(back_button)






# ha'r bit kurs ushin button
telegram_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Satip aliw", url="t.me/darmen_all")
    ]
])

algoritm_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Koriw", url="t.me/darmen_all")
    ]
])



