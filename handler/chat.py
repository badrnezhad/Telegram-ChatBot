from aiogram import F
from aiogram.types import Message

from config import dp
from service.deepseek import ask_deepseek
from service.openai import ask_chatgpt


@dp.message(F.text)
async def chat_handler(message: Message):
    answer = await ask_chatgpt(message.from_user.id, message.text)
    await message.answer(answer)
