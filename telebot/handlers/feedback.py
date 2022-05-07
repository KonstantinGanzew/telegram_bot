from email import message
from aiogram.dispatcher.filters.state import StatesGroup, State

#Получаем сообщения от сотрудника
class var_name(StatesGroup):
    tema = State()
    mes = State()
    photo = State()