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
    staff = google.open_list_employees(message.text)
    await state.finish()    
    await bot.send_message(message.chat.id, f'Имя: {staff[0]} {staff[1]} {staff[2]}\nДата рождения: {staff[4]}\nemail: {staff[5]}\nНомер телефона: {staff[6]}\nМесто работы: {staff[7]}\nДолжность: {staff[8]}', kb_person)


async def command_person(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_person)
    await message.delete()


@dp.message_handler(Text(equals='🔍 Сотрудники компании'), state=None)
async def search_employees(message: types.Message):
    await bot.send_message(message.from_user.id, 'Нажмите на кнопку найти, далее напишите имя, фамилию\nномер телефона в формате 9*********\nдолжность', reply_markup=kb_answer)
    await search_state.var_name.name.set()


@dp.message_handler(Text(equals='🈺 Вакансии компании'))
async def vac(message: types.Message):
    vacancy = parse(True)
    for item in vacancy:
        await bot.send_message(message.from_user.id, item)