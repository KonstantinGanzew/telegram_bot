import requests
from bs4 import BeautifulSoup

TRUE = False
# ССылка на ресурсы
HOST = 'https://hh.ru'
URL = 'https://sterlitamak.hh.ru/search/vacancy?from=employerPage&employer_id=4135342&hhtmFrom=employer'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
           'accept': '*/*'}

# Узнаем статус страницы
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


# Получаем количество страниц
def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='bloko-button HH-Pager-Control')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


# Получаем содержание главной строницы, собираем резюме всех пользователей
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='vacancy-serp-item__layout')

    vacancy = []

    for item in items:
#        resurse = HOST + item.find( 'a', class_='resume-search-item__name').get('href')
        vacancy.append(item.find('a', class_='serp-item__title').get('href'))
    return vacancy


# Выбераем данные от пользователей
def get_resum(html):
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find('div', class_='resume-wrapper')
    vacancy = [{
#            'vacansy_name': item.find('span', class_='resume-block__title-text').get('span'),
            'link': html,
    }]
    return vacancy


# Метод парсера
def parse(true):
    if true:
        html = get_html(URL)
        if html.status_code == 200:
            vacancy = []
            vacancy.extend(get_content(html.text))
            return vacancy
        else:
            print('Error')
    TRUE = False
