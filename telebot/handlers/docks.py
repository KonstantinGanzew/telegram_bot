import asyncio
from handlers import client
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_docks, kb_sample
from googleDisk import google

def search_company(mes):
    staff = google.EMPLOYEES
    for st in staff:
        for s in st:
            try:
                if int(s) == mes:
                    return st[8]
            except:
                continue

async def command_docks(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_docks)
    await message.delete()


@dp.message_handler(Text(equals='Образцы заявлений'))
async def sample_applications(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_sample)
    await message.delete()


@dp.message_handler(Text(equals='Выход из отпуска, уход за ребёнком'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'выход из отпуска, уход за ребёнком')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


@dp.message_handler(Text(equals='Обходной лист, увольнение'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Обходной лист, увольнение')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Отгул'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Отгул')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Отпуск, без содержания'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Отпуск, без содержания')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Отпуск, ежегодный'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Отпуск, ежегодный')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Отпуск, беременность'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Отпуск, беременность')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Перевод, 0,5 ставки'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Перевод, 0,5 ставки')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Перевод, временно'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Перевод, временно')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Перевод, другая должность'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Перевод, другая должность')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Перечень, документы'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Перечень, документы')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Прием'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Прием')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Прием, совмещение'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Прием, совмещение')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Увольнение'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Увольнение')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


@dp.message_handler(Text(equals='Приказы'))
async def sample_applications(message: types.Message):
    name_org = search_company(message.from_user.id)
    name_file = google.search_file(name_org, 2)
    for name in name_file:
        await bot.send_document(message.from_user.id, open(name, 'rb'))
        await asyncio.sleep(1)


@dp.message_handler(Text(equals='Регламенты'))
async def sample_applications(message: types.Message):
    await bot.send_message(message.from_user.id, 'Раздел в разработке')
    await message.delete()


@dp.message_handler(Text(equals='Положения'))
async def sample_applications(message: types.Message):
    name_org = search_company(message.from_user.id)
    name_file = google.save_file(name_org, 1)
    for name in name_file:
        await bot.send_document(message.from_user.id, open(name, 'rb'))
        await asyncio.sleep(1)


@dp.message_handler(Text(equals='Уставные документы'))
async def sample_applications(message: types.Message):
    await bot.send_message(message.from_user.id, 'Раздел в разработке')
    await message.delete()


@dp.message_handler(Text(equals='Карты партнера'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Карта партнера')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


@dp.message_handler(Text(equals='Фирменные бланки'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Фирменный бланк')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


@dp.message_handler(Text(equals='Листы мотивации'))
async def sample_applications(message: types.Message):
    await bot.send_message(message.from_user.id, 'Раздел в разработке')
    await message.delete()
