import asyncio
import sqlite3 as sq

import requests

from create_bot import bot
from handlers import client
from keyboards import client_kb_ru, admin_kb, client_kb_eng, client_kb_uz


def sql_start():
    global base, cur
    base = sq.connect('pizza.db')
    cur = base.cursor()
    if base:
        print('db connected')
    base.execute('create table if not exists category(id integer primary key autoincrement, name text)')
    base.execute(
        'create table if not exists user(chat_id integer primary key, first_name text, last_name text, pnumber TEXT)')
    base.execute(
        'CREATE TABLE IF NOT EXISTS menu(id INTEGER PRIMARY KEY AUTOINCREMENT, img TEXT, name TEXT, description TEXT, '
        'price INTEGER '
        ', idc INTEGER, psize TEXT, FOREIGN KEY (idc) REFERENCES category (id))')
    base.execute(
        'CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY AUTOINCREMENT, dateC TEXT,'
        ' address TEXT, fullprice INTEGER, received INTEGER, longtitude text, latitude text, send integer, '
        'star integer, feedback text'
        ',idu INTEGER, FOREIGN KEY (idu) REFERENCES user (chat_id))')
    base.execute('create table if not exists cart(idm integer, ido integer, amount integer, price integer, '
                 'foreign key (idm) references menu (id), foreign key (ido) references orders (id),'
                 'foreign key (price) references menu (price))')
    base.commit()


# Добавление меню
async def sql_add_pizza(state):
    async with state.proxy() as data:
        cur.execute('insert into menu (img, name, psize, description, price, idc) '
                    'values (?,?,?,?,?,1)', tuple(data.values()))
        base.commit()


async def sql_add_salat(state):
    async with state.proxy() as data:
        cur.execute('insert into menu (img, name, description, price, idc) '
                    'values (?,?,?,?,2)', tuple(data.values()))
        base.commit()


async def sql_add_souse(state):
    async with state.proxy() as data:
        cur.execute('insert into menu (img, name, description, price, idc) '
                    'values (?,?,?,?,3)', tuple(data.values()))
        base.commit()


async def sql_add_snack(state):
    async with state.proxy() as data:
        cur.execute('insert into menu (img, name, description, price, idc) '
                    'values (?,?,?,?,4)', tuple(data.values()))
        base.commit()


async def sql_add_drink(state):
    async with state.proxy() as data:
        cur.execute('insert into menu (img, name, psize, description, price, idc) '
                    'values (?,?,?,?,?,5)', tuple(data.values()))
        base.commit()


# Отображение пицц ################################################################################################
async def sql_view_pizza(message):
    a = cur.execute("select price from menu where idc=1 and name like ? and psize=36", (message.text,)).fetchone()
    b = cur.execute("select price from menu where idc=1 and name like ? and psize=38", (message.text,)).fetchone()
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=1 and name like ? and psize=32",
            (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nЦены:\n'
                                                           f'32 см  {ret[3]} сум\n'
                                                           f'36 см  {a[0]} сум\n'
                                                           f'38 см  {b[0]} сум\n',
                             reply_markup=client_kb_ru.inline_kb_pizza)
    print(a[0])


async def sql_view_pizza_eng(message):
    a = cur.execute("select price from menu where idc=1 and name like ? and psize=36", (message.text,)).fetchone()
    b = cur.execute("select price from menu where idc=1 and name like ? and psize=38", (message.text,)).fetchone()
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=1 and name like ? and psize=32",
            (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nPrice:\n '
                                                           f'32 sm {ret[3]} sum\n'
                                                           f'36 sm {a[0]} sum\n'
                                                           f'38 sm {b[0]} sum\n',
                             reply_markup=client_kb_eng.inline_kb_pizza)


async def sql_view_pizza_uz(message):
    a = cur.execute("select price from menu where idc=1 and name like ? and psize=36", (message.text,)).fetchone()
    b = cur.execute("select price from menu where idc=1 and name like ? and psize=38", (message.text,)).fetchone()
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=1 and name like ? and psize=32",
            (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nNarxlar\n '
                                                           f'32 sm {ret[3]} sum\n'
                                                           f'36 sm {a[0]} sum\n'
                                                           f'38 sm {b[0]} sum\n',
                             reply_markup=client_kb_uz.inline_kb_pizza)


async def sql_pizza_name(message):
    cur.execute("select name from menu where name like ?", (message.text,))


# Отображение салатов ################################################################################################
async def sql_view_salat(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=2 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nЦена {ret[3]} сум',
                             reply_markup=client_kb_ru.inline_kb_salat_snack_souse)


async def sql_view_salat_uz(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=2 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nNarxi {ret[3]} sum',
                             reply_markup=client_kb_uz.inline_kb_salat_snack_souse)


async def sql_view_salat_eng(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=2 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nPrice {ret[3]} sum',
                             reply_markup=client_kb_eng.inline_kb_salat_snack_souse)


# Отображение соусов ###############################################################################################
async def sql_view_souse(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=3 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nЦена {ret[3]} сум',
                             reply_markup=client_kb_ru.inline_kb_salat_snack_souse)


async def sql_view_souse_uz(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=3 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nNarxi {ret[3]} sum',
                             reply_markup=client_kb_uz.inline_kb_salat_snack_souse)


async def sql_view_souse_eng(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=3 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nPrice {ret[3]} sum',
                             reply_markup=client_kb_eng.inline_kb_salat_snack_souse)


# Отображение закусок ################################################################################################
async def sql_view_snack(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=4 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nЦена {ret[3]} сум',
                             reply_markup=client_kb_ru.inline_kb_salat_snack_souse)


async def sql_view_snack_uz(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=4 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nNarxi {ret[3]} sum',
                             reply_markup=client_kb_uz.inline_kb_salat_snack_souse)


async def sql_view_snack_eng(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=4 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nPrice {ret[3]} sum',
                             reply_markup=client_kb_eng.inline_kb_salat_snack_souse)


# Отображение напитков ################################################################################################
async def sql_view_drink(message):
    a = cur.execute("select price from menu where idc=5 and name like ? and psize=0.5", (message.text,)).fetchone()
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=5 and name like ? and psize=1",
            (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nЦены:\n '
                                                           f'0.5 литра {a[0]} сум\n'
                                                           f'1 литр {ret[3]} сум',
                             reply_markup=client_kb_ru.inline_kb_drink)


async def sql_view_drink_uz(message):
    a = cur.execute("select price from menu where idc=5 and name like ? and psize=0.5", (message.text,)).fetchone()
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=5 and name like ? and psize=1",
            (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nNarxlar:\n '
                                                           f'0.5 litr {a[0]} sum\n'
                                                           f'1 litr {ret[3]} sum',
                             reply_markup=client_kb_uz.inline_kb_drink)


async def sql_view_drink_eng(message):
    a = cur.execute("select price from menu where idc=5 and name like ? and psize=0.5", (message.text,)).fetchone()
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=5 and name like ? and psize=1",
            (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nPrice:\n '
                                                           f'0.5 liter {a[0]} sum\n'
                                                           f'1 liter {ret[3]} sum',
                             reply_markup=client_kb_eng.inline_kb_drink)


# Отображение мини пицц ###################################################################################
async def sql_view_mini_pizza(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=6 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nЦена {ret[3]} сум',
                             reply_markup=client_kb_ru.inline_kb_salat_snack_souse)


async def sql_view_mini_pizza_uz(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=6 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nNarxi {ret[3]} sum',
                             reply_markup=client_kb_uz.inline_kb_salat_snack_souse)


async def sql_view_mini_pizza_eng(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=6 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\n{ret[2]}\n\nPrice {ret[3]} sum',
                             reply_markup=client_kb_eng.inline_kb_salat_snack_souse)


# Отображение сетов ######################################################################################
async def sql_view_sets(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=7 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nЦена {ret[3]} сум',
                             reply_markup=client_kb_ru.inline_kb_salat_snack_souse)


async def sql_view_sets_uz(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=7 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nNarxi {ret[3]} sum',
                             reply_markup=client_kb_uz.inline_kb_salat_snack_souse)


async def sql_view_sets_eng(message):
    for ret in cur.execute(
            "SELECT img, name, description, price FROM menu where idc=7 and name like ?", (message.text,)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nPrice {ret[3]} sum',
                             reply_markup=client_kb_eng.inline_kb_salat_snack_souse)


#######################################################################################################################
async def sql_to_cart_pd(state):
    async with state.proxy() as data:
        a = tuple(data.values())
        cur.execute("insert  into cart (idm, ido, amount, price) values "
                    "((select id from menu"
                    " where name like ? and psize=?),"
                    " (select id from orders "
                    "where dateC=date() and idu=? and received=0), 1, "
                    "(select menu.price from menu inner join cart  on menu.id = cart.idm and name like ? and psize=?))",
                    (a[0], a[1], a[2], a[0], a[1],))
        base.commit()


async def sql_to_cart_other(state):
    async with state.proxy() as data:
        a = tuple(data.values())
        cur.execute("insert into cart (idm, ido, amount, price) values "
                    "((select id from menu where name like ?),"
                    " (select id from orders "
                    "where dateC=date() and idu=? and received=0), 1, "
                    "(select menu.price from menu inner join cart  on menu.id = cart.idm and name like ?))",
                    (a[0], a[1], a[0],))
        base.commit()


async def create_order_number(message):
    cur.execute('insert into orders (dateC, idu, received, send) values (date(),?,0,0)', (message.chat.id,))
    base.commit()


async def save_user(message):
    cur.execute("insert or ignore into user (chat_id, first_name, last_name, pnumber) values (?,?,?,0)",
                (message.chat.id, message.from_user.first_name,
                 message.from_user.last_name,))
    base.commit()


async def save_user_phone(message):
    cur.execute("update user set pnumber=? where chat_id=?", (message.contact.phone_number, message.chat.id,))
    base.commit()


async def check_lang_ru(callback):
    for a in cur.execute('select chat_id from user where lang=1').fetchone():
        a = callback.message.chat.id


async def check_lang_uz(callback):
    cur.execute('select lang from user where lang=? and chat_id=?', ('uz', callback.message.chat.id,))


async def check_lang_eng(callback):
    cur.execute('select lang from user where lang=? and chat_id=?', ('eng', callback.message.chat.id,))


async def save_user_lang(message):
    cur.execute("update user set lang=? where chat_id=?", ('ru', message.chat.id,))
    base.commit()


async def save_user_lang_uz(message):
    cur.execute("update user set lang=? where chat_id=?", ('uz', message.chat.id,))
    base.commit()


async def save_user_lang_eng(message):
    cur.execute("update user set lang=? where chat_id=?", ('eng', message.chat.id,))
    base.commit()


async def delivery_location(message):
    token = 'pk.1eb8aed04f9a7a71ec63c9212865a6ca'
    headers = {"Accept-Language": "ru"}
    address = requests.get(
        f'https://eu1.locationiq.com/v1/reverse.php?key={token}&lat={message.location.latitude}&lon={message.location.longitude}&format=json',
        headers=headers).json()
    cur.execute('update orders set address=? where idu=? and dateC=date() and received=0',
                (address.get("display_name"), message.chat.id,))
    cur.execute('update orders set longtitude=?, latitude=? where idu=? and dateC=date() and received=0',
                (message.location.longitude, message.location.latitude, message.chat.id,))
    base.commit()


async def self_del(message):
    cur.execute('update orders set address=? where idu=? and dateC=date() and received=0',
                (message.text, message.chat.id,))
    base.commit()


async def test_user_data(message):
    cur.execute("select chat_id from user where chat_id=?", (message.chat.id,))


async def show_user_data(message):
    if message.text == 'Мои данные':
        for ret in cur.execute(
                "select first_name, last_name, pnumber from user where chat_id=?", (message.chat.id,)).fetchall():
            await bot.send_message(message.from_user.id, f'{ret[0]} {ret[1]}\nНомер телефона: {ret[2]}')
    elif message.text == 'My details':
        for ret in cur.execute(
                "select first_name, last_name, pnumber from user where chat_id=?", (message.chat.id,)).fetchall():
            await bot.send_message(message.from_user.id, f'{ret[0]} {ret[1]}\nPhone number: {ret[2]}')
    elif message.text == 'Mening tafsilotlarim':
        for ret in cur.execute(
                "select first_name, last_name, pnumber from user where chat_id=?", (message.chat.id,)).fetchall():
            await bot.send_message(message.from_user.id, f'{ret[0]} {ret[1]}\nTelefon raqami: {ret[2]}')


async def test_user_phone(message):
    cur.execute("select pnumber from user where chat_id=?", (message.chat.id,))


async def pizza_check():
    cur.execute("select idc from menu")


async def show_cart(message):
    for ret in cur.execute(
            'select orders.id, menu.name, menu.psize, menu.price, cart.amount from orders '
            'inner join cart on orders.id = cart.ido '
            'inner join menu on menu.id = cart.idm '
            'inner join user on orders.idu = user.chat_id where chat_id=? and orders.dateC=date() and orders.received=0'
            , (message.chat.id,)):
        await bot.send_message(message.from_user.id,
                               f'Номер заказа: {ret[0]}\n{ret[1]} {ret[2]} см\nЦена: {ret[3] * ret[4]} сум\nКолличество: {ret[4]}',
                               reply_markup=client_kb_ru.inline_cart)

    for a in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0) and menu.id=cart.idm',
                         (message.chat.id,)).fetchone():
        await bot.send_message(message.from_user.id, f'Полная стоимость заказа: {a} сум',
                               reply_markup=client_kb_ru.kb_cart)


async def show_cart_uz(message):
    for ret in cur.execute(
            'select orders.id, menu.name, menu.psize, menu.price, cart.amount from orders '
            'inner join cart on orders.id = cart.ido '
            'inner join menu on menu.id = cart.idm '
            'inner join user on orders.idu = user.chat_id where chat_id=? and orders.dateC=date() and orders.received=0'
            , (message.chat.id,)):
        await bot.send_message(message.from_user.id,
                               f'Buyurtma raqami: {ret[0]}\n{ret[1]} {ret[2]} sm\nNarxi: {ret[3] * ret[4]} sum\nMiqdori: {ret[4]}',
                               reply_markup=client_kb_ru.inline_cart)

    for a in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0) and menu.id=cart.idm',
                         (message.chat.id,)).fetchone():
        await bot.send_message(message.from_user.id, f'Buyurtmaning umumiy qiymati: {a} sum',
                               reply_markup=client_kb_uz.kb_cart)


async def show_cart_eng(message):
    for ret in cur.execute(
            'select orders.id, menu.name, menu.psize, menu.price, cart.amount from orders '
            'inner join cart on orders.id = cart.ido '
            'inner join menu on menu.id = cart.idm '
            'inner join user on orders.idu = user.chat_id where chat_id=? and orders.dateC=date() and orders.received=0'
            , (message.chat.id,)):
        await bot.send_message(message.from_user.id,
                               f'Order number: {ret[0]}\n{ret[1]} {ret[2]} sm\nPrice: {ret[3] * ret[4]} sum\nQuantity: {ret[4]}',
                               reply_markup=client_kb_eng.inline_cart)

    for a in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0) and menu.id=cart.idm',
                         (message.chat.id,)).fetchone():
        await bot.send_message(message.from_user.id, f'Total cost of the order: {a} sum',
                               reply_markup=client_kb_eng.kb_cart)


async def send_order(message):
    cur.execute('update orders set send=? where dateC=date() and idu=?', (1, message.chat.id,))
    base.commit()
    for ret in cur.execute('select orders.longtitude, orders.latitude, user.pnumber, user.first_name from orders '
                           'inner join user on user.chat_id = orders.idu where dateC=date() and idu=? and received=0 '
                           'and send=1', (message.chat.id,)):
        await bot.send_location(596927092, ret[1], ret[0])
        await bot.send_message(596927092, f'{ret[3]}\n {ret[2]}')
    for ret in cur.execute(
            'select orders.id, menu.name, menu.psize, menu.price, cart.amount from orders '
            'inner join cart on orders.id = cart.ido '
            'inner join menu on menu.id = cart.idm '
            'inner join user on orders.idu = user.chat_id where chat_id=? and orders.dateC=date() and orders.received=0 and send=1'
            , (message.chat.id,)).fetchall():
        await bot.send_message(596927092,
                               f'Номер заказа: {ret[0]}\n{ret[1]} {ret[2]} см\nЦена: {ret[3] * ret[4]} сум\nКолличество: {ret[4]}',
                               reply_markup=admin_kb.inline_kb_recive)
    for a in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0 and send=1) and menu.id=cart.idm',
                         (message.chat.id,)).fetchone():
        await bot.send_message(596927092, f'Полная стоимость заказа: {a} сум')


async def my_orders(message):
    for ret in cur.execute(
            'select menu.name, menu.psize, cart.amount, orders.id, orders.dateC, orders.address '
            'from orders '
            'inner join cart on orders.id = cart.ido '
            'inner join user  on user.chat_id = orders.idu '
            'inner join menu  on menu.id = cart.idm where user.chat_id=? and orders.received=1',
            (message.chat.id,)).fetchall():
        await bot.send_message(message.chat.id,
                               f'Номер заказа: {ret[3]}\n {ret[0]} {ret[1]} см\n Колличество: {ret[2]}\n '
                               f'Дата заказа: {ret[4]}\n Адрес: {ret[5]}')


async def tip(callback):
    a = callback.message.text.split()
    cur.execute('update orders set received=1 where id=? and send=1', (a[2],))
    base.commit()
    await callback.message.edit_reply_markup(reply_markup=admin_kb.inline_kb_recive_done)
    for ret in cur.execute('select idu from main.orders where id=?', (a[2],)):
        await asyncio.sleep(10)
        for b in cur.execute('select lang from user '
                             'where chat_id=(select idu from main.orders where id=?)', (a[2],)).fetchone():
            if b == 'ru':
                await bot.send_message(ret[0], 'Оцение качество обслуживания пожалуйста',
                                       reply_markup=client_kb_ru.marks)
            elif b == 'uz':
                await bot.send_message(ret[0], 'Iltimos, xizmat sifatini baholang', reply_markup=client_kb_uz.marks)
            elif b == 'eng':
                await bot.send_message(ret[0], 'Rate the quality of service please', reply_markup=client_kb_eng.marks)


async def delete_cart(callback):
    a = callback.message.text.split()
    cur.execute('delete from cart where idm=(select id from menu where '
                '((name=?) and (psize=?))) '
                'and ido=(select id from orders where idu=? and dateC=date())',
                (
                    a[3] or a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5] or a[3] + ' ' + a[4] + ' ' + a[
                        5] + ' ' + a[
                        6],
                    a[4] or a[5] or a[6] or a[7], callback.message.chat.id,))
    cur.execute('delete from cart where idm=(select id from menu where '
                'name=?) '
                'and ido=(select id from orders where idu=? and dateC=date())',
                (a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5], callback.message.chat.id,))
    base.commit()
    for a in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0) and menu.id=cart.idm',
                         (callback.message.chat.id,)).fetchone():
        await callback.message.answer(f'Полная стоимость заказа: {a} сум')


async def delete_cart_uz(callback):
    a = callback.message.text.split()
    cur.execute('delete from cart where idm=(select id from menu where '
                '((name=?) and (psize=?))) '
                'and ido=(select id from orders where idu=? and dateC=date())',
                (
                    a[3] or a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5] or a[3] + ' ' + a[4] + ' ' + a[
                        5] + ' ' + a[
                        6],
                    a[4] or a[5] or a[6] or a[7], callback.message.chat.id,))
    cur.execute('delete from cart where idm=(select id from menu where '
                'name=?) '
                'and ido=(select id from orders where idu=? and dateC=date())',
                (a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5], callback.message.chat.id,))
    base.commit()
    for a in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0) and menu.id=cart.idm',
                         (callback.message.chat.id,)).fetchone():
        await callback.message.answer(f'Buyurtmaning umumiy qiymati: {a} сум')


async def delete_cart_eng(callback):
    a = callback.message.text.split()
    cur.execute('delete from cart where idm=(select id from menu where '
                '((name=?) and (psize=?))) '
                'and ido=(select id from orders where idu=? and dateC=date())',
                (
                    a[3] or a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5] or a[3] + ' ' + a[4] + ' ' + a[
                        5] + ' ' + a[
                        6],
                    a[4] or a[5] or a[6] or a[7], callback.message.chat.id,))
    cur.execute('delete from cart where idm=(select id from menu where '
                'name=?) '
                'and ido=(select id from orders where idu=? and dateC=date())',
                (a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5], callback.message.chat.id,))
    base.commit()
    for a in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0) and menu.id=cart.idm',
                         (callback.message.chat.id,)).fetchone():
        await callback.message.answer(f'Total cost of the order: {a} сум')


async def update_amount_plus(callback):
    a = callback.message.text.split()
    print(a)
    cur.execute('update cart set amount=amount+1 where idm=(select id from menu where '
                '((name=?) and (psize=?))) and ido=?',
                (
                    a[3] or a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5] or a[3] + ' ' + a[4] + ' ' + a[
                        5] + ' ' + a[
                        6],
                    a[4] or a[5] or a[6] or a[7], a[2],))
    cur.execute('update cart set amount=amount+1 where idm=(select id from menu where '
                'name=?) and ido=?',
                (a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5],
                 a[2],))
    base.commit()
    for ret in cur.execute(
            'select orders.id, menu.name, menu.psize, menu.price, cart.amount from orders '
            'inner join cart on orders.id = cart.ido '
            'inner join menu on menu.id = cart.idm '
            'inner join user on orders.idu = user.chat_id where chat_id=? and orders.dateC=date() and orders.received=0'
            , (callback.message.chat.id,)):
        await callback.message.answer(
            f'Номер заказа: {ret[0]}\n{ret[1]} {ret[2]} см\nЦена: {ret[3] * ret[4]} сум\nКолличество: {ret[4]}',
            reply_markup=client_kb_ru.inline_cart)

    for b in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0) and menu.id=cart.idm',
                         (callback.message.chat.id,)).fetchone():
        await callback.message.answer(f'Полная стоимость заказа: {b} сум')


async def update_amount_minus(callback):
    a = callback.message.text.split()
    cur.execute('update cart set amount=amount-1 where idm=(select id from menu where '
                '((name=?) and (psize=?))) and ido=?',
                (a[3] or a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5] or a[3] + ' ' + a[4] + ' ' + a[5] + ' ' +
                 a[6],
                 a[4] or a[5] or a[6] or a[7], a[2],))
    cur.execute('update cart set amount=amount-1 where idm=(select id from menu where '
                'name=?) and ido=?',
                (a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5],
                 a[2],))
    base.commit()
    for ret in cur.execute(
            'select orders.id, menu.name, menu.psize, menu.price, cart.amount from orders '
            'inner join cart on orders.id = cart.ido '
            'inner join menu on menu.id = cart.idm '
            'inner join user on orders.idu = user.chat_id where chat_id=? and orders.dateC=date() and orders.received=0'
            , (callback.message.chat.id,)):
        await callback.message.answer(
            f'Номер заказа: {ret[0]}\n{ret[1]} {ret[2]} см\nЦена: {ret[3] * ret[4]} сум\nКолличество: {ret[4]}',
            reply_markup=client_kb_ru.inline_cart)

    for a in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0) and menu.id=cart.idm',
                         (callback.message.chat.id,)).fetchone():
        await callback.message.answer(f'Полная стоимость заказа: {a} сум')


async def update_amount_plus_uz(callback):
    a = callback.message.text.split()
    cur.execute('update cart set amount=amount+1 where idm=(select id from menu where '
                '((name=?) and (psize=?))) and ido=?',
                (
                    a[3] or a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5] or a[3] + ' ' + a[4] + ' ' + a[
                        5] + ' ' + a[
                        6],
                    a[4] or a[5] or a[6] or a[7], a[2],))
    cur.execute('update cart set amount=amount+1 where idm=(select id from menu where '
                'name=?) and ido=?',
                (a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5],
                 a[2],))
    base.commit()
    for ret in cur.execute(
            'select orders.id, menu.name, menu.psize, menu.price, cart.amount from orders '
            'inner join cart on orders.id = cart.ido '
            'inner join menu on menu.id = cart.idm '
            'inner join user on orders.idu = user.chat_id where chat_id=? and orders.dateC=date() and orders.received=0'
            , (callback.message.chat.id,)):
        await callback.message.answer(
            f'Buyurtma raqami: {ret[0]}\n{ret[1]} {ret[2]} sm\nNarxi: {ret[3] * ret[4]} sum\nMiqdori: {ret[4]}',
            reply_markup=client_kb_uz.inline_cart)

    for a in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0) and menu.id=cart.idm',
                         (callback.message.chat.id,)).fetchone():
        await callback.message.answer(f'Buyurtmaning umumiy qiymati: {a} sum')


async def update_amount_minus_uz(callback):
    a = callback.message.text.split()
    cur.execute('update cart set amount=amount-1 where idm=(select id from menu where '
                '((name=?) and (psize=?))) and ido=?',
                (a[3] or a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5] or a[3] + ' ' + a[4] + ' ' + a[5] + ' ' +
                 a[6],
                 a[4] or a[5] or a[6] or a[7], a[2],))
    cur.execute('update cart set amount=amount-1 where idm=(select id from menu where '
                'name=?) and ido=?',
                (a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5],
                 a[2],))
    base.commit()
    for ret in cur.execute(
            'select orders.id, menu.name, menu.psize, menu.price, cart.amount from orders '
            'inner join cart on orders.id = cart.ido '
            'inner join menu on menu.id = cart.idm '
            'inner join user on orders.idu = user.chat_id where chat_id=? and orders.dateC=date() and orders.received=0'
            , (callback.message.chat.id,)):
        await callback.message.answer(
            f'Buyurtma raqami: {ret[0]}\n{ret[1]} {ret[2]} sm\nNarxi: {ret[3] * ret[4]} sum\nMiqdori: {ret[4]}',
            reply_markup=client_kb_uz.inline_cart)

    for a in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0) and menu.id=cart.idm',
                         (callback.message.chat.id,)).fetchone():
        await callback.message.answer(f'Buyurtmaning umumiy qiymati: {a} sum')


async def update_amount_plus_eng(callback):
    a = callback.message.text.split()
    cur.execute('update cart set amount=amount+1 where idm=(select id from menu where '
                '((name=?) and (psize=?))) and ido=?',
                (
                    a[3] or a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5] or a[3] + ' ' + a[4] + ' ' + a[
                        5] + ' ' + a[
                        6],
                    a[4] or a[5] or a[6] or a[7], a[2],))
    cur.execute('update cart set amount=amount+1 where idm=(select id from menu where '
                'name=?) and ido=?',
                (a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5],
                 a[2],))
    base.commit()
    for ret in cur.execute(
            'select orders.id, menu.name, menu.psize, menu.price, cart.amount from orders '
            'inner join cart on orders.id = cart.ido '
            'inner join menu on menu.id = cart.idm '
            'inner join user on orders.idu = user.chat_id where chat_id=? and orders.dateC=date() and orders.received=0'
            , (callback.message.chat.id,)):
        await callback.message.answer(
            f'Order number: {ret[0]}\n{ret[1]} {ret[2]} sm\nPrice: {ret[3] * ret[4]} sum\nQuantity: {ret[4]}',
            reply_markup=client_kb_eng.inline_cart)

    for a in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0) and menu.id=cart.idm',
                         (callback.message.chat.id,)).fetchone():
        await callback.message.answer(f'Total cost of the order: {a} sum')


async def update_amount_minus_eng(callback):
    a = callback.message.text.split()
    cur.execute('update cart set amount=amount-1 where idm=(select id from menu where '
                '((name=?) and (psize=?))) and ido=?',
                (
                    a[3] or a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5] or a[3] + ' ' + a[4] + ' ' + a[
                        5] + ' ' + a[
                        6],
                    a[4] or a[5] or a[6] or a[7], a[2],))
    cur.execute('update cart set amount=amount-1 where idm=(select id from menu where '
                'name=?) and ido=?',
                (a[3] + ' ' + a[4] or a[3] + ' ' + a[4] + ' ' + a[5],
                 a[2],))
    base.commit()
    for ret in cur.execute(
            'select orders.id, menu.name, menu.psize, menu.price, cart.amount from orders '
            'inner join cart on orders.id = cart.ido '
            'inner join menu on menu.id = cart.idm '
            'inner join user on orders.idu = user.chat_id where chat_id=? and orders.dateC=date() and orders.received=0'
            , (callback.message.chat.id,)):
        await callback.message.answer(
            f'Order number: {ret[0]}\n{ret[1]} {ret[2]} sm\nPrice: {ret[3] * ret[4]} sum\nQuantity: {ret[4]}',
            reply_markup=client_kb_eng.inline_cart)

    for a in cur.execute('select sum(menu.price*amount) from cart, menu where ido=(select id from orders '
                         'where dateC=date() and idu=? and received=0) and menu.id=cart.idm',
                         (callback.message.chat.id,)).fetchone():
        await callback.message.answer(f'Total cost of the order: {a} sum')


async def delete_order(message):
    cur.execute(
        'delete from cart where idm=(select id from orders where dateC=date() and idu=? and received=0 and send=0)',
        (message.chat.id,))
    cur.execute('delete from orders where idu=? and dateC=date() and received=0 and send=0', (message.chat.id,))
    base.commit()


async def clear_cart(message):
    cur.execute('delete from cart where idm=(select id from orders where dateC=date() and idu=? and received=0)',
                (message.chat.id,))


async def check_number(message):
    for i in cur.execute('select pnumber from user where chat_id=?', (message.chat.id,)).fetchone():
        if i == '0':
            await message.answer(
                'Пожалуйста нажмите на кнопку "📱Отправить номер телефона", без номера телефона заказ невозможен')
        else:
            await message.answer('Отправьте пожалуйста ваше местоположение😊', reply_markup=client_kb_ru.kb_address)


async def check_number_uz(message):
    for i in cur.execute('select pnumber from user where chat_id=?', (message.chat.id,)).fetchone():
        if i == '0':
            await message.answer(
                'Iltimos, "📱 Telefon raqamini yuborish" tugmasini bosing, telefon raqamisiz buyurtma berish mumkin emas')
        else:
            await message.answer('Iltimos, manzilingizni yuboring😊', reply_markup=client_kb_uz.kb_address)


async def check_number_eng(message):
    for i in cur.execute('select pnumber from user where chat_id=?', (message.chat.id,)).fetchone():
        if i == '0':
            await message.answer(
                'Please click on the button "📱 Send phone number", without a phone number the order is not possible')
        else:
            await message.answer('Please send your location😊', reply_markup=client_kb_eng.kb_address)


async def star(message):
    cur.execute('update orders set star=? where idu=? and received=1 and send=1 and dateC=date()'
                , (message.text, message.chat.id,))
    base.commit()
    for b in cur.execute('select lang from user '
                         'where chat_id=?', (message.chat.id,)).fetchone():
        if b == 'ru':
            await message.answer('Напишите подробный отзыв, если хотите', reply_markup=client_kb_ru.dont_want)
        elif b == 'uz':
            await message.answer('Agar xohlasangiz, batafsil sharh yozing)', reply_markup=client_kb_uz.dont_want)
        elif b == 'eng':
            await message.answer('Write a detailed review if you want)', reply_markup=client_kb_eng.dont_want)


async def feedback(message):
    cur.execute('update orders set star=? where idu=? and received=1 and send=1 and dateC=date()'
                , (message.text, message.chat.id,))
    base.commit()
    for b in cur.execute('select lang from user '
                         'where chat_id=?', (message.chat.id,)).fetchone():
        if b == 'ru':
            await bot.send_message(message.chat.id, 'Спасибо за отзыв, вы улучшаете наш сервис😊',
                                   reply_markup=client_kb_ru.kb_main)
        elif b == 'uz':
            await bot.send_message(message.chat.id, 'Mulohazangiz uchun rahmat, xizmatimizni yaxshilaysiz😊',
                                   reply_markup=client_kb_uz.kb_main)
        elif b == 'eng':
            await bot.send_message(message.chat.id, 'Thank you for your feedback, you improve our service😊',
                                   reply_markup=client_kb_eng.kb_main)

    for ret in cur.execute('select id, star, feedback, first_name, pnumber from main.orders'
                           ' inner join user on chat_id = orders.idu where idu=? and received=1 and send=1 and dateC=date()'
            , (message.chat.id,)):
        await bot.send_message(596927092, f'Пришел отзыв!!!\n {ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}')


async def amount():
    a = bot.message.text.split()
    cur.execute('select amount from cart where idm=(select id from menu where '
                '((name=? or name=?) and (psize=? or psize=?)) or (name=? or name=?) and ido=?)',
                (a[3], a[3] + ' ' + a[4], a[4], a[5], a[3], a[3] + ' ' + a[4], a[2],)).fetchone()
