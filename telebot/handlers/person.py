import asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot
from keyboards import kb_person, kb_answer
from parsers import parse
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from googleDisk import google
from aiogram import types
from aiogram.dispatcher import FSMContext
from handlers import search_state


@dp.message_handler(state=search_state.var_name)
async def take_first_state(message: types.Message, state: FSMContext):
    staff = google.SEARCH_PERSON
    employes = google.EMPLOYEES
    name_key = message.text
    if name_key.find(' ') != -1:
        name_key = name_key.split(' ')
        name_key = f'{name_key[0].capitalize()} {name_key[1].capitalize()}'
    else:
        name_key = name_key.capitalize()
    await state.finish()
    finds = True
    for i, a in enumerate(staff):
        s = ''
        if name_key in ' '.join(a):
            s = f'Фамилия: {employes[i][0]}\nИмя: {employes[i][1]}\nОтчество: {employes[i][2]}\nДата рождения: {employes[i][4]}\n'
            if employes[i][6] != '':
                s += f'Личный email: {employes[i][6]}\n'
            if employes[i][7] != '':
                s += f'Номер телефона: +7{employes[i][7]}\n'
            if employes[i][8] != '':
                s += f'Компания: {employes[i][8]}\n'
            if employes[i][9] != '':
                s += f'Должность: {employes[i][9]}'
            if employes[i][7] != '':
                await asyncio.sleep(1)
                await bot.send_message(message.from_user.id, s)
                await asyncio.sleep(1)
                await bot.send_contact(message.from_user.id, f'+7{employes[i][7]}', f'{employes[i][0]} {employes[i][1]}')
            else:
                await asyncio.sleep(1)
                await bot.send_message(message.from_user.id, s)
            finds = False
    if finds:
        await bot.send_message(message.from_user.id, "Контакт не найдет")



async def command_person(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_person)
    await message.delete()


@dp.message_handler(Text(equals='🔍 Сотрудники компании'))
async def search_employees(message: types.Message):
    await search_state.var_name.name.set()
    await bot.send_message(message.from_user.id, 'Напишите имя, фамилию\nномер телефона в формате 9*********\nдолжность')
    await message.delete()


@dp.message_handler(Text(equals='🈺 Вакансии компании'))
async def vac(message: types.Message):
    vacancy = parse(True)
    for item in vacancy:
        await bot.send_message(message.from_user.id, item)
        await asyncio.sleep(1)
    await message.delete()

@dp.message_handler(Text(equals='📖 Бизнес-процессы'))
async def business_processes(message: types.Message):
    await bot.send_message(message.from_user.id, 'Раздел в разработке')
    await message.delete()

@dp.message_handler(Text(equals='📈 Развитие персонала'))
async def staff_development(message: types.Message):
    await bot.send_message(message.from_user.id, 'Раздел в разработке')
    await message.delete()

@dp.message_handler(Text(equals='📋 Калькулятор вознаграждения'))
async def reward_calculator(message: types.Message):
    await bot.send_message(message.from_user.id, 'Раздел в разработке')
    await message.delete()

@dp.message_handler(Text(equals='📝 Лист мотивации'))
async def motivation_sheet(message: types.Message):
    await bot.send_message(message.from_user.id, 'Раздел в разработке')
    await message.delete()

@dp.message_handler(Text(equals='Библиотека компании'))
async def company_library(message: types.Message):
    await bot.send_message(message.from_user.id, 'Раздел в разработке')
    await message.delete()
