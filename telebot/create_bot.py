from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

bot = Bot('1810556658:AAHPm_ngxFX3CyYXohrUQ_AB4_XwjgzzB8I')
dp = Dispatcher(bot, storage=MemoryStorage())