import datetime
import aioschedule
import logging
import asyncio
from googleDisk import google
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_news
from googleDisk import google


ACTUAL_NEWS = []

async def command_news(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_news)
    await message.delete()

#29.04.2022 9:00:00
# Отправим актуальные новости в группу -618154662 -1001469485742 225923687
async def asck_news():
    global ACTUAL_NEWS
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
            if i in ACTUAL_NEWS:
                continue
            elif d11 >= d21:
                name_doc = google.save_file(i[4].split('=')[-1])
                doc = open(name_doc, 'rb')
                if name_doc.split('.')[-1] == 'jpg':
                    await bot.send_photo(-1001469485742, doc, i[3])
                    ACTUAL_NEWS.append(i)
                else:
                    await bot.send_message(-1001469485742, i[3])
                    await bot.send_document(-1001469485742, open(name_doc, 'rb'))
                    ACTUAL_NEWS.append(i)
                print('Новость опубликована')
        


@dp.message_handler(Text(equals='Вывод актуальных новостей'))
async def display_of_current_news(message: types.Message):
    global ACTUAL_NEWS
    d1 = int(datetime.datetime.now().strftime("%Y%m%d"))
    d11 = int(datetime.datetime.now().strftime("%H%M%S"))
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
            if d1 > d2:
                ACTUAL_NEWS.remove(i)
            elif d11 >= d21 and d31 >= d11:
                name_doc = google.save_file(i[4].split('=')[-1])
                doc = open(name_doc, 'rb')
                if name_doc.split('.')[-1] == 'jpg':
                    await bot.send_photo(message.from_user.id, doc, i[3])
                else:
                    await bot.send_message(message.from_user.id, i[3])
                    await bot.send_document(message.from_user.id, open(name_doc, 'rb'))
            else:
                ACTUAL_NEWS.remove(i)
    else:
        await bot.send_message(message.from_user.id, "Нет актуальных новостей")




async def scheduler():
    #aioschedule.every().seconds.at(f"{message.text}")
    aioschedule.every(3).seconds.do(asck_news)
    aioschedule.every(3).seconds.do(google.id_docks)
    aioschedule.every(3).seconds.do(google.get_news)
    aioschedule.every().hours.do(google.open_driveID)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

