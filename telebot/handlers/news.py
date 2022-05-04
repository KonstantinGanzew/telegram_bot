import datetime
import aioschedule
import logging
import asyncio
from googleDisk import google
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_news
from googleDisk import google


ACTUAL_NEWS = []

async def command_news(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_news)
    await message.delete()

#29.04.2022 9:00:00
# Отправим актуальные новости в группу -618154662
async def asck_news():
    global ACTUAL_NEWS
    d1 = int(datetime.datetime.now().strftime("%Y%m%d"))
    for i in google.ACTUAL_NEWS:
        date = i[5].split()
        date1 = date[0].split('.')
        date2 = date[1].split(':')
        d2 = int(date1[2] + date1[1] + date1[0])
        date = i[6].split()
        date1 = date[0].split('.')
        date2 = date[1].split(':')
        d3 = int(date1[2] + date1[1] + date1[0])
        if d1 >= d2 and d3 >= d1:
            if i in ACTUAL_NEWS:
                continue
            else:
                name_doc = google.saveFile('1GilYTUv3Bupck8vuIxLDJdaPfL2H23W0RZPtGXv_oXxRKQcHiH0P3gbupeL8l1O-Sak2KjGV', i[4].split('=')[-1])
                await bot.send_file(225923687, open(name_doc, 'rb'))
                ACTUAL_NEWS.append(i)



async def scheduler():
    aioschedule.every(3).seconds.do(asck_news)
    aioschedule.every(10).seconds.do(google.get_news)
    aioschedule.every().hours.do(google.open_driveID)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

