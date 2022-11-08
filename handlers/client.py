from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import bot, dp
from keyboards import client_kb_ru, client_kb_eng, client_kb_uz
from sql import sql_db

ID = None


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await sql_db.save_user(message)
    try:
        await bot.send_message(message.from_user.id,
                               'Assalomu alaykum! Selfie Pizza yetkazib berish xizmatiga xush kelibsiz.\n\n' +
                               'Здравствуйте! Добро пожаловать в службу доставки Selfie Pizza.\n\n'
                               'Hello! Welcome to Selfie Pizza Delivery Service.',
                               reply_markup=client_kb_ru.kb_language)
    except:
        await message.reply('Общение с ботом в лс, напиши ему')


@dp.message_handler(commands=['num'])
async def comm(message: types.Message):
    await sql_db.check_number(message)


@dp.message_handler(text=['🇷🇺 Русский', "🇺🇿 O'zbek tili", '🇬🇧 English'])
async def command_language(message: types.Message):
    if message.text == '🇷🇺 Русский':
        await sql_db.save_user_lang(message)
        await message.answer('Выбран Русский язык', reply_markup=client_kb_ru.kb_main)
    elif message.text == "🇺🇿 O'zbek tili":
        await sql_db.save_user_lang_uz(message)
        await message.answer("O‘zbek tili tanlandi", reply_markup=client_kb_uz.kb_main)
    elif message.text == '🇬🇧 English':
        await sql_db.save_user_lang_eng(message)
        await message.answer('English selected', reply_markup=client_kb_eng.kb_main)


@dp.message_handler(commands=['chat_id'])
async def chat_id(message: types.Message):
    await message.reply(message.chat.id)


class FSMPizza(StatesGroup):
    name = State()
    size = State()
    id = State()


class FSMSnack(StatesGroup):
    name = State()
    id = State()


@dp.message_handler(Text(equals=['🍕 Пицца', '🍕 Pizza', '🍕 Pitsa']))
async def command_menu(message: types.Message):
    await FSMPizza.name.set()
    if message.text == '🍕 Пицца':
        await message.answer('Выберите пиццу', reply_markup=client_kb_ru.kb_pizza)
    elif message.text == '🍕 Pizza':
        await message.answer('Choose a pizza', reply_markup=client_kb_eng.kb_pizza)
    elif message.text == '🍕 Pitsa':
        await message.answer('Pitsa tanlang', reply_markup=client_kb_uz.kb_pizza)


@dp.message_handler(Text(equals=['🥗 Салаты', '🥗 Salads', '🥗 Salatlar']))
async def command_menu(message: types.Message):
    await FSMSnack.name.set()
    if message.text == '🥗 Салаты':
        await message.answer('Выберите салат', reply_markup=client_kb_ru.kb_salat)
    elif message.text == '🥗 Salads':
        await message.answer('Choose a salad', reply_markup=client_kb_eng.kb_salat)
    elif message.text == '🥗 Salatlar':
        await message.answer('Salatni tanlang', reply_markup=client_kb_uz.kb_salat)


@dp.message_handler(Text(equals=['🧂 Соусы', '🧂 Sauces', '🧂 Souslar']))
async def command_menu(message: types.Message):
    await FSMSnack.name.set()
    if message.text == '🧂 Соусы':
        await message.answer('Выберите соус', reply_markup=client_kb_ru.kb_souse)
    elif message.text == '🧂 Sauces':
        await message.answer('Choose sauce', reply_markup=client_kb_eng.kb_souse)
    elif message.text == '🧂 Souslar':
        await message.answer('Sosingizni tanlang', reply_markup=client_kb_uz.kb_souse)


@dp.message_handler(Text(equals=['🍟 Снеки', '🍟 Snacks', '🍟 Aperatiflar']))
async def command_menu(message: types.Message):
    await FSMSnack.name.set()
    if message.text == '🍟 Снеки':
        await message.answer('Выберите снек', reply_markup=client_kb_ru.kb_snack)
    elif message.text == '🍟 Snacks':
        await message.answer('Choose snack', reply_markup=client_kb_eng.kb_snack)
    elif message.text == '🍟 Aperatiflar':
        await message.answer('Aperatifni tanlang', reply_markup=client_kb_uz.kb_snack)


@dp.message_handler(Text(equals=['🥤 Напитки', '🥤 Beverages', '🥤 Ichimliklar']))
async def command_menu(message: types.Message):
    await FSMPizza.name.set()
    if message.text == '🥤 Напитки':
        await message.answer('Выберите напиток', reply_markup=client_kb_ru.kb_drink)
    elif message.text == '🥤 Beverages':
        await message.answer('Choose a drink', reply_markup=client_kb_eng.kb_drink)
    elif message.text == '🥤 Ichimliklar':
        await message.answer('Ichimlikni tanlang', reply_markup=client_kb_uz.kb_drink)


@dp.message_handler(text=['🍕 Мини пиццы', '🍕 Mini pitsa', '🍕 Mini pizza'])
async def mini_pizza(message: types.Message):
    await FSMSnack.name.set()
    if message.text == '🍕 Мини пиццы':
        await message.answer('Выберите минии пиццу', reply_markup=client_kb_ru.kb_mini_pizza)
    elif message.text == '🍕 Mini pitsa':
        await message.answer('Mini pitsani talang', reply_markup=client_kb_uz.kb_mini_pizza)
    elif message.text == '🍕 Mini pizza':
        await message.answer('Choose mini pizza', reply_markup=client_kb_eng.kb_mini_pizza)


@dp.message_handler(text=['🗂 Сеты', "🗂 To'plamlar", '🗂 Sets'])
async def sets(message: types.Message):
    await FSMSnack.name.set()
    if message.text == '🗂 Сеты':
        await message.answer('Выберите сет', reply_markup=client_kb_ru.kb_sets)
    elif message.text == "🗂 To'plamlar":
        await message.answer("To'plamni talang", reply_markup=client_kb_uz.kb_sets)
    elif message.text == '🗂 Sets':
        await message.answer('Coose set', reply_markup=client_kb_eng.kb_sets)


@dp.message_handler(Text(equals=['🛎 Заказать', '🛎 Order', '🛎 Buyurtma berish']))
async def command_order(message: types.Message):
    await sql_db.create_order_number(message)
    if message.text == '🛎 Заказать':
        await message.answer('Что хотите заказать?\n'
                             'Для выбора другой позиции меню, нажмите по названию 2 раза',
                             reply_markup=client_kb_ru.kb_menu)
    elif message.text == '🛎 Order':
        await message.answer('What do you want to order?', reply_markup=client_kb_eng.kb_menu)
    elif message.text == '🛎 Buyurtma berish':
        await message.answer('Nima buyurtma bermoqchisiz?', reply_markup=client_kb_uz.kb_menu)


@dp.message_handler(Text(equals=['◀ Вернуться в меню', '◀ Back to menu', '◀ Menyuga qaytish']), state='*')
async def command_back_menu(message: types.Message, state: FSMContext):
    await state.finish()
    if message.text == '◀ Вернуться в меню':
        await message.answer('Что хотите заказать?', reply_markup=client_kb_ru.kb_menu)
    elif message.text == '◀ Back to menu':
        await message.answer('What do you want to order?', reply_markup=client_kb_eng.kb_menu)
    elif message.text == '◀ Menyuga qaytish':
        await message.answer('Nima buyurtma bermoqchisiz?', reply_markup=client_kb_uz.kb_menu)


@dp.message_handler(Text(equals=['🔙 В главное меню', '🔙 To main menu', '🔙 Asosiy menyuga']))
async def command_main_menu(message: types.Message):
    await sql_db.delete_order(message)
    if message.text == '🔙 В главное меню':
        await message.answer('Вы в главном меню', reply_markup=client_kb_ru.kb_main)
    elif message.text == '🔙 To main menu':
        await message.answer('You are in the main menu', reply_markup=client_kb_eng.kb_main)
    elif message.text == '🔙 Asosiy menyuga':
        await message.answer('Siz asosiy menyudasiz', reply_markup=client_kb_uz.kb_main)


@dp.message_handler(text=['📞 Обратная связь', '📞 Feedback', '📞 Qayta aloqa'])
async def command_phone(message: types.Message):
    if message.text == '📞 Обратная связь':
        await message.answer('Наш номер телефона:\n +998(90) 824-22-99', reply_markup=client_kb_ru.inline_kb_phone)
    elif message.text == '📞 Feedback':
        await message.answer('Our phone number:\n +998(90) 824-22-99', reply_markup=client_kb_eng.inline_kb_phone)
    elif message.text == '📞 Qayta aloqa':
        await message.answer('Bizning telefon raqamimiz:\n +998(90) 824-22-99',
                             reply_markup=client_kb_uz.inline_kb_phone)


@dp.message_handler(text=['Мои данные', 'My details', 'Mening tafsilotlarim'])
async def save_user_data(message: types.Message):
    if await sql_db.test_user_data(message) != message.chat.id:
        await sql_db.save_user(message)
        await sql_db.show_user_data(message)
        if await sql_db.test_user_phone(message) == 0:
            if message.text == 'Мои данные':
                await message.answer('Нажмите на кнопку для сохранения вашего номера телефона\n'
                                     '(без него доставка невозможна '
                                     '😔)')

            elif message.text == 'My details':
                await message.answer('Click on the button to save your phone number\n'
                                     '(delivery is not possible without it '
                                     '😔)')

            elif message.text == 'Mening tafsilotlarim':
                await message.answer('Telefon raqamingizni saqlash uchun tugmani bosing\n'
                                     '(busiz yetkazib berish mumkin emas'
                                     '😔)')


@dp.message_handler(text=['🛒 Корзина', '🛒 Cart', '🛒 Savat'])
async def cart(message: types.Message, state: FSMContext):
    await state.finish()
    if message.text == '🛒 Корзина':
        await sql_db.show_cart(message)  #
    if message.text == '🛒 Cart':
        await sql_db.show_cart_eng(message)  #
    if message.text == '🛒 Savat':
        await sql_db.show_cart_uz(message)  #


@dp.callback_query_handler(text=['delete_cart', 'delete_cart_uz', 'delete_cart_eng'])
async def delete_cart(callback: types.CallbackQuery):
    if callback.data in 'delete_cart':
        await sql_db.delete_cart(callback)
        await callback.message.delete()
    elif callback.data in 'delete_cart_uz':
        await sql_db.delete_cart_uz(callback)
        await callback.message.delete()
    elif callback.data in 'delete_cart_eng':
        await sql_db.delete_cart_eng(callback)
        await callback.message.delete()


# Пиццы ##########################################################################
@dp.message_handler(text=['Вегетерианская', 'С тунцом', 'Маргарита', 'Курица с грибами', 'Шашлык', 'Четыре сыра',
                          'Пепперони', 'Комбинированная', 'С морепродуктами', 'Селфи', 'Саламалейкум', 'Цезарь',
                          'Пицца-Бургер'],
                    state=FSMPizza.name)
async def command_veg_pizza(message: types.Message, state: FSMContext):
    await sql_db.sql_view_pizza(message)
    await message.answer('Что-бы выбрать другую пиццу кликните по ее названию 2 раза☺')
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMPizza.next()
    print(data)


@dp.message_handler(text=['Margarita', "TOVUQ VA QO'ZIQORINLI", "To'rt xil PISHLOQ", 'Peperoni', 'Kombi', 'Selfi',
                          'Salomaleykum', 'Sezar', 'Vegetarianli', 'Tuna bilan ajoyib pizza', 'Dengiz mahsulotlari',
                          'Shashlik', 'Pitsa-Burger'], state=FSMPizza.name)
async def command_veg_pizza_eng(message: types.Message, state: FSMContext):
    await sql_db.sql_view_pizza_uz(message)
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMPizza.next()
    print(data)
    await message.answer('Boshqa pizza tanlash uchun uning nomiga 2 marta bosing☺')


@dp.message_handler(text=['Margarrita', 'Chicken with mushrooms', 'FOUR CHEESES', 'Kebab', 'Pepperoni',
                          'Combined', 'Selfie', 'Salamaleykum', 'Cesar', 'Vegetarian', 'Gourmet pizza with tuna',
                          'Seafood pizza', 'Pizza Burger'], state=FSMPizza.name)
async def command_veg_pizza_uz(message: types.Message, state: FSMContext):
    await sql_db.sql_view_pizza_eng(message)
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMPizza.next()
    print(data)
    await message.answer('To select another pizza, double-click on its name☺')


# Салаты ##########################################################################
@dp.message_handler(
    text=['Греческий салат', 'Салат Цезарь'],
    state=FSMSnack.name)
async def command_salat_grees(message: types.Message, state: FSMContext):
    await sql_db.sql_view_salat(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()

    await message.answer('Что-бы выбрать другой салат кликните по ее названию 2 раза☺️')


@dp.message_handler(
    text=['Yunon salatasi', 'Sezar salatasi'],
    state=FSMSnack.name)
async def command_salat_grees_uz(message: types.Message, state: FSMContext):
    await sql_db.sql_view_salat_uz(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('Boshqa salat tanlash uchun uning nomiga 2 marta bosing☺️')


@dp.message_handler(
    text=['Greek salad', 'Caesar salad'],
    state=FSMSnack.name)
async def command_salat_grees_eng(message: types.Message, state: FSMContext):
    await sql_db.sql_view_salat_eng(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('To select another salad, double-click on its name☺️')


# Снеки ##########################################################################
@dp.message_handler(text=['Картофель фри', 'Куриные нагетсы', 'Картофель по деревенски', 'Сырные кубики',
                          'Итальянская мешанина'],
                    state=FSMSnack.name)
async def command_snack_fries(message: types.Message, state: FSMContext):
    await sql_db.sql_view_snack(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('Что-бы выбрать другой снек кликните по ее названию 2 раза☺️')


@dp.message_handler(text=[
    'Kartoshka fri', 'Rustik kartoshka', 'Tovuqli nagets', 'Pishloq kublari', 'Italiya mishmashi'],
    state=FSMSnack.name)
async def command_snack_fries_uz(message: types.Message, state: FSMContext):
    await sql_db.sql_view_snack_uz(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('Boshqa gazak tanlash uchun uning nomini 2 marta bosing☺️')


@dp.message_handler(text=[
    'French fries', 'Rustic potatoes', 'Chicken nuggets', 'Cheese cubes', 'Italian mishmash'],
    state=FSMSnack.name)
async def command_snack_fries_eng(message: types.Message, state: FSMContext):
    await sql_db.sql_view_snack_eng(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('To select another snack, click on its name 2 times☺️')


# Соусы ##########################################################################
@dp.message_handler(text=['Пицца соус', 'Сырный', 'Кетчуп', 'Барбекью', 'Сливочно-чесночный'], state=FSMSnack.name)
async def command_souse_pizza(message: types.Message, state: FSMContext):
    await sql_db.sql_view_souse(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('Что-бы выбрать другой соус кликните по ее названию 2 раза☺️')


@dp.message_handler(text=[
    'Pizza sauce', 'Ketchup', 'Cheesy', 'Barbecue', 'Creamy garlic'], state=FSMSnack.name)
async def command_souse_pizza_uz(message: types.Message, state: FSMContext):
    await sql_db.sql_view_souse_eng(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('To select another sauce, click on its name 2 times☺️')


@dp.message_handler(text=[
    'Pitsa sous', 'Kechup', 'Pishloqli', 'Barbekyu', 'Kremli sarimsoq'], state=FSMSnack.name)
async def command_souse_pizza_eng(message: types.Message, state: FSMContext):
    await sql_db.sql_view_souse_uz(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('Boshqa sousni tanlash uchun uning nomini 2 marta bosing☺️')


# Напитки ##########################################################################
@dp.message_handler(text=['Пепси кола', 'Вода с газом', 'Соки литровые', 'Фанта'
                          ], state=FSMPizza.name)
async def command_drink_pepsi(message: types.Message, state: FSMContext):
    await sql_db.sql_view_drink(message)
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)
    await FSMPizza.next()
    await message.answer('Что-бы выбрать другой напиток кликните по ее названию 2 раза☺\n'
                         'если это сок, нажмите на 1 литр')


@dp.message_handler(text=[
    'Pepsi kola', 'Gazlangan suv', 'Sharbatlar litr', 'Fanta'
], state=FSMPizza.name)
async def command_drink_pepsi_uz(message: types.Message, state: FSMContext):
    await sql_db.sql_view_drink_uz(message)
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)
    await FSMPizza.next()
    await message.answer('Boshqa ichimlikni tanlash uchun uning nomiga 2 marta bosing☺\n'
                         'agar u sharbat bolsa, 1 litr bosing')


@dp.message_handler(text=[
    'Pepsi cola', 'Sparkling water', 'Juices liter', 'Fannta'], state=FSMPizza.name)
async def command_drink_pepsi_eng(message: types.Message, state: FSMContext):
    await sql_db.sql_view_drink_eng(message)
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)
    await FSMPizza.next()
    await message.answer('To select another drink, click on its name 2 times☺\n'
                         'if it is juice, press 1 liter')


# Мини пиццы #####################################################################################
@dp.message_handler(
    text=['Мини Маргарита', 'Мини Курица с грибами', 'Мини Пепперони', 'Мини Четыре сыра', 'Мини Комбинированная',
          'Мини Селфи', 'Мини Саламалейкум', 'Мини Цезарь', 'Мини Вегетерианская', 'Мини С тунцом',
          'Мини Шашлык'],
    state=FSMSnack.name)
async def command_mini_pizza(message: types.Message, state: FSMContext):
    await sql_db.sql_view_mini_pizza(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('Что-бы выбрать другую мини пиццу кликните по ее названию 2 раза☺️')


@dp.message_handler(text=[
    'Mini Margarita', "Mini TOVUQ VA QO'ZIQORINLI", "Mini To'rt xil PISHLOQ", 'Mini Peperoni',
    'Mini Kombi', 'Mini Selfi', 'Mini Salomaleykum', 'Mini Sezar', 'Mini Vegetarianli', 'Mini Tuna bilan pizza',
    'Mini Shashlik'], state=FSMSnack.name)
async def command_mini_pizza_uz(message: types.Message, state: FSMContext):
    await sql_db.sql_view_mini_pizza_uz(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('Boshqa mini pitsani tanlash uchun uning nomini 2 marta bosing☺️')


@dp.message_handler(text=[
    'Mini Margarrita', 'Mini Chicken with mushrooms', 'Mini FOUR CHEESES', 'Mini Pepperoni',
    'Mini Combined', 'Mini Selfie', 'Mini Salamaleykum', 'Mini Cesar', 'Mini Vegetarian', 'Mini Pizza with tuna',
    'Mini Kebab'], state=FSMSnack.name)
async def command_mini_pizza_eng(message: types.Message, state: FSMContext):
    await sql_db.sql_view_mini_pizza_eng(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('To select another mini pizza, click on its name 2 times☺️')


# Сеты ####################################################################################################
@dp.message_handler(
    text=['Бомба Бургер', 'Бомба'],
    state=FSMSnack.name)
async def command_set(message: types.Message, state: FSMContext):
    await sql_db.sql_view_sets(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('Что-бы выбрать другой сет кликните по ее названию 2 раза☺️')


@dp.message_handler(text=[
    'Bomba Burger', 'Bomba'], state=FSMSnack.name)
async def command_set_uz(message: types.Message, state: FSMContext):
    await sql_db.sql_view_sets_uz(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer("Boshqa to'plamni tanlash uchun uning nomini 2 marta bosing☺️")


@dp.message_handler(text=[
    'Bomb Burger', 'Bomb'], state=FSMSnack.name)
async def command_set_eng(message: types.Message, state: FSMContext):
    await sql_db.sql_view_sets_eng(message)
    async with state.proxy() as data:
        data['name'] = message.text
    print(data)
    await FSMSnack.next()
    await message.answer('To select another set, click on its name 2 times☺️')


#####################################################################################################################
@dp.callback_query_handler(text='add_pizza_to_cart', state=FSMPizza.id)
async def to_cart(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = callback.message.chat.id
        print(data)
    await sql_db.sql_to_cart_pd(state)
    await state.finish()
    await callback.answer('Добавлено в корзину', show_alert=True)
    await callback.message.answer('Что хотите заказать?', reply_markup=client_kb_ru.kb_menu)


@dp.callback_query_handler(text='add_pizza_to_cart_uz', state=FSMPizza.id)
async def to_cart(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = callback.message.chat.id
        print(data)
    await sql_db.sql_to_cart_pd(state)
    await state.finish()
    await callback.answer("Savatga qo'shildi", show_alert=True)
    await callback.message.answer('Nima buyurtma bermoqchisiz?', reply_markup=client_kb_uz.kb_menu)


@dp.callback_query_handler(text='add_pizza_to_cart_eng', state=FSMPizza.id)
async def to_cart(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = callback.message.chat.id
        print(data)
    await sql_db.sql_to_cart_pd(state)
    await state.finish()
    await callback.answer('Added to cart', show_alert=True)
    await callback.message.answer('What do you want to order?', reply_markup=client_kb_eng.kb_menu)


@dp.message_handler(text=['Вегетерианская', 'С тунцом', 'Маргарита', 'Курица с грибами', 'Шашлык', 'Четыре сыра',
                          'Пепперони', 'Комбинированная', 'С морепродуктами', 'Селфи', 'Саламалейкум', 'Цезарь',
                          'Margarita', "TOVUQ VA QO'ZIQORINLI", "To'rt xil PISHLOQ", 'Peperoni', 'Kombi', 'Selfie',
                          'Salamaleykum', 'Sezar', 'Vegetarianli', 'Tuna bilan ajoyib pizza', 'Dengiz mahsulotlari',
                          'Shashlik', 'Margarrita', 'Chicken with mushrooms', 'FOUR CHEESES', 'Kebab', 'Pepperoni',
                          'Combined', 'Selfie', 'Salamaleykum', 'Ceasar', 'Vegetarian', 'Gourmet pizza with tuna',
                          'Seafood pizza', 'Пицца-Бургер', 'Pitsa-Burger', 'Pizza Burger',
                          'Греческий салат', 'Салат Цезарь', 'Yunon salatasi', 'Sezar salatasi',
                          'Greek salad', 'Caesar salad',
                          'Картофель фри', 'Куриные нагетсы', 'Картофель по деревенски', 'Сырные кубики',
                          'Итальянская мешанина',
                          'Kartoshka fri', 'Rustik kartoshka', 'Tovuqli nagets', 'Pishloq kublari', 'Italiya mishmashi',
                          'French fries', 'Rustic potatoes', 'Chicken nuggets', 'Cheese cubes', 'Italian mishmash',
                          'Пицца соус', 'Сырный', 'Кетчуп', 'Барбекью', 'Сливочно-чесночный',
                          'Pizza sauce', 'Ketchup', 'Cheesy', 'Barbecue', 'Creamy garlic',
                          'Pitsa sous', 'Kechup', 'Pishloqli', 'Barbekyu', 'Kremli sarimsoq',
                          'Пепси кола', 'Вода с газом', 'Соки литровые', 'Фанта',
                          'Pepsi kola', 'Gazlangan suv', 'Sharbatlar litr', 'Fanta',
                          'Pepsi cola', 'Sparkling water', 'Juices liter', 'Fannta', 'Мини Маргарита',
                          'Мини Курица с грибами', 'Мини Пепперони', 'Мини Четыре сыра', 'Мини Комбинированная',
                          'Мини Селфи', 'Мини Саламалейкум', 'Мини Цезарь', 'Мини Вегетерианская', 'Мини С тунцом',
                          'Мини Шашлык', 'Mini Margarita', "Mini TOVUQ VA QO'ZIQORINLI", "Mini To'rt xil PISHLOQ",
                          'Mini Peperoni', 'Mini Kombi', 'Mini Selfi', 'Mini Salomaleykum', 'Mini Sezar',
                          'Mini Vegetarianli', 'Mini Tuna bilan pizza', 'Mini Shashlik', 'Mini Margarrita',
                          'Mini Chicken with mushrooms', 'Mini FOUR CHEESES', 'Mini Pepperoni',
                          'Mini Combined', 'Mini Selfie', 'Mini Salamaleykum', 'Mini Cesar', 'Mini Vegetarian',
                          'Mini Pizza with tuna', 'Mini Kebab', 'Бомба Бургер', 'Бомба', 'Bomba Burger', 'Bomba',
                          'Bomb Burger', 'Bomb'],
                    state='*')
async def change_name(message: types.Message, state: FSMContext):
    if message.text in ['Вегетерианская', 'С тунцом', 'Маргарита', 'Курица с грибами', 'Шашлык', 'Четыре сыра',
                        'Пепперони', 'Комбинированная', 'С морепродуктами', 'Селфи', 'Саламалейкум',
                        'Margarita', "TOVUQ VA QO'ZIQORINLI", "To'rt xil PISHLOQ", 'Peperoni', 'Kombi', 'Selfie',
                        'Salamaleykum', 'Sezar', 'Vegetarianli', 'Tuna bilan ajoyib pizza', 'Dengiz mahsulotlari',
                        'Shashlik', 'Margarrita', 'Chicken with mushrooms', 'FOUR CHEESES', 'Kebab', 'Pepperoni',
                        'Combined', 'Selfie', 'Salamaleykum', 'Ceasar', 'Vegetarian', 'Gourmet pizza with tuna',
                        'Seafood pizza', 'Пепси кола', 'Вода с газом', 'Соки литровые', 'Фанта',
                        'Pepsi kola', 'Gazlangan suv', 'Sharbatlar litr', 'Fanta',
                        'Pepsi cola', 'Sparkling water', 'Juices liter', 'Fannta', 'Пицца-Бургер', 'Pitsa-Burger',
                        'Pizza Burger']:
        await state.reset_state(with_data=True)
        await FSMPizza.name.set()
        await message.delete()
        return
    elif message.text in ['Греческий салат', 'Салат Цезарь', 'Yunon salatasi', 'Sezar salatasi',
                          'Greek salad', 'Caesar salad',
                          'Картофель фри', 'Куриные нагетсы', 'Картофель по деревенски', 'Сырные кубики',
                          'Итальянская мешанина',
                          'Kartoshka fri', 'Rustik kartoshka', 'Tovuqli nagets', 'Pishloq kublari', 'Italiya mishmashi',
                          'French fries', 'Rustic potatoes', 'Chicken nuggets', 'Cheese cubes', 'Italian mishmash',
                          'Пицца соус', 'Сырный', 'Кетчуп', 'Барбекью', 'Сливочно-чесночный',
                          'Pizza sauce', 'Ketchup', 'Cheesy', 'Barbecue', 'Creamy garlic',
                          'Pitsa sous', 'Kechup', 'Pishloqli', 'Barbekyu', 'Kremli sarimsoq', 'Мини Маргарита',
                          'Мини Курица с грибами', 'Мини Пепперони', 'Мини Четыре сыра', 'Мини Комбинированная',
                          'Мини Селфи', 'Мини Саламалейкум', 'Мини Цезарь', 'Мини Вегетерианская', 'Мини С тунцом',
                          'Мини Шашлык', 'Mini Margarita', "Mini TOVUQ VA QO'ZIQORINLI", "Mini To'rt xil PISHLOQ",
                          'Mini Peperoni', 'Mini Kombi', 'Mini Selfi', 'Mini Salomaleykum', 'Mini Sezar',
                          'Mini Vegetarianli', 'Mini Tuna bilan pizza', 'Mini Shashlik', 'Mini Margarrita',
                          'Mini Chicken with mushrooms', 'Mini FOUR CHEESES', 'Mini Pepperoni',
                          'Mini Combined', 'Mini Selfie', 'Mini Salamaleykum', 'Mini Cesar', 'Mini Vegetarian',
                          'Mini Pizza with tuna', 'Mini Kebab', 'Бомба Бургер', 'Бомба', 'Bomba Burger', 'Bomba',
                          'Bomb Burger', 'Bomb']:
        await state.reset_state(with_data=True)
        await FSMSnack.name.set()
        await message.delete()
        return


@dp.callback_query_handler(
    text=['32', '36', '38', '32_eng', '36_eng', '38_eng', '32_uz', '36_uz', '38_uz', '1', '0.5', '1_eng', '0.5_eng',
          '1_uz', '0.5_uz'],
    state='*')
@dp.callback_query_handler(
    text=['32', '36', '38', '32_eng', '36_eng', '38_eng', '32_uz', '36_uz', '38_uz', '1', '0.5', '1_eng', '0.5_eng',
          '1_uz', '0.5_uz'],
    state=FSMPizza.size)
async def command_size(callback: types.CallbackQuery, state: FSMContext):
    if callback.data in '32':
        await callback.message.edit_reply_markup(reply_markup=client_kb_ru.inline_kb_pizza_32)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 32
        await FSMPizza.next()

    elif callback.data in '36':
        await callback.message.edit_reply_markup(reply_markup=client_kb_ru.inline_kb_pizza_36)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 36
        await FSMPizza.next()

    elif callback.data in '38':
        await callback.message.edit_reply_markup(reply_markup=client_kb_ru.inline_kb_pizza_38)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 38
        await FSMPizza.next()

    elif callback.data in '32_eng':
        await callback.message.edit_reply_markup(reply_markup=client_kb_eng.inline_kb_pizza_32)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 38
        await FSMPizza.next()

    elif callback.data in '36_eng':
        await callback.message.edit_reply_markup(reply_markup=client_kb_eng.inline_kb_pizza_36)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 38
        await FSMPizza.next()

    elif callback.data in '38_eng':
        await callback.message.edit_reply_markup(reply_markup=client_kb_eng.inline_kb_pizza_38)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 38
        await FSMPizza.next()

    elif callback.data in '32_uz':
        await callback.message.edit_reply_markup(reply_markup=client_kb_uz.inline_kb_pizza_32)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 38
        await FSMPizza.next()

    elif callback.data in '36_uz':
        await callback.message.edit_reply_markup(reply_markup=client_kb_uz.inline_kb_pizza_36)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 38
        await FSMPizza.next()

    elif callback.data in '38_uz':
        await callback.message.edit_reply_markup(reply_markup=client_kb_uz.inline_kb_pizza_38)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 38
        await FSMPizza.next()

    if callback.data in '1':
        await callback.message.edit_reply_markup(reply_markup=client_kb_ru.inline_kb_pizza_1)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 1
        await FSMPizza.next()
    elif callback.data in '0.5':
        await callback.message.edit_reply_markup(reply_markup=client_kb_ru.inline_kb_pizza_0_5)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 0.5
        await FSMPizza.next()

    elif callback.data in '1_eng':
        await callback.message.edit_reply_markup(reply_markup=client_kb_eng.inline_kb_pizza_1)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 1
        await FSMPizza.next()
    elif callback.data in '0.5_eng':
        await callback.message.edit_reply_markup(reply_markup=client_kb_eng.inline_kb_pizza_0_5)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 0.5
        await FSMPizza.next()

    elif callback.data in '1_uz':
        await callback.message.edit_reply_markup(reply_markup=client_kb_uz.inline_kb_pizza_1)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 1
        await FSMPizza.next()
    elif callback.data in '0.5_uz':
        await callback.message.edit_reply_markup(reply_markup=client_kb_uz.inline_kb_pizza_0_5)
        await state.reset_state(False)
        await FSMPizza.size.set()
        async with state.proxy() as data:
            data['size'] = 0.5
        await FSMPizza.next()

    print(data)
    await callback.answer()


@dp.callback_query_handler(text='add_other_to_cart', state=FSMSnack.id)
async def to_cart(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = callback.message.chat.id
        print(data)
    await sql_db.sql_to_cart_other(state)
    await state.finish()
    await callback.answer('Добавлено в корзину', show_alert=True)
    await callback.message.answer('Что хотите заказать?', reply_markup=client_kb_ru.kb_menu)


@dp.callback_query_handler(text='add_other_to_cart_uz', state=FSMSnack.id)
async def to_cart(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = callback.message.chat.id
        print(data)
    await sql_db.sql_to_cart_other(state)
    await state.finish()
    await callback.answer("Savatga qo'shildi", show_alert=True)
    await callback.message.answer('Nima buyurtma bermoqchisiz?', reply_markup=client_kb_uz.kb_menu)


@dp.callback_query_handler(text='add_other_to_cart_eng', state=FSMSnack.id)
async def to_cart(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = callback.message.chat.id
        print(data)
    await sql_db.sql_to_cart_other(state)
    await state.finish()
    await callback.answer('Added to cart', show_alert=True)
    await callback.message.answer('What do you want to order?', reply_markup=client_kb_eng.kb_menu)


@dp.message_handler(text=['👍🏽Оформить заказ', "👍🏽Tekshirib ko'rmoq", "👍🏽Checkout"])
async def make_order(message: types.Message):
    if message.text == '👍🏽Оформить заказ':
        await message.answer('Нажмите на кнопку для сохранения вашего номера телефона\n'
                             '(без него доставка невозможна '
                             '😔)', reply_markup=client_kb_ru.kb_phone)
        await message.answer('Нажмите пожалуйста на продолжить оформление заказа')
    if message.text == "👍🏽Tekshirib ko'rmoq":
        await message.answer('Telefon raqamingizni saqlash uchun tugmani bosing\n'
                             '(busiz yetkazib berish mumkin emas'
                             '😔)', reply_markup=client_kb_uz.kb_phone)
        await message.answer('Buyurtmani davom ettirish tugmasini bosing')
    if message.text == '👍🏽Checkout':
        await message.answer('Click on the button to save your phone number\n'
                             '(delivery is not possible without it '
                             '😔)', reply_markup=client_kb_eng.kb_phone)
        await message.answer('Please click on continue ordering')


@dp.message_handler(text=['🚗Доставка', '🚗Delivery', '🚗Yetkazib berish'])
async def delivery(message: types.Message):
    if message.text == '🚗Доставка':
        await message.answer('Куда доставить?🧐', reply_markup=client_kb_ru.kb_address)
    elif message.text == '🚗Delivery':
        await message.answer('Where to deliver?🧐', reply_markup=client_kb_eng.kb_address)
    elif message.text == '🚗Yetkazib berish':
        await message.answer('Qaerga yetkazib berish?🧐', reply_markup=client_kb_uz.kb_address)


@dp.message_handler(content_types=['contact'])
async def show_back_button(message: types.Message):
    await sql_db.save_user_phone(message)


@dp.message_handler(text=['Яккасарайский р-он, ул. Шарафа Рашидова 40В', 'Сергелийский р-он, ул. Обихаёт 3',
                          'Yakkasaray district, Sharaf Rashidov st. 40V', 'Sergeli district, Environment st. 3',
                          'Yakkasaroy, Sharafa Rashidov koch. 40V', 'Sergeli, Atrof-muhit koch. 3'])
async def self_delivery(message: types.Message):
    await sql_db.self_del(message)
    await sql_db.send_order(message)
    if message.text == ['Яккасарайский р-он, ул. Шарафа Рашидова 40В', 'Сергелийский р-он, ул. Обихаёт 3']:
        await message.answer('Ожидайте звонка оператора')
        await message.answer('Вы в главном меню', reply_markup=client_kb_ru.kb_main)

    elif message.text == ['Yakkasaray district, Sharaf Rashidov st. 40V', 'Sergeli district, Environment st. 3']:
        await message.answer("Wait for the operator's call")
        await message.answer('You are in the main menu', reply_markup=client_kb_eng.kb_menu)

    elif message.text == ['Yakkasaroy, Sharafa Rashidov koch. 40V', 'Sergeli, Atrof-muhit koch. 3']:
        await message.answer("Operator qo'ng'irog'ini kuting")
        await message.answer('Siz asosiy menyudasiz', reply_markup=client_kb_uz.kb_menu)


@dp.message_handler(text=['🏢Самовывоз', '🏢Pickup', '🏢Termoq'])
async def delivery(message: types.Message):
    if message.text == '🏢Самовывоз':
        await message.answer('Выберите адрес пицерии', reply_markup=client_kb_ru.kb_kafe)
    elif message.text == '🏢Pickup':
        await message.answer('Choose the address of the pizzeria', reply_markup=client_kb_eng.kb_kafe)
    elif message.text == '🏢Termoq':
        await message.answer('Pitseriya manzilini tanlang', reply_markup=client_kb_uz.kb_kafe)


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    await sql_db.delivery_location(message)


@dp.message_handler(text=['📜 Мои заказы', '📜 My orders', '📜 Mening buyurtmalarim'])
async def my_orders(message: types.Message):
    if message.text == '📜 Мои заказы':
        await sql_db.my_orders(message)  #
    elif message.text == '📜 My orders':
        await sql_db.my_orders(message)  #
    elif message.text == '📜 Mening buyurtmalarim':
        await sql_db.my_orders(message)  #


@dp.message_handler(text=['❗Отмена', '❗Cancel', '❗Bekor qilish'])
async def cancel(message: types.Message):
    if message.text == '❗Отмена':
        await message.answer('Вы в главном меню', reply_markup=client_kb_ru.kb_menu)
    elif message.text == '❗Cancel':
        await message.answer('You are in the main menu', reply_markup=client_kb_eng.kb_menu)
    elif message.text == '❗Bekor qilish':
        await message.answer('Siz asosiy menyudasiz', reply_markup=client_kb_uz.kb_menu)


@dp.message_handler(text=['▶️Продолжить оформление заказа', '▶️Continue checkout', '▶️Buyurtmani davom eting'])
async def continue_order(message: types.Message):
    if message.text == '▶️Продолжить оформление заказа':
        await sql_db.check_number(message)
    elif message.text == '▶️Buyurtmani davom eting':
        await sql_db.check_number_uz(message)
    elif message.text == '▶️Continue checkout':
        await sql_db.check_number_eng(message)


@dp.message_handler(text=['📤Отправить заказ', '📤Send order', '📤Buyurtmani yuboring'])
async def send_full_order(message: types.Message):
    if message.text == '📤Отправить заказ':
        await message.answer('Спасибо за заказ, ожидайте звонка оператора😊', reply_markup=client_kb_ru.kb_main)
    elif message.text == '📤Buyurtmani yuboring':
        await message.answer("Buyurtma uchun rahmat, operatordan qo'ng'iroqni kuting😊",
                             reply_markup=client_kb_uz.kb_main)
    elif message.text == '📤Send order':
        await message.answer('Thank you for the order, wait for a call from the operator😊',
                             reply_markup=client_kb_eng.kb_main)
    await sql_db.send_order(message)


@dp.callback_query_handler(text=['plus', 'minus'])
async def plus_minus(callback: types.CallbackQuery):
    await callback.message.delete()
    if callback.data == 'plus':
        await sql_db.update_amount_plus(callback)
        await callback.answer()
    elif callback.data == 'minus':
        await sql_db.update_amount_minus(callback)
        await callback.answer()


@dp.callback_query_handler(text=['plus_uz', 'minus_uz'])
async def plus_minus_uz(callback: types.CallbackQuery):
    await callback.message.delete()
    if callback.data == 'plus_uz':
        await sql_db.update_amount_plus_uz(callback)
        await callback.answer()
    elif callback.data == 'minus_uz':
        await sql_db.update_amount_minus_uz(callback)
        await callback.answer()


@dp.callback_query_handler(text=['plus_eng', 'minus_eng'])
async def plus_minus_eng(callback: types.CallbackQuery):
    if callback.data == 'plus_eng':
        await sql_db.update_amount_plus_eng(callback)
        await callback.answer()
    elif callback.data == 'minus_eng':
        await sql_db.update_amount_minus_eng(callback)
        await callback.answer()


@dp.message_handler(text=['🌀 Очистить корзину', '🌀 Clear the cart', "🌀 Savatni bo'shatish"])
async def clear_cart(message: types.Message):
    if message.text == '🌀 Очистить корзину':
        await sql_db.delete_order(message)
        await message.answer('Корзина очищена, вы в главном меню', reply_markup=client_kb_ru.kb_main)
    elif message.text == '🌀 Clear the cart':
        await sql_db.delete_order(message)
        await message.answer('Cart empty, you are in the main menu', reply_markup=client_kb_eng.kb_main)
    elif message.text == "🌀 Savatni bo'shatish":
        await sql_db.delete_order(message)
        await message.answer('Arava bo‘sh, siz asosiy menyudasiz', reply_markup=client_kb_uz.kb_main)


@dp.message_handler(text=['Отлично 🌟🌟🌟🌟🌟', 'Хорошо 🌟🌟🌟🌟', 'Нормально 🌟🌟🌟', 'Так себе 🌟🌟', 'Плохо, 🌟', 'Не хочу',
                          'Ajoyib 🌟🌟🌟🌟🌟', 'Yaxshi 🌟🌟🌟🌟', 'Yoqdi 🌟🌟🌟', 'Boladi 🌟🌟', 'Yomon 🌟', 'Hohlamayman',
                          'Excellent 🌟🌟🌟🌟🌟', 'Good 🌟🌟🌟🌟', 'Nice 🌟🌟🌟', 'So-so 🌟🌟', 'Bad 🌟', 'I do not want'])
async def mark(message: types.Message):
    await sql_db.star(message)
    if message.text == 'Не хочу':
        await message.answer('Хорошо, вернул вас в главное меню', reply_markup=client_kb_ru.kb_main)
    elif message.text == 'Hohlamayman':
        await message.answer('OK, sizni asosiy menyuga qaytardim', reply_markup=client_kb_uz.kb_main)
    elif message.text == 'I do not want':
        await message.answer('Okay, brought you back to the main menu', reply_markup=client_kb_eng.kb_main)


@dp.message_handler()
async def feedback(message: types.Message):
    await sql_db.feedback(message)


def register_handlers_client(disp: Dispatcher):
    disp.register_message_handler(command_start, commands=['start', 'help'])
    disp.register_message_handler(command_language)
