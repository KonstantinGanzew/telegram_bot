from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_docks
from googleDisk import google

async def command_docks(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_docks)
    await message.delete()


@dp.message_handler(Text(equals='Образцы заявлений'))
async def sample_applications(message: types.Message):
    name_file = google.search_file(search_organization(message.from_user.id), 0)
    for name in name_file:
        await bot.send_document(message.from_user.id, open(name, 'rb'))


@dp.message_handler(Text(equals='Приказы'))
async def sample_applications(message: types.Message):
    name_file = google.search_file(search_organization(message.from_user.id), 2)
    for name in name_file:
        await bot.send_document(message.from_user.id, open(name, 'rb'))


@dp.message_handler(Text(equals='Регламенты'))
async def sample_applications(message: types.Message):
    pass


@dp.message_handler(Text(equals='Положения'))
async def sample_applications(message: types.Message):
    name_file = google.search_file(search_organization(message.from_user.id), 1)
    for name in name_file:
        await bot.send_document(message.from_user.id, open(name, 'rb'))


@dp.message_handler(Text(equals='Уставные документы'))
async def sample_applications(message: types.Message):
    pass


@dp.message_handler(Text(equals='Карты партнера'))
async def sample_applications(message: types.Message):
    pass


@dp.message_handler(Text(equals='Фирменные бланки'))
async def sample_applications(message: types.Message):
    pass


@dp.message_handler(Text(equals='Листы мотивации'))
async def sample_applications(message: types.Message):
    pass


async def search_organization(mas_id):
    staff = google.EMPLOYEES
    for st in staff:
        if st[5] == mas_id:
            return st[8]
