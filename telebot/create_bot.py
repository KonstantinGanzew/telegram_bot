from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

bot = Bot()
dp = Dispatcher(bot, storage=MemoryStorage())
