import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# Собираем ID сотрудников
def open_driveID():
    CREDENTIALS_FILE = 'D:\\project\\telegabot\\telebot\\googleDisk\\creeds.json'
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
    values = []
    for item in val:
        for i in item:
            values.append(int(i.replace(' ', '')))

    return values


# Собираем список сотрудников
def open_list_employees(name_key):
    CREDENTIALS_FILE = 'D:\\project\\telegabot\\telebot\\googleDisk\\creeds.json'
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
        range='A1:J137',
        majorDimension='ROWS'
    ).execute()

    val = values.pop('values')
    for item in val:
        for i in item:
            if i == name_key:
                return item

    return values


print(*open_list_employees('Бурдаев'))

# Заносим пожудание на диск
def down_drive(first_name, username, text):
    CREDENTIALS_FILE = 'D:\\project\\telegabot\\telebot\\googleDisk\\creeds.json'
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
