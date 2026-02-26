from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from datetime import datetime
from states.booking_states import BookingStates
from keyboards.main_kb import get_services_keyboard, get_cancel_keyboard
from google_sheets.operations import add_booking

router = Router()

@router.message(F.text == "✂️ Записаться")
async def start_booking(message: Message, state: FSMContext):
    await state.set_state(BookingStates.selecting_service)
    await message.answer(
        "Выберите услугу:",
        reply_markup=get_services_keyboard()
    )

@router.callback_query(F.data.startswith("service_"))
async def service_selected(callback: CallbackQuery, state: FSMContext):
    service = callback.data.replace("service_", "")
    await state.update_data(service=service)
    await state.set_state(BookingStates.entering_name)
    await callback.message.answer("Введите ваше имя:")

@router.message(BookingStates.entering_name)
async def name_entered(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookingStates.entering_phone)
    await message.answer("Введите ваш номер телефона:")

@router.message(BookingStates.entering_phone)
async def phone_entered(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(BookingStates.selecting_datetime)
    await message.answer(
        "Введите желаемую дату и время (например: 25.02.2026 14:00):",
        reply_markup=get_cancel_keyboard()
    )

@router.message(BookingStates.selecting_datetime)
async def datetime_entered(message: Message, state: FSMContext):
    data = await state.get_data()
    
    # Сохранение в Google Sheets
    booking_data = {
        "created_at": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "name": data['name'],
        "phone": data['phone'],
        "service": data['service'],
        "datetime": message.text
    }
    add_booking(booking_data)
    
    await message.answer(
        f"✅ Вы записаны!\n\n"
        f"Услуга: {data['service']}\n"
        f"Имя: {data['name']}\n"
        f"Телефон: {data['phone']}\n"
        f"Дата: {message.text}"
    )
    await state.clear()

@router.callback_query(F.data == "back_main")
async def back_to_main(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("Главное меню:")
