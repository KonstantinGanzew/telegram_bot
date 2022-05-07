import re
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопки для главного меню
#main_key = ['Новости', 'Документы', 'Персонал', 'EBITDA', 'Прямая связь', 'О компании']
main_key = ['Новости', 'Документы', 'Персонал', 'О компании']
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
for item in main_key:
    kb_client.insert(KeyboardButton(item))


# Кнопки для новостей
news_key = ['Вывод актуальных новостей', 'Акции', 'Назад']
kb_news = ReplyKeyboardMarkup(resize_keyboard=True)
for item in news_key:
    kb_news.add(KeyboardButton(item))


# Кнопки для документов
docks_key = ['Образцы заявлений', 'Приказы', 'Регламенты', 'Положения', 'Уставные документы', 'Карты партнера', 'Фирменные бланки', 'Листы мотивации', 'Назад']
kb_docks = ReplyKeyboardMarkup(resize_keyboard=True)
for item in docks_key:
    kb_docks.insert(KeyboardButton(item))

# Кнопки для персонала
person_key = ['🔍 Сотрудники компании', '🈺 Вакансии компании', '📖 Бизнес-процессы', '📈 Развитие персонала', '📋 Калькулятор вознаграждения', '📝 Лист мотивации', 'Назад']
kb_person = ReplyKeyboardMarkup(resize_keyboard=True)
for item in person_key:
    kb_person.insert(KeyboardButton(item))


# Кнопки для о компании
company_key = ['Обращение директора', 'Оргструктура', 'История компании', 'Принципы и политики компании', 'Назад']
kb_company = ReplyKeyboardMarkup(resize_keyboard=True)
for item in company_key:
    kb_company.insert(KeyboardButton(item))

# Кнопки для прямой связи
direct_key = ['Передать проблему', 'Обращение к директору', 'Назад']
kb_direct = ReplyKeyboardMarkup(resize_keyboard=True)
for item in direct_key:
    kb_direct.add(item)

# Кнопки обращение к директору
dir_send_key = ['Персонализировано', 'Анонимно', 'Haзад']
kb_dir_send = ReplyKeyboardMarkup(resize_keyboard=True)
for item in dir_send_key:
    kb_dir_send.add(item)

kb_answer = ReplyKeyboardMarkup(resize_keyboard=True)
kb_answer.add('Назад')