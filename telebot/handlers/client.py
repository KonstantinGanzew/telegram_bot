from email import message
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from googleDisk import google_test


aut_id = google_test.open_driveID()
aut_id.append(225923687)

# Обрабатываем комманды
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте @lisenokstr Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}')


# Регистрируем комманды
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
