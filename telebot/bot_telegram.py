from aiogram.utils import executor
from create_bot import dp
from googleDisk import google

async def on_startup(_):
    print('Бот запущен')
    google.open_driveID()
    google.get_news()



from handlers import client, admin

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
