from aiogram.filters import CommandStart
from aiogram.types import Message

from config import dp


@dp.message(CommandStart())
async def start_handler(message: Message):
    print(f"message recieved : {message.text} ({message.from_user.first_name})")
    await message.answer(
        f"{message.from_user.first_name} سلام.\nبه چت بات پشتیبانی هولوسن خوش آمدید."
        "\n\nشروع کن به گفتگو:"
    )
