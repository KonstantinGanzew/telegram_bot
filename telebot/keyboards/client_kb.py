import re
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопки для главного меню
main_key = ['Новости', 'Документы', 'Персонал', 'EBITDA', 'Прямая связь', 'О компании']
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
for item in main_key:
    kb_client.insert(KeyboardButton(item))


# Кнопки для новостей
news_key = ['Вывод актуальных новостей', 'Акции', 'Назад']
kb_news = ReplyKeyboardMarkup(resize_keyboard=True)
for item in news_key:
    kb_news.add(KeyboardButton(item))


# Кнопки для документов
docks_key = ['Образцы заявлений', 
             'Приказы', 
             'Положения', 
             'Уставные документы', 
             'Карты партнера', 
             'Фирменные бланки', 
             'Назад']
kb_docks = ReplyKeyboardMarkup(resize_keyboard=True)
for item in docks_key:
    kb_docks.insert(KeyboardButton(item))

# Кнопки для положений
provisions_key = ['О коммерческой тайне',
                  'O компании',
                  'О персональных данных',
                  'Об оплате труда работников',
                  'О пропускном режиме',
                  'ПВТР',
                  'Hазaд']
kb_provisions_key = ReplyKeyboardMarkup(resize_keyboard=True)
for item in provisions_key:
    kb_provisions_key.insert(KeyboardButton(item))

# Кнопки карт партнера
partner_cards_key = ['ТАСКО-МОТОРС',
                 'ТАСКО-трейд',
                 'Автотрейд',
                 'СК Моторс',
                 'Сервис Плюс',
                 'ИП Терехов',
                 'ИП Васильев',
                 'Орентранс',
                 'Hазaд']
kb_partner_cards = ReplyKeyboardMarkup(resize_keyboard=True)
for item in partner_cards_key:
    kb_partner_cards.insert(KeyboardButton(item))

# Кнопки для фирменных бланков
letterhead_key = ['ТАСКО-МОТОРC',
                 'ТАСКO-трейд',
                 'Aвтотрейд',
                 'CК Моторс',
                 'Cервис Плюс',
                 'ИП Tерехов',
                 'ИП Bасильев',
                 'Hазaд']
kb_letterhead = ReplyKeyboardMarkup(resize_keyboard=True)
for item in letterhead_key:
    kb_letterhead.insert(item)

# Кнопки для персонала
person_key = ['🔍 Сотрудники компании', 
              '🈺 Вакансии компании', 
              '📖 Бизнес-процессы', 
              '📈 Развитие персонала', 
              '📋 Калькулятор вознаграждения', 
              '📝 Лист мотивации', 
              'Назад']
kb_person = ReplyKeyboardMarkup(resize_keyboard=True)
for item in person_key:
    kb_person.insert(KeyboardButton(item))


# Кнопки для о компании
company_key = ['Оргструктура', 
               'История компании', 
               'Принципы и политики компании', 
               'Назад']
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

# Кнопки для Образцыов заявлений
sample_key = ['Выход из отпуска, уход за ребёнком',
              'Обходной лист, увольнение',
              'Отгул',
              'Отпуск, без содержания',
              'Отпуск, ежегодный',
              'Отпуск, беременность',
              'Перевод, 0,5 ставки',
              'Перевод, временно',
              'Перевод, другая должность',
              'Перечень, документы',
              'Прием',
              'Прием, совмещение',
              'Увольнение',
              'Hазaд']
kb_sample = ReplyKeyboardMarkup(resize_keyboard=True)
for item in sample_key:
    kb_sample.insert(item)

# Кнопки для уставных документов
statutory_documents_key = ['ТAСКО-МОТОРС',
                           'ТAСКО-трейд',
                           'Автoтрейд',
                           'СK Моторс',
                           'Сeрвис Плюс',
                           'Hазaд']
kb_statory_documents = ReplyKeyboardMarkup(resize_keyboard=True)
for item in statutory_documents_key:
    kb_statory_documents.insert(item)
