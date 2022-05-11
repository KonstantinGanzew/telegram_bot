import asyncio
from handlers import client
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
    staff = google.EMPLOYEES
    name_org = ''
    for st in staff:
        for s in st:
            try:
                if int(s) == message.from_user.id:
                    name_org = st[8]
                    break
            except:
                continue
    name_file = google.search_file(name_org, 0)
    for name in name_file:
        await bot.send_document(message.from_user.id, open(name, 'rb'))
        await asyncio.sleep(1)


@dp.message_handler(Text(equals='Приказы'))
async def sample_applications(message: types.Message):
    staff = google.EMPLOYEES
    name_org = ''
    for st in staff:
        for s in st:
            try:
                if int(s) == message.from_user.id:
                    name_org = st[8]
                    break
            except:
                continue
    name_file = google.search_file(name_org, 2)
    for name in name_file:
        await bot.send_document(message.from_user.id, open(name, 'rb'))
        await asyncio.sleep(1)


@dp.message_handler(Text(equals='Регламенты'))
async def sample_applications(message: types.Message):
    pass


@dp.message_handler(Text(equals='Положения'))
async def sample_applications(message: types.Message):
    staff = google.EMPLOYEES
    name_org = ''
    for st in staff:
        for s in st:
            try:
                if int(s) == message.from_user.id:
                    name_org = st[8]
                    break
            except:
                continue
    name_file = google.search_file(name_org, 1)
    for name in name_file:
        await bot.send_document(message.from_user.id, open(name, 'rb'))
        await asyncio.sleep(1)


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


