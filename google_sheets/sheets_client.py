import gspread
from google.oauth2.service_account import Credentials
from config import GOOGLE_SPREADSHEET_ID, GOOGLE_SERVICE_ACCOUNT_FILE

def get_client():
    """Подключение к Google Sheets"""
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    credentials = Credentials.from_service_account_file(
        GOOGLE_SERVICE_ACCOUNT_FILE,
        scopes=scopes
    )
    
    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_key(GOOGLE_SPREADSHEET_ID)
    worksheet = spreadsheet.sheet1
    
    # Создаем заголовки если лист пустой
    if worksheet.row_values(1) == []:
        worksheet.append_row(["Дата записи", "Имя", "Телефон", "Услуга", "Дата и время визита"])
    
    return worksheet
