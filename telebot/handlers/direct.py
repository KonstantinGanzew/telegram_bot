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
from googleDisk import google

# В данном методе ищем номер сотрудника по его телеграм ид
def search_company(mes):
    staff = google.EMPLOYEES
    for st in staff:
        for s in st:
            try:
                if int(s) == mes:
                    return st[7]
            except:
                continue

# Отлавливаем нажатие кнопки "Прямая связь", отправляем следующие кнопки 'Передать проблему', 'Обращение к директору', 'Назад' 
# 225923687, -1001720658480
async def command_direct(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_direct)
    await message.delete()


@dp.message_handler(Text(equals='Обращение к директору'))
async def appeal_to_the_director(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_dir_send)


@dp.message_handler(Text(equals='Передать проблему'), state=None)
async def submit_problem(message: types.Message):
    await feedback.var_name.mes.set()
    kb_without_photo = ReplyKeyboardMarkup(resize_keyboard=True).add('Отправить без фотографии').add('Отмена')
    await bot.send_message(message.from_user.id, 'Необходимо написать сообщение проблемы', reply_markup=kb_without_photo)
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
    mes_text = str(data['mes'])
    await bot.send_photo(-1001720658480, data['photo'], f'Имя: {message.from_user.full_name}\nID: @{message.from_user.username}\nНомер: +7{search_company(message.from_user.id)}\nОбращение: {mes_text}')
    await state.finish()
    await bot.send_message(message.from_user.id, 'Обращение отправленно', reply_markup=kb_direct)

@dp.message_handler(Text(equals='Отправить без фотографии'), state=feedback.var_name.mes)
async def send_message_without_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        message_text = data['mes']
    await bot.send_message(-1001720658480, f'Имя: {message.from_user.full_name}\nID: @{message.from_user.username}\nНомер: +7{search_company(message.from_user.id)}\nОбращение: {message_text}')
    await state.finish()
    await bot.send_message(message.from_user.id, 'Обращение отправленно', reply_markup=kb_direct)


#<-----------------------------------------Персональное----------------------------------------->
# 225923687, 185161895

""" 
    Отправляем сообщение директору, имя, ид, номер, сотрудника
    В первом блоке отплавливаем нажатие кнопки "Персонализировано"
    Далее запускаем машину состояния на первое сообщение и ожидаем пока оно придет от пользователя,
    после закрываем работу машины состояния и чистим буфер, отправляем сообщения полученые от пользователя

"""
@dp.message_handler(Text(equals='Персонализировано'), state=None)
async def personalized(message: types.Message):
    await not_anonymous_send.messages.mes.set()
    await bot.send_message(message.from_user.id, 'Передать проблему директору')
    await message.delete()

@dp.message_handler(state=not_anonymous_send.messages.mes)
async def anonymous_to_director(message: types.Message, state: FSMContext):
    message_text = message.text
    await state.finish()
    await bot.send_message(185161895, f'Имя: {message.from_user.full_name}\nID: @{message.from_user.username}\nНомер: +7{search_company(message.from_user.id)}\nОбращение: {message_text}')
    await bot.send_message(message.from_user.id, 'Обращение отправленно')


#<-----------------------------------------Персональное----------------------------------------->
# 185161895, 225923687

""" 
    Отправляем сообщение директору анонимно
    В первом блоке отплавливаем нажатие кнопки "Персонализировано"
    Далее запускаем машину состояния на первое сообщение и ожидаем пока оно придет от пользователя,
    после закрываем работу машины состояния и чистим буфер, отправляем сообщения полученые от пользователя

"""
@dp.message_handler(Text(equals='Анонимно'), state=None)
async def anonymously(message: types.Message):
    await anonymous_send.not_messages.mes.set()
    await bot.send_message(message.from_user.id, 'Передать проблему директору анонимно')
    await message.delete()

@dp.message_handler(state=anonymous_send.not_messages.mes)
async def not_anonymous_to_director(message: types.Message, state: FSMContext):
    message_text = message.text
    await state.finish()
    await bot.send_message(185161895, f'Анонимно\nОбращение: {message_text}')
    await bot.send_message(message.from_user.id, 'Обращение отправленно анонимно')


@dp.message_handler(Text(equals='Отмена'), state='*')
async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish
    await bot.send_message(message.from_user.id, 'Обращение отменено', reply_markup=kb_direct)