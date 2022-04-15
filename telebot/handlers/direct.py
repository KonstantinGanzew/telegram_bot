from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot
from keyboards import kb_direct, kb_dir_send

async def command_direct(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_direct)
    await message.delete()


@dp.message_handler(Text(equals='Обращение к директору'))
async def appeal_to_the_director(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_dir_send)