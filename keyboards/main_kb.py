from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_keyboard() -> ReplyKeyboardMarkup:
    """Главное меню бота"""
    kb = [
        [KeyboardButton(text="✂️ Записаться")],
        [KeyboardButton(text="📋 Мои записи"), KeyboardButton(text="❌ Отменить запись")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def get_services_keyboard() -> InlineKeyboardMarkup:
    """Выбор услуги"""
    services = [
        ["Стрижка", "service_strizhka"],
        ["Окрашивание", "service_okrashivanie"],
        ["Маникюр", "service_manikur"],
        ["Педикюр", "service_pedikur"]
    ]
    buttons = [
        [InlineKeyboardButton(text=name, callback_data=cb)]
        for name, cb in services
    ]
    buttons.append([InlineKeyboardButton(text="← Назад", callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_cancel_keyboard() -> InlineKeyboardMarkup:
    """Кнопка отмены"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")]
    ])
