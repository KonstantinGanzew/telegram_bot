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
    staf = google.open_list_employees(message.text)
    await state.finish()
    if staf:
        for staff in staf:
            await bot.send_message(message.from_user.id, f'Имя: {staff[1]}\nФамилия: {staff[0]}\nОтчество: {staff[2]}\nДата рождения: {staff[4]}\nНомер телефона: +7{staff[7]}\nЛичный email: {staff[6]}\nЮрлицо где оформлен сотрудник: {staff[8]}\nДолжность: {staff[9]}')
            await bot.send_contact(message.from_user.id, f'+7{staff[7]}', f'{staff[0]} {staff[1]}')
    else:
        await bot.send_message(message.from_user.id, "Контакт не найден")

async def command_person(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_person)
    await message.delete()


@dp.message_handler(Text(equals='🔍 Сотрудники компании'))
async def search_employees(message: types.Message):
    await search_state.var_name.name.set()
    await bot.send_message(message.from_user.id, 'Нажмите на кнопку найти, далее напишите имя, фамилию\nномер телефона в формате 9*********\nдолжность')


@dp.message_handler(Text(equals='🈺 Вакансии компании'))
async def vac(message: types.Message):
    vacancy = parse(True)
    for item in vacancy:
        await bot.send_message(message.from_user.id, item)