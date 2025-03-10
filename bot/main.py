import asyncio
from configs.config import settings
from loader import bot, dp
import logging
from loguru import logger

from handlers.start import start_router


class InterceptHandler(logging.Handler):
    def emit(self, record):
        level = logger.level(record.levelname).name
        logger.log(level, record.getMessage())

logging.getLogger('aiogram').setLevel(logging.DEBUG)
logging.getLogger('aiogram').addHandler(InterceptHandler())
logging.getLogger('asyncio').setLevel(logging.DEBUG)
logging.getLogger('asyncio').addHandler(InterceptHandler())


async def main():
    logger.info(f"Starting the bot using api_key: {settings.bot_api_key}")

    await bot.delete_webhook(drop_pending_updates=True)

    dp.include_router(start_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())