import asyncio

from aiogram import executor, types
from create_bot import dp
from handlers import client, admin
from sql import sql_db


async def on_startup(_):
    print('Bot awaked')
    sql_db.sql_start()
    asyncio.create_task(sql_db.scheduler())


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
