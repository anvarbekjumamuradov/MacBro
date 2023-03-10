from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db


main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

main_menu.row("Apple Gadjetlari")
main_menu.row("Savatcha đ", "Buyurtmalarim đ")
main_menu.row("Sozlamalar âī¸", "Hamyonim đ°")

back_btn = KeyboardButton(text="ORQAGA âŠī¸")
cart_btn = KeyboardButton(text="Savatcha đ")

cats = db.select_all_cats()

cats_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
cats_markup.add(back_btn, cart_btn)

for cat in cats:
    cats_markup.insert(KeyboardButton(text=cat[1]))


def make_products_markup(cat_id):
    products = db.select_all_products(cat_id=cat_id)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(back_btn, cart_btn)
    for product in products:
        markup.insert(KeyboardButton(text=product[1]))
    return markup

numbers = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

for num in range(1, 10):
    numbers.insert(KeyboardButton(text=str(num)))
numbers.add(back_btn)


def cart_products_markup(items):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(text="Buyurtma berish đ"))
    for item in items:
        data = db.get_product_data(id=item[0])
        markup.add(KeyboardButton(text=f"â {data[1]} â"))
    markup.add(back_btn, KeyboardButton(text="đ Bo'shatish"))
    return markup


phone = KeyboardButton(text="đ Telefon Raqam", request_contact=True)
location = KeyboardButton(text="đ Joylashuvni yuborish", request_location=True)
cancel = KeyboardButton("â Bekor qilish â")
