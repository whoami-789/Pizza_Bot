from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import bot, dp
from keyboards import client_kb_ru, admin_kb
from sql import sql_db
from aiogram.dispatcher.filters import Text

ID = None


@dp.message_handler(commands='moderator', is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Вы в главном меню панели админа', reply_markup=admin_kb.kb_admin_main)
    await message.delete()


@dp.callback_query_handler(text='Принять заказ')
async def command_size(callback: types.CallbackQuery):
    await sql_db.tip(callback)


class FSMAdminP(StatesGroup):
    photo = State()
    name = State()
    size = State()
    description = State()
    price = State()


class FSMAdminD(StatesGroup):
    photo = State()
    name = State()
    size = State()
    description = State()
    price = State()


class FSMAdminSnack(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


class FSMAdminSouse(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


class FSMAdminSalat(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


@dp.message_handler(state="*", text='Назад')
@dp.message_handler(text='Назад')
async def command_back(m: types.Message, state: FSMContext):
    global ID
    ID = m.from_user.id
    await bot.send_message(m.from_user.id, 'Вы в главном меню', reply_markup=admin_kb.kb_admin_main)
    if m.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()


@dp.message_handler(text='Добавить позицию в меню')
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что добавить в меню?', reply_markup=admin_kb.kb_admin)


@dp.message_handler(Text(equals='Пицца'), state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdminP.photo.set()
        await message.reply('Загрузи фото', reply_markup=None)


@dp.message_handler(content_types=['photo'], state=FSMAdminP.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdminP.next()
        await message.reply(data)
        await message.reply("Введи название", reply_markup=None)


@dp.message_handler(state=FSMAdminP.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdminP.next()
        await message.reply("Выбери размер", reply_markup=admin_kb.kb_admin1)


@dp.message_handler(state=FSMAdminP.size)
async def load_size(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['size'] = int(message.text)
        await FSMAdminP.next()
        await message.reply("Введи описание", reply_markup=None)


@dp.message_handler(state=FSMAdminP.description)
async def load_desc(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdminP.next()
        await message.reply("Введи цену")


@dp.message_handler(state=FSMAdminP.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = int(message.text)

        async with state.proxy() as data:
            print(data)

        await sql_db.sql_add_pizza(state)
        await state.finish()
        await message.answer('Пицца сохранена', reply_markup=admin_kb.kb_admin)


########################################################################################################################

@dp.message_handler(Text(equals='Салаты'), state=None)
async def cm_salat(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdminSalat.photo.set()
        await message.reply('Загрузи фото')


@dp.message_handler(content_types=['photo'], state=FSMAdminSalat.photo)
async def load_photo_s(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdminSalat.next()
        await message.reply(data)
        await message.reply("Введи название")


@dp.message_handler(state=FSMAdminSalat.name)
async def load_name_s(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdminSalat.next()
        await message.reply("Введи описание")


@dp.message_handler(state=FSMAdminSalat.description)
async def load_desc_s(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdminSalat.next()
        await message.reply("Введи цену")


@dp.message_handler(state=FSMAdminSalat.price)
async def load_price_s(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = int(message.text)

        async with state.proxy() as data:
            print(data)

        await sql_db.sql_add_salat(state)
        await state.finish()
        await message.answer('Салат сохранен', reply_markup=admin_kb.kb_admin)


########################################################################################################################

@dp.message_handler(Text(equals='Снеки'), state=None)
async def cm_salat(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdminSnack.photo.set()
        await message.reply('Загрузи фото')


@dp.message_handler(content_types=['photo'], state=FSMAdminSnack.photo)
async def load_photo_s(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdminSnack.next()
        await message.reply(data)
        await message.reply("Введи название")


@dp.message_handler(state=FSMAdminSnack.name)
async def load_name_s(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdminSnack.next()
        await message.reply("Введи описание")


@dp.message_handler(state=FSMAdminSnack.description)
async def load_desc_s(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdminSnack.next()
        await message.reply("Введи цену")


@dp.message_handler(state=FSMAdminSnack.price)
async def load_price_s(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = int(message.text)

        async with state.proxy() as data:
            print(data)

        await sql_db.sql_add_snack(state)
        await state.finish()
        await message.answer('Салат сохранен', reply_markup=admin_kb.kb_admin)


########################################################################################################################

@dp.message_handler(Text(equals='Соусы'), state=None)
async def cm_souse(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdminSouse.photo.set()
        await message.reply('Загрузи фото')


@dp.message_handler(content_types=['photo'], state=FSMAdminSouse.photo)
async def load_photo_s(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdminSouse.next()
        await message.reply(data)
        await message.reply("Введи название")


@dp.message_handler(state=FSMAdminSouse.name)
async def load_name_s(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdminSouse.next()
        await message.reply("Введи описание")


@dp.message_handler(state=FSMAdminSouse.description)
async def load_desc_s(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdminSouse.next()
        await message.reply("Введи цену")


@dp.message_handler(state=FSMAdminSouse.price)
async def load_price_s(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = int(message.text)

        async with state.proxy() as data:
            print(data)

        await sql_db.sql_add_souse(state)
        await state.finish()
        await message.answer('Соус сохранен', reply_markup=admin_kb.kb_admin)


###################################################################################################################

@dp.message_handler(Text(equals='Напитки'), state=None)
async def cm_start_d(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdminD.photo.set()
        await message.reply('Загрузи фото', reply_markup=None)


@dp.message_handler(content_types=['photo'], state=FSMAdminD.photo)
async def load_photo_d(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdminD.next()
        await message.reply(data)
        await message.reply("Введи название", reply_markup=None)


@dp.message_handler(state=FSMAdminD.name)
async def load_name_d(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdminD.next()
        await message.reply("Выбери размер", reply_markup=admin_kb.drink_kb)


@dp.message_handler(state=FSMAdminD.size)
async def load_size_d(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['size'] = int(message.text)
        await message.reply(data)
        await message.reply("Введи описание", reply_markup=None)


@dp.message_handler(state=FSMAdminD.description)
async def load_desc_d(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdminD.next()
        await message.reply("Введи цену")


@dp.message_handler(state=FSMAdminD.price)
async def load_price_d(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = int(message.text)

        async with state.proxy() as data:
            print(data)

        await sql_db.sql_add_drink(state)
        await state.finish()
        await message.answer('Напиток сохранен', reply_markup=admin_kb.kb_admin)


########################################################################################################################
@dp.message_handler(state="*", commands='отмена')
@dp.message_handler(Text(equals='❗отмена', ignore_case=True), state='*')
async def cansel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')
        await message.answer('Что добавить в меню?')


@dp.message_handler(state="*", commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cansel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')
        await message.answer('Что добавить в меню?')
