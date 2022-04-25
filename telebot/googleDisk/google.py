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

CREDENTIALS_FILE = 'D:\\project\\telegabot\\telebot\\googleDisk\\creeds.json'

LIST_EMPLOYES = []

# Получаем ид сотрудников
def open_driveID():
    if not ID_TEL: 
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
            range='F1:F1000',
            majorDimension='ROWS'
        ).execute()
        val = values.pop('values')
        for item in val:
            for i in item:
                ID_TEL.append(int(i.replace(' ', '')))

    return ID_TEL



# Заносим пожелание на диск
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


# Собираем список сотрудников
def open_list_employees(name_key):
    global LIST_EMPLOYES
    if not LIST_EMPLOYES:
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

        LIST_EMPLOYES = values.pop('values')

    values = []
    for item in LIST_EMPLOYES:
        s = ''
        for i in item:
            s  += i.strip().lower() + ' '
        if s.find(name_key.lower()) != -1:
            values.append(item)
        s = ''

    return values
