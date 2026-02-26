import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, booking, cancel

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Регистрация роутеров
    dp.include_router(start.router)
    dp.include_router(booking.router)
    dp.include_router(cancel.router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
