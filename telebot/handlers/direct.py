from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot
from keyboards import kb_direct, kb_dir_send
from handlers import feedback
from handlers import not_anonymous_send
from handlers import anonymous_send

async def command_direct(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_direct)
    await message.delete()


@dp.message_handler(Text(equals='Обращение к директору'))
async def appeal_to_the_director(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_dir_send)


@dp.message_handler(Text(equals='Передать проблему'), state=None)
async def submit_problem(message: types.Message):
    await feedback.var_name.mes.set()
    await bot.send_message(message.from_user.id, 'Необходимо написать сообщение проблемы')
    await message.delete()

@dp.message_handler(state=feedback.var_name.mes)
async def first_message_for_feedback(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mes'] = message.text
    await feedback.var_name.next()
    await bot.send_message(message.from_user.id, 'Необходимо отправить фото')

@dp.message_handler(content_types=['photo'], state=feedback.var_name.photo)
async def second_message_for_feedback(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
    await bot.send_photo(1001720658480, data['photo'], str(data['mes']))
    await state.finish()



@dp.message_handler(Text(equals='Персонализировано'), state=None)
async def personalized(message: types.Message):
    await not_anonymous_send.messages.mes.set()
    await bot.send_message(message.from_user.id, 'Передать проблему директору')
    await message.delete()

@dp.message_handler(state=not_anonymous_send.messages.mes)
async def anonymous_to_director(message: types.Message, state: FSMContext):
    message_text = message.text
    await state.finish()
    await bot.send_message(331398137, f'Имя: {message.from_user.full_name}\nID: @{message.from_user.username}\nНомер: +7{}\nОбращение: {message_text}')

@dp.message_handler(Text(equals='Анонимно'), state=None)
async def anonymously(message: types.Message):
    await anonymous_send.not_messages.mes.set()
    await bot.send_message(message.from_user.id, 'Передать проблему директору анонимно')
    await message.delete()

@dp.message_handler(state=anonymous_send.not_messages.mes)
async def not_anonymous_to_director(message: types.Message, state: FSMContext):
    message_text = message.text
    await state.finish()
    await bot.send_message(331398137, f'Анонимно\nОбращение: {message_text}')