import copy
import datetime
import aioschedule
import logging
import asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_news
from googleDisk import google

"""date = i[5].split()
        date1 = date[0].split('.')
        date2 = date[1].split(':')
        d1 = datetime(int(date1[2]), int(date1[1]), int(date1[0]), int(date2[0], int(date[1]), int(date[2])))
        d2 = int(date1[2] + date1[1] + date1[0])
        date = i[6].split()
        date1 = date[0].split('.')
        date2 = date[1].split(':')
        d1 = datetime(int(date1[2]), int(date1[1]), int(date1[0]), int(date2[0], int(date[1]), int(date[2])))"""

ACTUAL_NEWS = []
ACTUAL_ACT = []

async def command_news(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_news)
    await message.delete()

#29.04.2022 9:00:00
# Отправим актуальные новости в группу -618154662 -1001469485742 225923687
async def asck_news():
    global ACTUAL_NEWS
    global ACTUAL_ACT
    d1 = int(datetime.datetime.now().strftime("%Y%m%d"))
    d11 = int(datetime.datetime.now().strftime("%H%M%S"))
    for i in google.ACTUAL_NEWS:
        if len(i) == 0:
            continue
        date = i[5].split()
        date1 = date[0].split('.')
        date2 = date[1].split(':')
        d2 = int(date1[2] + date1[1] + date1[0])
        d21 = int(date2[0] + date2[1] + date2[2])
        date = i[6].split()
        date1 = date[0].split('.')
        date2 = date[1].split(':')
        d3 = int(date1[2] + date1[1] + date1[0])
        d31 = int(date2[0] + date2[1] + date2[2])
        if d1 >= d2 and d3 >= d1:
            if i in ACTUAL_NEWS or ACTUAL_ACT:
                continue
            elif d11 >= d21:
                if i[4] != '':
                    name_doc = google.save_files(i[4].split('=')[-1])
                    doc = open(name_doc, 'rb')
                    if name_doc.split('.')[-1] == 'jpg':
                        await bot.send_photo(-1001469485742, doc, i[3])
                    else:
                        await bot.send_message(-1001469485742, i[3])
                        await bot.send_document(-1001469485742, open(name_doc, 'rb'))
                else:
                    await bot.send_message(-1001469485742, i[3])
                if i[2] == 'Акция':
                    ACTUAL_ACT.append(i)
                else:
                    ACTUAL_NEWS.append(i)
        


@dp.message_handler(Text(equals='Вывод актуальных новостей'))
async def display_of_current_news(message: types.Message):
    global ACTUAL_NEWS
    d1 = int(datetime.datetime.now().strftime("%Y%m%d"))
    d11 = int(datetime.datetime.now().strftime("%H%M%S"))
    act = copy.copy(ACTUAL_NEWS)
    if len(ACTUAL_NEWS) != 0:
        for i in ACTUAL_NEWS:
            date = i[5].split()
            date1 = date[0].split('.')
            date2 = date[1].split(':')
            d2 = int(date1[2] + date1[1] + date1[0])
            d21 = int(date2[0] + date2[1] + date2[2])
            date = i[6].split()
            date1 = date[0].split('.')
            date2 = date[1].split(':')
            d3 = int(date1[2] + date1[1] + date1[0])
            d31 = int(date2[0] + date2[1] + date2[2])
            if d11 >= d21 and d31 >= d11:
                if i[4] != '':
                    name_doc = google.save_files(i[4].split('=')[-1])
                    doc = open(name_doc, 'rb')
                    if name_doc.split('.')[-1] == 'jpg':
                        await bot.send_photo(message.from_user.id, doc, i[3])
                    else:
                        await bot.send_message(message.from_user.id, i[3])
                        await bot.send_document(message.from_user.id, open(name_doc, 'rb'))
                else:
                    await bot.send_message(message.from_user.id, i[3])
            else:
                act.remove(i)
    else:
        await bot.send_message(message.from_user.id, "Нет актуальных новостей")
    ACTUAL_NEWS = act
    await message.delete()


@dp.message_handler(Text(equals='Акции'))
async def display_of_current_news(message: types.Message):
    global ACTUAL_ACT
    d1 = int(datetime.datetime.now().strftime("%Y%m%d"))
    d11 = int(datetime.datetime.now().strftime("%H%M%S"))
    act = copy.copy(ACTUAL_ACT)
    if len(ACTUAL_ACT) != 0:
        for i in ACTUAL_ACT:
            date = i[5].split()
            date1 = date[0].split('.')
            date2 = date[1].split(':')
            d2 = int(date1[2] + date1[1] + date1[0])
            d21 = int(date2[0] + date2[1] + date2[2])
            date = i[6].split()
            date1 = date[0].split('.')
            date2 = date[1].split(':')
            d3 = int(date1[2] + date1[1] + date1[0])
            d31 = int(date2[0] + date2[1] + date2[2])
            if d1 > d2:
                act.remove(i)
            elif d11 >= d21 and d31 >= d11:
                if i[4] != '':
                    name_doc = google.save_files(i[4].split('=')[-1])
                    doc = open(name_doc, 'rb')
                    if name_doc.split('.')[-1] == 'jpg':
                        await bot.send_photo(message.from_user.id, doc, i[3])
                    else:
                        await bot.send_message(message.from_user.id, i[3])
                        await bot.send_document(message.from_user.id, open(name_doc, 'rb'))
                else:
                    await bot.send_message(message.from_user.id, i[3])
    else:
        await bot.send_message(message.from_user.id, "Нет актуальных акций")
    ACTUAL_ACT = act
    await message.delete()


async def scheduler():
    try:
        aioschedule.every(5).seconds.do(asck_news)
        aioschedule.every(5).seconds.do(google.id_docks)
        aioschedule.every(5).seconds.do(google.get_news)
        aioschedule.every().hours.do(google.open_driveID)
        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(1)
    except:
        await asyncio.sleep(30)

