from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product


python_lessons = Product(
    title="Python leorning",   # tema
    description="Videog'a to'lew qiliw ushin tomendegi knopkani basin'.",   # podtema
    currency="UZS",   #valiyuta
    prices=[
        LabeledPrice(
            label="Lessons",
            amount=15000000,   # 150000 so'm
        ),
        LabeledPrice(
            label="Skitka",
            amount=-1000000,  #10000 so'm
        ),
    ],
    start_parameter="create_invoice_python_lesson",   # STARTI
    photo_url = 'https://images.unsplash.com/photo-1624953587687-daf255b6b80a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cHl0aG9ufGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60',
    photo_width=851,
    photo_height=1280,

    need_email=True,  # paydalaniwshinin' email jaziwi shart
    need_name=True,
    need_phone_number=True,
)
python_book = Product(
    title="Python leorning",
    description="Kitap g'a to'lew qiliw ushin tomendegi knopkani basin'.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Book",
            amount=5000000,
        ),
        LabeledPrice(
            label="Jetkizip beriw (7-kun)",
            amount=1000000,
        ),
    ],
    start_parameter="create_invoice_python_book",
    is_flexible=True,  # jetkerip beriw ushin
    photo_url='https://images-cdn.ubuy.co.in/643bd37d2b22684eb652eb89-python-programming-the-complete-guide.jpg',
    photo_width=851,
    photo_height=1280,   # jetkerip beriw ushin
    need_name=True,  # paydalaniwshinin' ati
    need_phone_number=True,   # paydalaniwshinin'nomeri
    need_shipping_address=True,  # paydalaniwshinin' adresi

)


REGULAR_SHIPPING = types.ShippingOption(   # jetkizip beriw 1-usili
    id='post_reg',
    title="Fargo (3-kun)",
    prices=[
        LabeledPrice(
            "karobka", 1000000),
        LabeledPrice(
            "3 kun ishinde jetkizip beriw", 1000000),
    ],
)
FAST_SHIPPING = types.ShippingOption(  #jetkizip beriw 1-usili
    id='post_reg',
    title="Expess pochta (1-kun)",  # tez jetkizip beriw
    prices=[
        LabeledPrice(
            "1-kun ishinde jetkizip beriw", 1000000),
    ],
)
PICKUP_SHIPPING = types.ShippingOption(id="pickup",
                                       title="Texnoparkten alip ketiw",
                                       prices=[
                                           LabeledPrice("Jetkizip beriwsiz",-1000000)
                                       ])

