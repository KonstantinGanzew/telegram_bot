import asyncio
from aiogram.utils import executor
from create_bot import dp
from googleDisk import google
from handlers import news

async def on_startup(_):
    print('Бот запущен')
    asyncio.create_task(news.scheduler())
    asyncio.create_task(google.open_driveID())
    asyncio.create_task(google.get_news())
    asyncio.create_task(google.id_docks())


from handlers import client

client.register_handlers_client(dp)
#admin.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
