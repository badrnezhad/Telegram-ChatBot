import asyncio

from aiogram import Bot

import handler.router
from config import BOT_TOKEN, dp


async def main():
    print("bot started")

    bot = Bot(token=BOT_TOKEN)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

