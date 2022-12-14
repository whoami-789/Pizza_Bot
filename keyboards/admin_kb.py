from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

b1 = KeyboardButton(' Пицца')
b2 = KeyboardButton(' Салаты')
b3 = KeyboardButton(' Соусы')
snack = KeyboardButton(' Снеки')
drink = KeyboardButton('Напитки')
b4 = KeyboardButton('32')
b5 = KeyboardButton('36')
b6 = KeyboardButton('38')
drink_1 = KeyboardButton('0.5')
drink_2 = KeyboardButton('1')
back = KeyboardButton('Назад')
add = KeyboardButton('Добавить позицию в меню')
order = KeyboardButton('🛎 Заказать')
cancel = KeyboardButton('❗Отмена')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin_main = ReplyKeyboardMarkup(resize_keyboard=True)
drink_kb = ReplyKeyboardMarkup(resize_keyboard=True)

inline_resive = InlineKeyboardButton('✅ Принять заказ', callback_data='Принять заказ')
inline_resive_done = InlineKeyboardButton('✅ Принято', callback_data='✅')
inline_kb_recive = InlineKeyboardMarkup().row(inline_resive)
inline_kb_recive_done = InlineKeyboardMarkup().row(inline_resive_done)

kb_admin_main.row(order, add)
kb_admin.row(back).row(b1, b2).row(b3, snack, drink)
kb_admin1.row(b4, b5, b6).row(cancel)
drink_kb.row(drink_1, drink_2).row(cancel)
