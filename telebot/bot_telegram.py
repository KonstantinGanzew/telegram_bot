from aiogram.utils import executor
from create_bot import dp
from googleDisk import google
from handlers import news

async def on_startup(_):
    print('Бот запущен')
    await google.open_driveID()
    await google.get_news()
    await news.scheduler()



from handlers import client, admin

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
