from email import message
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_client, kb_direct
from handlers import news, company, direct, docks, EBITDA, person
from googleDisk import google_test


aut_id = google_test.open_driveID()
aut_id.append(225923687)

# Обрабатываем комманды
async def command_start(message: types.Message):
    for item in aut_id:
        await bot.send_message(item, 'Привет👋\n\
            Я твой виртуальный помощник 🤖. Мои разработчики не\n\
            могут определиться как меня называть. Они мне сказали, что\n\
            важно мнение каждого сотрудника и попросили спросить у\n\
            тебя. Отправь, пожалуйста, свой вариант моего имени ответом \n\
            на это сообщение.')


# Регистрируем комманды
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
