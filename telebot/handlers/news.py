import time
import aioschedule
import logging
import asyncio
from googleDisk import google
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_news


ACTUAL_NEWS = []

async def command_news(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите пункт', reply_markup=kb_news)
    await message.delete()


# Отправим актуальные новости в группу -618154662
async def asck_news(message):
    sum = list(set(ACTUAL_NEWS + google.list_news()))
    print(sum)
    if sum != 0:
        for item in sum:
            await bot.send_message("225923687", item)
    ACTUAL_NEWS = google.list_news()
    print('test')



async def scheduler():
    aioschedule.every(10).seconds.do(asck_news)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

