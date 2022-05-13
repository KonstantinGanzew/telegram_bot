from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot
from keyboards import kb_news

@dp.message_handler(Text(equals='EBITDA'))
async def command_ebitda(message: types.Message):
    await bot.send_message(message.from_user.id, 'Раздел в разработке')
    await message.delete()
