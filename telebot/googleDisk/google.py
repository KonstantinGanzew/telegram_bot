import time
import schedule
import logging
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build


ID_FOLDER = {'Автотрейд': '1w0bXnZDHgYrM5hawUkH5CvmOoAPnedV7',
             'ИП Васильев': '1huMRi6BgY1VU8Ts55KIRbpmQ13ui58LM',
             'ИП Терехов': '1Y-bj95Ch1K-dDjkDOtOK2uhD0Nf2QqjC',
             'Сервис Плюс':'1vlM7nS5zVEtfmF8hpVXiULgDn3OtsIH_',
             'СК Моторс': '1Upch3gks8dCc5ZZKQ9dsPEO1a-6_1iNc',
             'ТАСКО-МОТОРС': '11QKQA4u6ZWVKuAX0GOlFEGifgDTxsM-P',
             'ТАСКО-трейд': '1Un7zNPRHmxP1rP949MT_bKTOxZvUgNnD'}

ID_TEL = []
EMPLOYEES = []
ACTUAL_NEWS = []

CREDENTIALS_FILE = 'D:\\project\\telegabot\\telebot\\googleDisk\\creeds.json'

# Возвращаем значение идшек
def id_telegram():
    return ID_TEL

# Возвращаем список сотруднитков
def list_employees():
    return EMPLOYEES

# Возвращаем список всех новостей
def list_news():
    return ACTUAL_NEWS

# Получаем сотрудников
def open_driveID():
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
        ID_TEL.append(item[5].replace(' ', ''))
        EMPLOYEES.append(item)

def get_news():
    ACTUAL_NEWS = []
    # ID Google Sheets документа
    spreadsheet_id = '1gqmdEgkMGGo6XHB4l0akIUkQN7ExZJGHh797fGS6l0E'

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
        range='A11:G1000',
        majorDimension='ROWS'
    ).execute()
    val = values.pop('values')
    for item in val:
        ACTUAL_NEWS.append(item)


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


# Скачиваем файл с диска
def search_file(name_org, search_file):
    SCOPES = ['https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)
    results = service.files().list(
                                    pageSize=20, 
                                    fields="files(id, name, mimeType, parents, createdTime)",
                                    q=f"'{ID_FOLDER.get(name_org)}' in parents and fullText contains '{search_file}'").execute()
    print(results.pop('files')[0].pop('id'))

# Запускаем шедуле
if __name__ == '__main__':
    schedule.every(10).seconds.do(get_news)
    schedule.every().hours.do(open_driveID)
    while True:
        try:
            schedule.run_pending()
        except Exception as e:
            logging.exception("Не удалось получить данные с гугла")
            pass
        time.sleep(1)
