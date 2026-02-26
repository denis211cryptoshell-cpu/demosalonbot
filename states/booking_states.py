from aiogram.fsm.state import State, StatesGroup

class BookingStates(StatesGroup):
    selecting_service = State()   # Выбор услуги
    entering_name = State()       # Ввод имени
    entering_phone = State()      # Ввод телефона
    selecting_datetime = State()  # Выбор даты и времени
