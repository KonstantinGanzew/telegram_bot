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
             'ТАСКО-МОТОРС': ['11QKQA4u6ZWVKuAX0GOlFEGifgDTxsM-P' '1sMQ2tm599P1ecFwN736G0Xa3wNPArH2S', '18uTcupE90lY-Ni3WnJXMikG7B1e9unLu'],
             'ТАСКО-трейд': ['1Un7zNPRHmxP1rP949MT_bKTOxZvUgNnD', '1dyG19CFPXGyGqYiZdC1UfN6adKR399sj', '17TxJZ6SudqijH32ktnmnDvPHXFd6uG2k']}

ID_TEL = []
EMPLOYEES = []
ACTUAL_NEWS = []

CREDENTIALS_FILE = 'C:\\Users\\gantcev_k2312\\Desktop\\Тест\\telegram_bot\\telebot\\googleDisk\\creeds.json'
#CREDENTIALS_FILE = 'D:\\project\\telegabot\\telebot\\googleDisk\\creeds.json'

# Получаем сотрудников
def open_driveID():
    global ID_TEL
    global EMPLOYEES
    ID_TEL = []
    EMPLOYEES = []
    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = '19Ez9Endd_Qcg7QqRoZdrfKspxyatb17Lbo9O1dZ30QY'

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
        range="A1:J19",
        majorDimension='ROWS'
    ).execute()
    spreadsheet = service.spreadsheets().create(body = {
    'properties': {'title': 'Бюджет 2022 г.', 'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 378550121,
                               'title': 'Dashboard',
                               'gridProperties': {'rowCount': 1, 'columnCount': 16}}}]
    }).execute()

    print(values)
    print(spreadsheet)
    

open_driveID()