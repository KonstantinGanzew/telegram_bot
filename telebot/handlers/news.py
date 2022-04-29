import time
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


# Отправим актуальные новости в группу -618154662
async def asck_news():
    global ACTUAL_NEWS
    for i in google.ACTUAL_NEWS:
        for j in i:
            if j in ACTUAL_NEWS:
                continue
            else:
                await bot.send_message(-618154662, j)
                ACTUAL_NEWS.append(j)



async def scheduler():
    aioschedule.every(3).seconds.do(asck_news)
    aioschedule.every(10).seconds.do(google.get_news)
    aioschedule.every().hours.do(google.open_driveID)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

