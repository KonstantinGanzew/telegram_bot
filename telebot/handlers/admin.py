from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_admin, kb_answer
from googleDisk import google_test
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command


async def command_manager(message: types.Message):
    if message.from_user.id == 225923687:
        await bot.send_message(message.from_user.id, 'Необходимо нажать на опубликовать!!', reply_markup=kb_admin)

@dp.message_handler(Text(equals=['Опубликовать новость']))
async def public_message(message: types.Message):
    for item in google_test.open_driveID():
        await bot.send_message(item, 'Привет👋\n\
            Я твой виртуальный помощник 🤖. Мои разработчики не\n\
            могут определиться как меня называть. Они мне сказали, что\n\
            важно мнение каждого сотрудника и попросили спросить у\n\
            тебя. Отправь, пожалуйста, свой вариант моего имени ответом \n\
            на это сообщение.', reply_markup=kb_answer)

@dp.message_handler(Text(equals=['Ответить']), state=None)
async def take_first_state(message: types.Message):
    pass


# Регистрируем комманды
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(command_manager, commands=['manager'])