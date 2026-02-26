from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

router = Router()

@router.callback_query(F.data == "cancel")
async def cancel_booking(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("❌ Запись отменена.\nВыберите действие в главном меню.")

@router.message(Command("cancel"))
async def cancel_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("❌ Действие отменено.")
