from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot
from keyboards import kb_direct, kb_dir_send

async def command_direct(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_direct)
    await message.delete()


@dp.message_handler(Text(equals='Обращение к директору'))
async def appeal_to_the_director(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_dir_send)


@dp.message_handler(Text(equals='Передать проблему'), state=None)
async def submit_problem(message: types.Message):
    pass


@dp.message_handler(Text(equals='Персонализировано'), state=None)
async def personalized(message: types.Message):
    pass


@dp.message_handler(Text(equals='Анонимно'), state=None)
async def anonymously(message: types.Message):
    pass
