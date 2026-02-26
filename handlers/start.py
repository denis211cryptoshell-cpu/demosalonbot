from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.main_kb import get_main_keyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Добро пожаловать в салон красоты!\n"
        "Выберите действие в меню:",
        reply_markup=get_main_keyboard()
    )
