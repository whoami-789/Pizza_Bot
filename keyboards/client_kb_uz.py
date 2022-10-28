from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

location = KeyboardButton('🌏Joylashuvni yuborish', request_location=True)
phone = KeyboardButton('📱Telefon raqamini yuborish', request_contact=True)
kafe_1 = KeyboardButton('Yakkasaroy, Sharafa Rashidov koch. 40V')
kafe_2 = KeyboardButton('Sergeli, Atrof-muhit koch. 3')
delivery = KeyboardButton('🚗Yetkazib berish')
self = KeyboardButton('🏢Termoq')
piza = KeyboardButton('🍕 Pitsa')
salad = KeyboardButton('🥗 Salatlar')
souse = KeyboardButton('🧂 Souslar')
snack = KeyboardButton('🍟 Aperatiflar')
drink = KeyboardButton('🥤 Ichimliklar')
mini_pizza = KeyboardButton('🍕 Mini pitsa')
sets = KeyboardButton("🗂 To'plamlar")
order = KeyboardButton('🛎 Buyurtma berish')
myorders = KeyboardButton('📜 Mening buyurtmalarim')
feedback = KeyboardButton('📞 Qayta aloqa')
main_menu = KeyboardButton('🔙 Asosiy menyuga')
back_to_menu = KeyboardButton('◀ Menyuga qaytish')
basket = KeyboardButton('🛒 Savat')
clear = KeyboardButton("🌀 Savatni bo'shatish")
continue_order = KeyboardButton('▶️Buyurtmani davom eting')
send_order = KeyboardButton('📤Buyurtmani yuboring')
user_data = KeyboardButton('Mening tafsilotlarim')
cancel = KeyboardButton('❗Bekor qilish')
make_order = KeyboardButton("👍🏽Tekshirib ko'rmoq")

margarita = KeyboardButton('Margarita')
chick = KeyboardButton("TOVUQ VA QO'ZIQORINLI")
cheeze = KeyboardButton("To'rt xil PISHLOQ")
pep = KeyboardButton('Peperoni')
kombi = KeyboardButton('Kombi')
selfie = KeyboardButton('Selfi')
salam = KeyboardButton('Salomaleykum')
sezar = KeyboardButton('Sezar')
veg = KeyboardButton('Vegetarianli')
tuna = KeyboardButton('Tuna bilan ajoyib pizza')
seafood = KeyboardButton('Dengiz mahsulotlari')
kebab = KeyboardButton('Shashlik')
burger = KeyboardButton('Pitsa-Burger')


pizasouse = KeyboardButton('Pitsa sous')
ketchup = KeyboardButton('Kechup')
cheezesouse = KeyboardButton('Pishloqli')
barby = KeyboardButton('Barbekyu')
garlic = KeyboardButton('Kremli sarimsoq')

grecsalat = KeyboardButton('Yunon salatasi')
sezarsalat = KeyboardButton('Sezar salatasi')

frenchfries = KeyboardButton('Kartoshka fri')
potato = KeyboardButton('Rustik kartoshka')
nagets = KeyboardButton('Tovuqli nagets')
chkub = KeyboardButton('Pishloq kublari')
it_mesh = KeyboardButton('Italiya mishmashi')


pepsi = KeyboardButton('Pepsi kola')
water = KeyboardButton('Gazlangan suv')
sok = KeyboardButton('Sharbatlar litr')
fanta = KeyboardButton('Fanta')


mini_margarita = KeyboardButton('Mini Margarita')
mini_chick = KeyboardButton("Mini TOVUQ VA QO'ZIQORINLI")
mini_cheeze = KeyboardButton("Mini To'rt xil PISHLOQ")
mini_pep = KeyboardButton('Mini Peperoni')
mini_kombi = KeyboardButton('Mini Kombi')
mini_selfie = KeyboardButton('Mini Selfi')
mini_salam = KeyboardButton('Mini Salomaleykum')
mini_sezar = KeyboardButton('Mini Sezar')
mini_veg = KeyboardButton('Mini Vegetarianli')
mini_tuna = KeyboardButton('Mini Tuna bilan pizza')
mini_seafood = KeyboardButton('С морепродуктами')
mini_kebab = KeyboardButton('Mini Shashlik')

set_burger_bomba = KeyboardButton('Bomba Burger')
set_bomba = KeyboardButton('Bomba')

# Inline buttons
inline_to_basket = InlineKeyboardButton("🛒 Savatga qo'shish", callback_data='add_pizza_to_cart_uz')
inline_to_basket_other = InlineKeyboardButton("🛒 Savatga qo'shish", callback_data='add_other_to_cart_uz')
inline_make_order = InlineKeyboardButton("👍🏽Tekshirib ko'rmoq", callback_data='make_order_uz')
inline_remove = InlineKeyboardButton('❌', callback_data='delete_cart')
inline_size_32 = InlineKeyboardButton('32 sm', callback_data='32_uz')
inline_size_36 = InlineKeyboardButton('36 sm', callback_data='36_uz')
inline_size_38 = InlineKeyboardButton('38 sm', callback_data='38_uz')
inline_size_32_1 = InlineKeyboardButton('✔️32 sm', callback_data='32_uz')
inline_size_36_1 = InlineKeyboardButton('✔️36 sm', callback_data='36_uz')
inline_size_38_1 = InlineKeyboardButton('✔️38 sm', callback_data='38_uz')
inline_dsize_1 = InlineKeyboardButton('1 litr', callback_data='1_uz')
inline_dsize_0_5 = InlineKeyboardButton('0,5 litr', callback_data='0.5_uz')
inline_dsize_1_1 = InlineKeyboardButton('✔1 litr', callback_data='1_uz')
inline_dsize_0_5_1 = InlineKeyboardButton('✔0,5 litr', callback_data='0.5_uz')
inline_plus = InlineKeyboardButton(text='➕', callback_data='plus_uz')
inline_minus = InlineKeyboardButton(text='➖', callback_data='minus_uz')
inline_phone = InlineKeyboardButton('Bizning instagram', url='https://www.instagram.com/selfie_pizza_uz/')
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