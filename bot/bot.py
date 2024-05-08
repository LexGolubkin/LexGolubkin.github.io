import asyncio
import handlers
import os

from aiogram import Bot, Dispatcher

from configs.base import TOKEN, LOGGING_PATH
# from data.db import DatabaseManager
from loguru import logger


WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.environ.get("PORT", 5000))


bot = Bot(TOKEN)
dp = Dispatcher()
# db = DatabaseManager()


async def on_startup():
    dp.include_routers(handlers.shop)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logger.add(LOGGING_PATH)
    asyncio.run(on_startup())
