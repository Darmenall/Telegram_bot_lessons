import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import db

# Tiwrli knopkalar ushin CallbackData-obektlerdi jaratip alamiz
menu_cd = CallbackData("show_menu", "level", "category", "subcategory", "item_id")
buy_item = CallbackData("buy", "item_id")  # clicg'a jalg'asaq boladi bizlerde buy, item_id qaytadi


# Tomendegi funksiya jardeminde menudagi ha'r bir element ushin calbback data jaratib alinadi
# Eger zat kategoriyasi, ost-kategoriyasi ha'm id sanlari berilmegen bolsa 0 ge ten' boladi
def make_callback_data(level, category="0", subcategory="0", item_id="0"):
    return menu_cd.new(
        level=level, category=category, subcategory=subcategory, item_id=item_id
    )


# Bizlerdin menuda 3 etaj (LEVEL) dan ibarat
# 0 - Kategoriyalar
# 1 - Ost-kategoriyalar
# 2 - zatlar
# 3 - Jalgiz zatlar


# Kategoriyalar ushin keyboard jaratip alamiz
async def categories_keyboard():
    # Eng joqaridagi 0-etajdagi ekenin' ko'rsetemiz
    CURRENT_LEVEL = 0

    # Keyboard jaratamiz
    markup = InlineKeyboardMarkup(row_width=1)

    # Bazadagi hamme kategoriyalardi alamiz
    categories = await db.get_categories()
    # Har bir kategoriya ushin tomendegilerdi isleymiz:
    for category in categories:
        # Kategoriyaga tiysli zatlarlar sanini tawamiz
        number_of_items = await db.count_products(category["category_code"])

        # knopka tekstin jaratip alamiz
        button_text = f"{category['category_name']} ({number_of_items} dana)"

        # knopka basganda qaytaruwshi callbackni jaratamiz: Keyingi basqich +1 ha'm kategoriyalar
        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1, category=category["category_code"]
        )

        # knopkani keyboardga qo'samiz
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Keyboardi qaytaramiz
    return markup


# Berilgen kategoriya astidagi kategoriyalarni qaytaruvchi keyboard
async def subcategories_keyboard(category):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=1)

    # Kategoriya astidagi kategoriyalarni bazadan alamiz
    subcategories = await db.get_subcategories(category)
    for subcategory in subcategories:
        # Kategoriyada neshe  zatlar barligini tekseremiz
        number_of_items = await db.count_products(
            category_code=category, subcategory_code=subcategory["subcategory_code"]
        )

        # knopka tekstin jaratip alamiz
        button_text = f"{subcategory['subcategory_name']} ({number_of_items} dona)"

        # knopka basganda qaytaruwshi callbackni jaratamiz: Keyingi basqich +1 ha'm kategoriyalar
        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1,
            category=category,
            subcategory=subcategory["subcategory_code"],
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Ortga qaytariwshi knopka jaratamiz (jaqaridagi etajga qaytamiz)
    markup.row(
        InlineKeyboardButton(
            text="⬅️Artga", callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
        )
    )
    return markup


# astkategoriyaga tiysli zatlar ushun keyboard jasaymiz
async def items_keyboard(category, subcategory):
    CURRENT_LEVEL = 2

    markup = InlineKeyboardMarkup(row_width=1)

    # ast-kategorioyaga tiysli barche zatlardi alamiz
    items = await db.get_products(category, subcategory)
    for item in items:
        #  knopka tekstin jaratip alamiz
        button_text = f"{item['productname']} - ${item['price']}"

        # knopka basganda qaytaruwshi callbackni jaratamiz: Keyingi basqich +1 ha'm kategoriyalar
        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1,
            category=category,
            subcategory=subcategory,
            item_id=item["id"],
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # artga qaytiw knopkasi
    markup.row(
        InlineKeyboardButton(
            text="⬅️Artga",
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 1, category=category
            ),
        )
    )
    return markup


# Berilgen zatlar uchin Satip Aliw ha'm Artga jaziwlardi shigariwshi knopka keyboard
def item_keyboard(category, subcategory, item_id):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(
        InlineKeyboardButton(
            text=f"🛒 Satip Aliw", callback_data=buy_item.new(item_id=item_id)
        )
    )
    markup.row(
        InlineKeyboardButton(
            text="⬅️Artga",
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 1, category=category, subcategory=subcategory
            ),
        )
    )
    return markup