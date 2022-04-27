from email import message
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_client, kb_direct
from handlers import news, company, direct, docks, EBITDA, person
from googleDisk import google


aut_id = google.id_telegram()
aut_id.append(225923687)

# Обрабатываем комманды
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'test', reply_markup=kb_client)
        print(message)
    except:
        await message.answer("Пшел ты! педик")
#    if autentication(message):
#        await send_dir(message)
#        for item in aut_id:
#            await bot.send_message(item, 'Привет👋\nЯ твой виртуальный помощник 🤖. Мои разработчики не могут определиться как меня называть. Они мне сказали, что важно мнение каждого сотрудника и попросили спросить у тебя. Отправь, пожалуйста, свой вариант моего имени ответом на это сообщение.')
#
#    else:
#        for item in aut_id:
#            await bot.send_message(item, 'Привет👋\nЯ твой виртуальный помощник 🤖. Мои разработчики не могут определиться как меня называть. Они мне сказали, что важно мнение каждого сотрудника и попросили спросить у тебя. Отправь, пожалуйста, свой вариант моего имени ответом на это сообщение.')

#        await send_dir(message)
#        await bot.send_message(message.from_user.id, f'Для доступа к боту отправьте @lisenokstr Ваши ФИО, адрес личной электронной почты и id {message.from_user.id}', reply_markup=kb_client)
        #aut_id.append(message.from_user.id)

# Проверка на авторизацию
def autentication(message):
    for item in aut_id:
        if message.chat.id == item:
            return True


# Обращение директора
async def send_dir(message):
    photo = open('photo_dir.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, 'Дорогие коллеги и друзья!')
    await bot.send_message(message.from_user.id, 'Наша компания существует с 2005 года. С самого начала мы установили для себя ряд ключевых ценностей, которыми руководствуемся в нашей работе и в настоящее время. Все они отражены в Принципах и политиках компании – документу, знакомому каждому из вас. Неизменное следование им в любой ситуации позволяет нашей компании с честью проходить через все сложности и изменения, продолжая развиваться и сохранять стабильность. \nЯ хотел бы выразить признательность каждому из вас за участие в процессе развития компании. Именно благодаря вам мы занимаем лидирующие позиции в автомобильном бизнесе своего региона, расширяем наше присутствие в соседних регионах.\nРеализация нового проекта корпоративного Телеграм бота – это еще один шаг на пути к достижению нашей цели:\n«Стать лучшими в представленных городах Республики Башкортостан и Российской Федерации в автомобильном бизнесе, стать номером один в продажах автомобилей как новых, так и с пробегом, это значит продавать больше всех автомобилей и предложить нашим клиентам лучший сервис в обслуживании автомобилей».\nЯ верю, что этот проект поможет вам стать более эффективными за счет экономии времени на поиск информации, создания единого информационного поля и корпоративного пространства.\nИ призываю вас принять активное участие в его совершенствовании. Благодаря вашим идеям, предложениям, замечаниям он станет лучшим инструментом корпоративного общения.')

# Ввыдим новости
@dp.message_handler(Text(equals=['Новости']))
async def point_new(message: types.Message):
    await news.command_news(message)

# Ввыводим документы
@dp.message_handler(Text(equals=['Документы']))
async def point_docks(message: types.Message):
    await docks.command_docks(message)

# Ввыводим Персонал
@dp.message_handler(Text(equals=['Персонал']))
async def point_person(message: types.Message):
    await person.command_person(message)

# Ввыводим EBITDA
@dp.message_handler(Text(equals=['EBITDA']))
async def point_EBITDA(message: types.Message):
    await news.command_news(message)

# Ввыводим Пярмая связь
@dp.message_handler(Text(equals=['Прямая связь']))
async def point_direct(message: types.Message):
    await direct.command_direct(message)

# О компании
@dp.message_handler(Text(equals=['О компании']))
async def point_company(message: types.Message):
    await company.command_company(message)

# Назад
@dp.message_handler(Text(equals=['Назад']))
async def point_company(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_client)

# Выходи из пункта обращения
@dp.message_handler(Text(equals=['Haзад']))
async def point_company(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_direct)



# Регистрируем комманды
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
