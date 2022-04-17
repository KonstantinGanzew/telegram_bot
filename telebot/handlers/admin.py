from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_admin, kb_answer
from googleDisk import google_test
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from handlers import name_variation


async def command_manager(message: types.Message):
    if message.from_user.id == 225923687:
        await bot.send_message(message.from_user.id, 'Необходимо нажать на опубликовать!!', reply_markup=kb_admin)
    else:
        await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте @lisenokstr Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}')

@dp.message_handler(Text(equals=['Опубликовать новость']))
async def public_message(message: types.Message):
    for item in google_test.open_driveID():
        try:
            await bot.send_message(item, 'Привет👋\nЯ твой виртуальный помощник 🤖. Мои разработчики не\nмогут определиться как меня называть. Они мне сказали, что\nважно мнение каждого сотрудника и попросили спросить у\nтебя. Отправь, пожалуйста, свой вариант моего имени ответом \nна это сообщение.', reply_markup=kb_answer)
        except:
            google_test.down_drive("ID сотрудника", item, "Сотрудник остановил бота")

@dp.message_handler(Text(equals=['Ответить']), state=None)
async def take_first_state(message: types.Message):
    await name_variation.var_name.name.set()


@dp.message_handler(state=name_variation.var_name)
async def down_answer_to_disk(message: types.Message, state: FSMContext):
    first_name = str(message.chat.first_name)
    username = str(message.chat.username)
    text = str(message.text)
    google_test.down_drive(first_name, username, text)
    await message.answer("Спасибо за ваши ответы!", reply_markup=ReplyKeyboardRemove())
    await state.finish()


# Регистрируем комманды
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(command_manager, commands=['start'])