from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from googleDisk import google


async def command_manager(message: types.Message):
    if message.from_user.id == 225923687:
        await bot.send_message(message.from_user.id, 'Необходимо нажать на опубликовать!!')


# Регистрируем комманды
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(command_manager, commands=['manager'])