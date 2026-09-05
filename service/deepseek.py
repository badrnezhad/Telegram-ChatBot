import os
from openai import OpenAI

from config import HF_TOKEN

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)


async def ask_deepseek(user_id: int, message: str):
    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V4-Flash-0731:novita",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ],
    )

    return completion.choices[0].message.content
