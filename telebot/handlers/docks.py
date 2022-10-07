import asyncio
from handlers import client
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from create_bot import dp, bot
from keyboards import kb_docks, kb_sample, kb_provisions_key, kb_partner_cards, kb_letterhead, kb_statory_documents
from googleDisk import google
from handlers import tags

def search_company(mes):
    staff = google.EMPLOYEES
    for st in staff:
        for s in st:
            try:
                if int(s) == mes:
                    return st[8]
            except:
                continue

async def command_docks(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_docks)
    await message.delete()


@dp.message_handler(Text(equals='Образцы заявлений'))
async def sample_applications(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_sample)
    await message.delete()


@dp.message_handler(Text(equals='Выход из отпуска, уход за ребёнком'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'выход из отпуска, уход за ребёнком')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


@dp.message_handler(Text(equals='Обходной лист, увольнение'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Обходной лист, увольнение')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Отгул'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Отгул')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Отпуск, без содержания'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Отпуск, без содержания')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Отпуск, ежегодный'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Отпуск, ежегодный')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Отпуск, беременность'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Отпуск, беременность')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Перевод, 0,5 ставки'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Перевод, 0,5 ставки')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Перевод, временно'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Перевод, временно')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Перевод, другая должность'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Перевод, другая должность')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Перечень, документы'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Перечень, документы')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Прием'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Прием')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Прием, совмещение'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Прием, совмещение')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Увольнение'))
async def sample_applications(message: types.Message):
    name_file = google.search_filename(search_company(message.from_user.id), 'Увольнение')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


@dp.message_handler(Text(equals='Приказы'), state=None)
async def sample_applications(message: types.Message):
    name_org = search_company(message.from_user.id)
    id_tag = ''
    for tag in google.ID_ORDERS:
        if name_org == tag[1] or 'все компании' == tag[1]:
            if id_tag.find(tag[0]) == -1:
                id_tag += tag[0] + '\n'
    await bot.send_message(message.from_user.id, f'Введите запрос через #:\n{id_tag}')
    await tags.tags.tag.set()
    

@dp.message_handler(state=tags.tags.tag)
async def first_message_for_feedback(message: types.Message, state: FSMContext):
    tags = message.text.lower()
    name_org = search_company(message.from_user.id)
    for tag in google.ID_ORDERS:
        if tag[0] == tags and (name_org == tag[1] or 'все компании' == tag[1]):
            name_file = google.save_files(tag[2])
            await bot.send_document(message.from_user.id, open(name_file, 'rb'))
        else:
            continue
    await state.finish()


@dp.message_handler(Text(equals='Регламенты'))
async def sample_applications(message: types.Message):
    await bot.send_message(message.from_user.id, 'Раздел в разработке')
    await message.delete()


@dp.message_handler(Text(equals='Положения'))
async def sample_applications(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_provisions_key)
    await message.delete()


@dp.message_handler(Text(equals='Уставные документы'))
async def sample_applications(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_statory_documents)
    await message.delete()


@dp.message_handler(Text(equals='Карты партнера'))
async def sample_applications(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_partner_cards)
    await message.delete()


@dp.message_handler(Text(equals='Фирменные бланки'))
async def sample_applications(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_letterhead)
    await message.delete()


@dp.message_handler(Text(equals='Листы мотивации'))
async def sample_applications(message: types.Message):
    await bot.send_message(message.from_user.id, 'Раздел в разработке')
    await message.delete()



#<----------------------------------Блок с положением---------------------------------->



@dp.message_handler(Text(equals='О коммерческой тайне'))
async def about_trade_secret(message: types.Message):
    name_org = search_company(message.from_user.id)
    name_file = google.search_filename(name_org, 'Коммерческая тайна')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


@dp.message_handler(Text(equals='O компании'))
async def about_company(message: types.Message):
    name_org = search_company(message.from_user.id)
    name_file = google.search_filename(name_org, 'О компании')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


@dp.message_handler(Text(equals='О персональных данных'))
async def personal_data(message: types.Message):
    name_org = search_company(message.from_user.id)
    name_file = google.search_filename(name_org, 'Персональные данные')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


@dp.message_handler(Text(equals='Об оплате труда работников'))
async def wages_of_employees(message: types.Message):
    name_org = search_company(message.from_user.id)
    name_file = google.search_filename(name_org, 'Оплата труда работников')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


@dp.message_handler(Text(equals='О пропускном режиме'))
async def pass_mode(message: types.Message):
    name_org = search_company(message.from_user.id)
    name_file = google.search_filename(name_org, 'Пропускной режим')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


@dp.message_handler(Text(equals='ПВТР'))
async def pass_mode(message: types.Message):
    name_file = google.save_files('18qR3wqu7F9hKMRJhtupdu93V3EJEZ-vw')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


#<----------------------------------Карты партнера---------------------------------->



@dp.message_handler(Text(equals='ТАСКО-МОТОРС'))
async def TASCO_MOTORS(message: types.Message):
    name_file = google.search_filename('ТАСКО-МОТОРС', 'Карта партнера')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='ТАСКО-трейд'))
async def TASCO_trade(message: types.Message):
    name_file = google.search_filename('ТАСКО-трейд', 'Карта партнера')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Автотрейд'))
async def autotrade(message: types.Message):
    name_file = google.search_filename('Автотрейд', 'Карта партнера')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='СК Моторс'))
async def SK_Motors(message: types.Message):
    name_file = google.search_filename('СК Моторс', 'Карта партнера')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Сервис Плюс'))
async def Service_Plus(message: types.Message):
    name_file = google.search_filename('Сервис Плюс', 'Карта партнера')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='ИП Терехов'))
async def IP_Terekhov(message: types.Message):
    name_file = google.search_filename('ИП Терехов', 'Карта партнера')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='ИП Васильев'))
async def IP_Vasiliev(message: types.Message):
    name_file = google.search_filename('ИП Васильев', 'Карта партнера')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Орентранс'))
async def IP_Vasiliev(message: types.Message):
    name_file = google.search_filename('Орентранс', 'Карта партнера')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

#<----------------------------------Фирменные бланки---------------------------------->



@dp.message_handler(Text(equals='ТАСКО-МОТОРC'))
async def TASCO_MOTORS(message: types.Message):
    name_file = google.search_filename('ТАСКО-МОТОРС', 'Фирменный бланк')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='ТАСКO-трейд'))
async def TASCO_trade(message: types.Message):
    name_file = google.search_filename('ТАСКО-трейд', 'Фирменный бланк')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Aвтотрейд'))
async def autotrade(message: types.Message):
    name_file = google.search_filename('Автотрейд', 'Фирменный бланк')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='CК Моторс'))
async def SK_Motors(message: types.Message):
    name_file = google.search_filename('СК Моторс', 'Фирменный бланк')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Cервис Плюс'))
async def Service_Plus(message: types.Message):
    name_file = google.search_filename('Сервис Плюс', 'Фирменный бланк')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='ИП Tерехов'))
async def IP_Terekhov(message: types.Message):
    name_file = google.search_filename('ИП Терехов', 'Фирменный бланк')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='ИП Bасильев'))
async def IP_Vasiliev(message: types.Message):
    name_file = google.search_filename('ИП Васильев', 'Фирменный бланк')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()


#<----------------------------------Блок с уставом---------------------------------->


@dp.message_handler(Text(equals='ТAСКО-МОТОРС'))
async def TASCO_MOTORS(message: types.Message):
    name_file = google.search_filename('ТАСКО-МОТОРС', 'Устав')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='ТAСКО-трейд'))
async def TASCO_MOTORS(message: types.Message):
    name_file = google.search_filename('ТАСКО-трейд', 'Устав')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Автoтрейд'))
async def TASCO_MOTORS(message: types.Message):
    name_file = google.search_filename('Автотрейд', 'Устав')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='СK Моторс'))
async def TASCO_MOTORS(message: types.Message):
    name_file = google.search_filename('СК Моторс', 'Устав')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()

@dp.message_handler(Text(equals='Сeрвис Плюс'))
async def TASCO_MOTORS(message: types.Message):
    name_file = google.search_filename('Сервис Плюс', 'Устав')
    await bot.send_document(message.from_user.id, open(name_file, 'rb'))
    await message.delete()