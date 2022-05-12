from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config

<<<<<<< HEAD
bot = Bot(config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
=======
bot = Bot()
dp = Dispatcher(bot, storage=MemoryStorage())
>>>>>>> a08a852ee40a1fb383033d8a760d8a20b6b3ddb3
