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
    staf = google.EMPLOYEES
    name_key = message.text
    await state.finish()
    it = 0
    for staff in staf:
        s = ''
        for i in staff:
            s  += i.strip().lower() + ' '
            if s.find(name_key.lower()) != -1:
                await bot.send_message(message.from_user.id, f'Имя: {staff[1]}\nФамилия: {staff[0]}\nОтчество: {staff[2]}\nДата рождения: {staff[4]}\nНомер телефона: +7{staff[7]}\nЛичный email: {staff[6]}\nКомпания: {staff[8]}\nДолжность: {staff[9]}')
                await asyncio.sleep(1)
                if staff[7] != '':
                    await bot.send_contact(message.from_user.id, f'+7{staff[7]}', f'{staff[0]} {staff[1]}')
                else:
                    await bot.send_message(message.from_user.id, 'Нет контакта')
                await asyncio.sleep(1)
                it += 1
                break
        s = ''
    if it == 0:
        await bot.send_message(message.from_user.id, "Контакт не найден")
    else:
        it = 0

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
