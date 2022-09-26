from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_client, kb_direct, kb_docks
from handlers import news, company, direct, docks, EBITDA, person, feedback
from googleDisk import google

name_OK = '@denis_chekin'

# Обрабатываем комманды
async def command_start(message: types.Message):
    try:
        if message.chat.id != -1001469485742:
            if autentication(message.from_user.id):
                await send_dir(message.from_user.id)
            else:
                await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте {name_OK} Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}')
    except Exception as e:
        await message.answer('Пиши в личку')
        print(e)

# Проверка на авторизацию
def autentication(message):
    for item in google.ID_TEL:
        if item == message:
            return True
    return False


# Обращение директора
async def send_dir(message):
    photo = open('photo_dir.jpg', 'rb')
    await bot.send_photo(message, photo, 'Дорогие коллеги и друзья!')
    await bot.send_message(message, 'Наша компания существует с 2005 года. С самого начала мы установили для себя ряд ключевых ценностей, которыми руководствуемся в нашей работе и в настоящее время. Все они отражены в Принципах и политиках компании – документу, знакомому каждому из вас. Неизменное следование им в любой ситуации позволяет нашей компании с честью проходить через все сложности и изменения, продолжая развиваться и сохранять стабильность. \nЯ хотел бы выразить признательность каждому из вас за участие в процессе развития компании. Именно благодаря вам мы занимаем лидирующие позиции в автомобильном бизнесе своего региона, расширяем наше присутствие в соседних регионах.\nРеализация нового проекта корпоративного Телеграм бота – это еще один шаг на пути к достижению нашей цели:\n«Стать лучшими в представленных городах Республики Башкортостан и Российской Федерации в автомобильном бизнесе, стать номером один в продажах автомобилей как новых, так и с пробегом, это значит продавать больше всех автомобилей и предложить нашим клиентам лучший сервис в обслуживании автомобилей».\nЯ верю, что этот проект поможет вам стать более эффективными за счет экономии времени на поиск информации, создания единого информационного поля и корпоративного пространства.\nИ призываю вас принять активное участие в его совершенствовании. Благодаря вашим идеям, предложениям, замечаниям он станет лучшим инструментом корпоративного общения.', reply_markup=kb_client)

# Ввыдим новости
@dp.message_handler(Text(equals=['Новости']))
async def point_new(message: types.Message):
    if autentication(message.from_user.id):
        await news.command_news(message)
    else:
        await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте {name_OK} Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}', reply_markup=types.ReplyKeyboardRemove())


# Ввыводим документы
@dp.message_handler(Text(equals=['Документы']))
async def point_docks(message: types.Message):
    if autentication(message.from_user.id):
        await docks.command_docks(message)
    else:
        await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте {name_OK} Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}', reply_markup=types.ReplyKeyboardRemove())



# Ввыводим Персонал
@dp.message_handler(Text(equals=['Персонал']))
async def point_person(message: types.Message):
    if autentication(message.from_user.id):
        await person.command_person(message)
    else:
        await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте {name_OK} Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}', reply_markup=types.ReplyKeyboardRemove())


# Ввыводим EBITDA
@dp.message_handler(Text(equals=['EBITDA']))
async def point_EBITDA(message: types.Message):
    if autentication(message.from_user.id):
        await news.command_news(message)
    else:
        await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте {name_OK} Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}', reply_markup=types.ReplyKeyboardRemove())



# Ввыводим Пярмая связь
@dp.message_handler(Text(equals=['Прямая связь']))
async def point_direct(message: types.Message):
    if autentication(message.from_user.id):
        await direct.command_direct(message)
    else:
        await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте {name_OK} Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}', reply_markup=types.ReplyKeyboardRemove())


# О компании
@dp.message_handler(Text(equals=['О компании']))
async def point_company(message: types.Message):
    if autentication(message.from_user.id):
        await company.command_company(message)
    else:
        await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте {name_OK} Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}', reply_markup=types.ReplyKeyboardRemove())



# Назад
@dp.message_handler(Text(equals=['Назад']))
async def point_company(message: types.Message):
    if autentication(message.from_user.id):
        await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_client)
    else:
        await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте {name_OK} Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}', reply_markup=types.ReplyKeyboardRemove())



# Выходи из пункта обращения
@dp.message_handler(Text(equals=['Haзад']))
async def point_company(message: types.Message):
    if autentication(message.from_user.id):
        await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_direct)
    else:
        await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте {name_OK} Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}', reply_markup=types.ReplyKeyboardRemove())



# Выходи из пункта образцы заявлений
@dp.message_handler(Text(equals=['Hазaд']))
async def point_company(message: types.Message):
    if autentication(message.from_user.id):
        await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_docks)
    else:
        await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте {name_OK} Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}', reply_markup=types.ReplyKeyboardRemove())



# Регистрируем комманды
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
