from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

location = KeyboardButton('πSubmit Location', request_location=True)
phone = KeyboardButton('π±Send phone number', request_contact=True)
kafe_1 = KeyboardButton('Yakkasaray district, Sharaf Rashidov st. 40V')
kafe_2 = KeyboardButton('Sergeli district, Environment st. 3')
delivery = KeyboardButton('πDelivery')
self = KeyboardButton('π’Pickup')
piza = KeyboardButton('π Pizza')
salad = KeyboardButton('π₯ Salads')
souse = KeyboardButton('π§ Sauces')
snack = KeyboardButton('π Snacks')
drink = KeyboardButton('π₯€ Beverages')
mini_pizza = KeyboardButton('π Mini pizza')
sets = KeyboardButton("π Sets")
order = KeyboardButton('π Order')
myorders = KeyboardButton('π My orders')
feedback = KeyboardButton('π Feedback')
main_menu = KeyboardButton('π To main menu')
back_to_menu = KeyboardButton('β Back to menu')
continue_order = KeyboardButton('βΆοΈContinue checkout')
send_order = KeyboardButton('π€Send order')
basket = KeyboardButton('π Cart')
clear = KeyboardButton('π Clear the cart')
user_data = KeyboardButton('My details')
cancel = KeyboardButton('βCancel')

mark_5 = KeyboardButton('Excellent πππππ')
mark_4 = KeyboardButton('Good ππππ')
mark_3 = KeyboardButton('Nice πππ')
mark_2 = KeyboardButton('So-so ππ')
mark_1 = KeyboardButton('Bad π')
mark_none = KeyboardButton('I do not want')

margarita = KeyboardButton('Margarrita')
chick = KeyboardButton('Chicken with mushrooms')
cheeze = KeyboardButton('FOUR CHEESES')
kebab = KeyboardButton('Kebab')
pep = KeyboardButton('Pepperoni')
kombi = KeyboardButton('Combined')
selfie = KeyboardButton('Selfie')
salam = KeyboardButton('Salamaleykum')
sezar = KeyboardButton('Cesar')
veg = KeyboardButton('Vegetarian')
tuna = KeyboardButton('Gourmet pizza with tuna')
seafood = KeyboardButton('Seafood pizza')
burger = KeyboardButton('Pizza Burger')

pizasouse = KeyboardButton('Pizza sauce')
ketchup = KeyboardButton('Ketchup')
cheezesouse = KeyboardButton('Cheesy')
barby = KeyboardButton('Barbecue')
garlic = KeyboardButton('Creamy garlic')

grecsalat = KeyboardButton('Greek salad')
sezarsalat = KeyboardButton('Caesar salad')

frenchfries = KeyboardButton('French fries')
potato = KeyboardButton('Rustic potatoes')
nagets = KeyboardButton('Chicken nuggets')
chkub = KeyboardButton('Cheese cubes')
it_mesh = KeyboardButton('Italian mishmash')

pepsi = KeyboardButton('Pepsi cola')
water = KeyboardButton('Sparkling water')
sok = KeyboardButton('Juices liter')
fanta = KeyboardButton('Fannta')

mini_margarita = KeyboardButton('Mini Margarrita')
mini_chick = KeyboardButton('Mini Chicken with mushrooms')
mini_cheeze = KeyboardButton('Mini FOUR CHEESES')
mini_pep = KeyboardButton('Mini Pepperoni')
mini_kombi = KeyboardButton('Mini Combined')
mini_selfie = KeyboardButton('Mini Selfie')
mini_salam = KeyboardButton('Mini Salamaleykum')
mini_sezar = KeyboardButton('Mini Cesar')
mini_veg = KeyboardButton('Mini Vegetarian')
mini_tuna = KeyboardButton('Mini Pizza with tuna')
mini_seafood = KeyboardButton('Π‘ ΠΌΠΎΡΠ΅ΠΏΡΠΎΠ΄ΡΠΊΡΠ°ΠΌΠΈ')
mini_kebab = KeyboardButton('Mini Kebab')

set_burger_bomba = KeyboardButton('Bomb Burger')
set_bomba = KeyboardButton('Bomb')

# Inline buttons
inline_to_basket = InlineKeyboardButton('π Add to Cart', callback_data='add_pizza_to_cart_eng')
inline_to_basket_other = InlineKeyboardButton('π Add to Cart', callback_data='add_other_to_cart_eng')
inline_make_order = InlineKeyboardButton('ππ½Checkout', callback_data='make_order_eng')
inline_remove = InlineKeyboardButton('β', callback_data='delete_cart')
inline_size_32 = InlineKeyboardButton('32 sm', callback_data='32_eng')
inline_size_32_b = InlineKeyboardButton('32 sm', callback_data='32_eng_b')
inline_size_36 = InlineKeyboardButton('36 sm', callback_data='36_eng')
inline_size_38 = InlineKeyboardButton('38 sm', callback_data='38_eng')
inline_size_32_1 = InlineKeyboardButton('βοΈ32 sm', callback_data='32_eng')
inline_size_32_1_b = InlineKeyboardButton('βοΈ32 sm', callback_data='32_eng_b')
inline_size_36_1 = InlineKeyboardButton('βοΈ36 sm', callback_data='36_eng')
inline_size_38_1 = InlineKeyboardButton('βοΈ38 sm', callback_data='38_eng')
inline_dsize_1 = InlineKeyboardButton('1 liter', callback_data='1_eng')
inline_dsize_0_5 = InlineKeyboardButton('0,5 liter', callback_data='0.5_eng')
inline_dsize_1_1 = InlineKeyboardButton('β1 liter', callback_data='1_eng')
inline_dsize_0_5_1 = InlineKeyboardButton('β0,5 liter', callback_data='0.5_eng')
inline_plus = InlineKeyboardButton(text='β', callback_data='plus_eng')
inline_minus = InlineKeyboardButton(text='β', callback_data='minus_eng')
inline_phone = InlineKeyboardButton('Our instagram', url='https://www.instagram.com/selfie_pizza_uz/')
inline_kb_pizza = InlineKeyboardMarkup().row(inline_size_32, inline_size_36, inline_size_38).row(inline_to_basket)
inline_kb_pizza_32 = InlineKeyboardMarkup().row(inline_size_32_1, inline_size_36, inline_size_38).row(inline_to_basket)
inline_kb_pizza_36 = InlineKeyboardMarkup().row(inline_size_32, inline_size_36_1, inline_size_38).row(inline_to_basket)
inline_kb_pizza_38 = InlineKeyboardMarkup().row(inline_size_32, inline_size_36, inline_size_38_1).row(inline_to_basket)
inline_kb_drink = InlineKeyboardMarkup().row(inline_dsize_0_5, inline_dsize_1).row(inline_to_basket)
inline_kb_pizza_0_5 = InlineKeyboardMarkup().row(inline_dsize_0_5_1, inline_dsize_1).row(inline_to_basket)
inline_kb_pizza_1 = InlineKeyboardMarkup().row(inline_dsize_0_5, inline_dsize_1_1).row(inline_to_basket)
inline_kb_phone = InlineKeyboardMarkup().add(inline_phone)
inline_cart = InlineKeyboardMarkup().row(inline_minus, inline_plus).row(inline_remove)
inline_order = InlineKeyboardMarkup().add(inline_make_order)
inline_kb_salat_snack_souse = InlineKeyboardMarkup().add(inline_to_basket_other)
inline_size_20 = InlineKeyboardButton('20 sm', callback_data='20_eng')
inline_size_20_1 = InlineKeyboardButton('βοΈ20 sm', callback_data='20_eng')
inline_kb_pizza_burger = InlineKeyboardMarkup().row(inline_size_32_b, inline_size_20).row(inline_to_basket)
inline_kb_pizza_burger_32 = InlineKeyboardMarkup().row(inline_size_32_1_b, inline_size_20).row(inline_to_basket)
inline_kb_pizza_burger_20 = InlineKeyboardMarkup().row(inline_size_32, inline_size_20_1).row(inline_to_basket)

kb_language = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_pizza = ReplyKeyboardMarkup(resize_keyboard=True)
kb_souse = ReplyKeyboardMarkup(resize_keyboard=True)
kb_salat = ReplyKeyboardMarkup(resize_keyboard=True)
kb_snack = ReplyKeyboardMarkup(resize_keyboard=True)
kb_drink = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mini_pizza = ReplyKeyboardMarkup(resize_keyboard=True)
kb_sets = ReplyKeyboardMarkup(resize_keyboard=True)
kb_phone = ReplyKeyboardMarkup(resize_keyboard=True)
kb_address = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kafe = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mydata = ReplyKeyboardMarkup(resize_keyboard=True)
kb_del_or_self = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cart = ReplyKeyboardMarkup(resize_keyboard=True)
marks = ReplyKeyboardMarkup(resize_keyboard=True)
dont_want = ReplyKeyboardMarkup(resize_keyboard=True)
kb_back_to_menu = ReplyKeyboardMarkup(resize_keyboard=True)
make_order = KeyboardButton("ππ½Checkout")

kb_main.add(order).row(myorders, user_data, feedback)
kb_menu.row(main_menu, basket).row(piza, mini_pizza).row(drink, salad).row(souse, snack, sets)
kb_pizza.add(back_to_menu).add(veg, tuna) \
    .add(margarita, chick).add(cheeze, pep) \
    .add(kombi, salam).add(selfie, kebab).row(burger, sezar)

kb_souse.add(back_to_menu).add(pizasouse, ketchup) \
    .add(cheezesouse, barby).add(garlic)

kb_salat.add(back_to_menu).add(grecsalat, sezarsalat)

kb_snack.add(back_to_menu).add(frenchfries, potato).add(nagets, chkub).row(it_mesh)

kb_drink.add(back_to_menu, pepsi).add(water, sok).row(fanta)

kb_mini_pizza.row(back_to_menu, mini_margarita).row(mini_chick, mini_cheeze).row(mini_pep, mini_kombi). \
    row(mini_selfie, mini_salam).row(mini_sezar, mini_veg).row(mini_tuna, mini_kebab)

kb_sets.row(back_to_menu).row(set_burger_bomba, set_bomba)

kb_mydata.add(phone, main_menu)

kb_phone.add(phone, continue_order).row(back_to_menu)

kb_address.add(location, send_order).row(main_menu)

kb_kafe.row(kafe_1, kafe_2).row(main_menu, back_to_menu)

kb_cart.row(make_order).row(clear, back_to_menu)

marks.row(mark_none, mark_5, mark_4).row(mark_3, mark_2, mark_1)

dont_want.add(mark_none)

kb_del_or_self.add(delivery, self)

kb_back_to_menu.add(back_to_menu)
