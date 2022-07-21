from email import message
from aiogram.dispatcher.filters.state import StatesGroup, State

#Получаем сообщения от сотрудника
class tags(StatesGroup):
    tag = State()