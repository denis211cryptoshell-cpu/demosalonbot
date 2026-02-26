from .sheets_client import get_client

def add_booking(booking_data: dict):
    """Добавление записи в Google Sheets"""
    worksheet = get_client()
    
    row = [
        booking_data.get("created_at", ""),
        booking_data.get("name", ""),
        booking_data.get("phone", ""),
        booking_data.get("service", ""),
        booking_data.get("datetime", "")
    ]
    
    worksheet.append_row(row)
    return True

def get_bookings():
    """Получение всех записей"""
    worksheet = get_client()
    return worksheet.get_all_records()
