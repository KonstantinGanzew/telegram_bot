from http import client
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_company
from handlers import client

# Отрисовываем подменю
async def command_company(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_company)
    await message.delete()


# Ввыводим обращение директора
@dp.message_handler(Text(equals=['Обращение директора']))
async def send_director(message: types.Message):
    await client.send_dir(message)


# Ввывоим оргструктуру
@dp.message_handler(Text(equals=['Оргструктура']))
async def organ_structure(message: types.Message):
    await message.reply_document(open('Оргструктура.pdf', 'rb'))


# Ввыводим историю компании
@dp.message_handler(Text(equals=['История компании']))
async def hystory_compamy(message: types.Message):
    await message.reply_document(open('История компании.pdf', 'rb'))


# Ввыводим принципы компании
@dp.message_handler(Text(equals=['Принципы и политики компании']))
async def principles(message: types.Message):
    await message.reply_document(open('Принципы и политики компании.pdf', 'rb'))
