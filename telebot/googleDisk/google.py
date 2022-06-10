import os
import logging
import asyncio
import io
from webbrowser import get
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from googleapiclient.discovery import build

#  название организации     Образцы заявлений                    положения                            приказы
ID_FOLDER = {'Автотрейд': ['1w0bXnZDHgYrM5hawUkH5CvmOoAPnedV7', '19zigzNaeTNWKe1BmL8oTJi7aReDhifNr', '1kdrDGDtbxLU0g38hbjWIWwbpZRbdwYzk'], 
             'ИП Васильев': ['1huMRi6BgY1VU8Ts55KIRbpmQ13ui58LM', '', '1bd2LgRH0l3eh9kNYSBCBYenbUDLQMiN_'], # Нету в положении
             'ИП Терехов': ['1Y-bj95Ch1K-dDjkDOtOK2uhD0Nf2QqjC', '1rTd_NMU1uK9cvBZ9cGBik6vuLwVhpR0k', '1y11HuGaDHUGKFPCfXz5ewdqzt3UhCSCg'],
             'Сервис Плюс': ['1vlM7nS5zVEtfmF8hpVXiULgDn3OtsIH_', '', '1lyDUNCsxKlMtu0xmla-7yum5uzJvQDlJ'], # Нету в положении
             'СК Моторс': ['1Upch3gks8dCc5ZZKQ9dsPEO1a-6_1iNc', '1wJFoKmu1AvNAtCQxV5SCLXAiiHopWYX3', '1P8xmwwfXYtyl-5GFqVjh42ASNnDJTk5i'],
             'ТАСКО-МОТОРС': ['11QKQA4u6ZWVKuAX0GOlFEGifgDTxsM-P', '1sMQ2tm599P1ecFwN736G0Xa3wNPArH2S', '18uTcupE90lY-Ni3WnJXMikG7B1e9unLu'],
             'ТАСКО-трейд': ['1Un7zNPRHmxP1rP949MT_bKTOxZvUgNnD', '1dyG19CFPXGyGqYiZdC1UfN6adKR399sj', '17TxJZ6SudqijH32ktnmnDvPHXFd6uG2k']}

ID_DOCKS = dict()
ID_ORDERS = []

ID_TEL = []
EMPLOYEES = []
ACTUAL_NEWS = []
SEARCH_PERSON = []

CREDENTIALS_FILE = '/bot/googleDisk/creeds.json'
#CREDENTIALS_FILE = 'C:\\Users\\gantcev_k2312\\Desktop\\Тест\\telegram_bot\\telebot\\googleDisk\\creeds.json'
#CREDENTIALS_FILE = 'D:\\project\\telegabot\\telebot\\googleDisk\\creeds.json'

# Получаем сотрудников
async def open_driveID():
    global ID_TEL
    global EMPLOYEES
    global SEARCH_PERSON
    ID_TEL = []
    EMPLOYEES = []
    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = '1TLIT1BHPWw-00tF8PNHdyny1FJp5OAQB2ukXiUmyY-0'

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

    # Читаем файл и заполняем кортеж идшниками
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:K1000',
        majorDimension='ROWS'
    ).execute()
    val = values.pop('values')
    for item in val:
        EMPLOYEES.append(item)
        SEARCH_PERSON.append([item[0], item[1], item[7], item[9]])
        if item[5] != '':
            ID_TEL.append(int(item[5].replace(' ', '')))


async def get_news():
    global ACTUAL_NEWS
    ACTUAL_NEWS = []
    # ID Google Sheets документа
    spreadsheet_id = '1IHR2-KftLdq1swsr0G3Nqb9VpWGypdlrF7AgG1jd3bc'

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

    # Читаем файл и заполняем кортеж идшниками
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A3:G1000',
        majorDimension='ROWS'
    ).execute()
    val = values.pop('values')
    for item in val:
        ACTUAL_NEWS.append(item)

async def id_docks():
    global ID_DOCKS
    global ID_ORDERS
    ID_DOCKS = dict()
    ID_ORDERS = []
    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = '1xnd2KtknGSb8s7oc7dYvaMpad_liFR54x5MhwgT3DYU'

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

    # Читаем файл и заполняем кортеж идшниками
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B2:G1000',
        majorDimension='ROWS'
    ).execute()
    val = values.pop('values')
    for item in val:
        if item[0] != 'Приказы':
            try:
                ID_DOCKS[item[5]][item[4]] = item[3].split('=')[-1]
            except Exception:
                ID_DOCKS.update({item[5]: {item[4]: item[3].split('=')[-1]}})
        else:
            ID_ORDERS.append([item[4], item[5], item[3].split('=')[-1]])


# Заносим пожелание на диск не использоваемый функционал
def down_drive(first_name, username, text):
    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = '1gqmdEgkMGGo6XHB4l0akIUkQN7ExZJGHh797fGS6l0E'

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

    list = [[first_name], [username], [text]]

    resource = {
        "majorDimension": "COLUMNS",
        "values": list
    }
    range = "Sheet1!A:C"
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range,
        body=resource,
        valueInputOption="USER_ENTERED"
    ).execute()

def save_file(parend_id, file_id):
    SCOPES = ['https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)
    results = service.files().list(
        pageSize=1000, 
        fields="files(id, name, mimeType, parents, createdTime)",
        q=f"'{parend_id}' in parents").execute()
    file_name = ''
    for i in results['files']:
        if i['id'] == file_id:
            file_name = i['name'].lower()
            break
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False
    while not done:
        done = downloader.next_chunk()
        fh.seek(0)

        with open(os.path.join(file_name), 'wb') as f:
            f.write(fh.read())
            f.close()
    return file_name

def save_files(file_id):
    SCOPES = ['https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)
    results = service.files().list(
        pageSize=1000, 
        fields="files(id, name, mimeType, parents, createdTime)",
        ).execute()
    file_name = ''
    for i in results['files']:
        if i['id'] == file_id:
            file_name = i['name'].lower()
            break
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False
    while not done:
        done = downloader.next_chunk()
        fh.seek(0)

        with open(os.path.join(file_name), 'wb') as f:
            f.write(fh.read())
            f.close()
    return file_name

# Скачиваем файл с диска
def search_file(name_org, number_folder):
    SCOPES = ['https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)
    id_fl = ID_FOLDER.get(name_org)[number_folder]
    results = service.files().list(pageSize=20, fields="files(id, name, mimeType, parents, createdTime)", q=f"'{id_fl}' in parents").execute()
    name_file = []
    for i in results.pop('files'):
        id = i.pop('id') 
        name_file.append(save_file(id_fl, id))
    return name_file

# Скачиваем файл с диска
def search_filename(name_org, name_fil):
    return save_files(ID_DOCKS[name_org][name_fil])

