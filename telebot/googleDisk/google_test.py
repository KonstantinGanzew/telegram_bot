import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

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

# Заносим пожудание на диск
def down_drive():
    CREDENTIALS_FILE = 'C:\\Users\\gantcev_k2312\\telegabot\\telebot\\creeds.json'
    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = '1gqmdEgkMGGo6XHB4l0akIUkQN7ExZJGHh797fGS6l0E'

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
    values = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": "B3:C4",
                 "majorDimension": "ROWS",
                 "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]},
                {"range": "D5:E6",
                "majorDimension": "COLUMNS",
                 "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
	        ]
        }
    ).execute()

print(open_driveID())