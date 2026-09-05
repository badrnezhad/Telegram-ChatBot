from openai import AsyncOpenAI

from config import OPENAI_API_KEY

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

hisotries = {}


async def ask_chatgpt(user_id: int, message: str):
    if user_id not in hisotries:
        hisotries[user_id] = []

    history = hisotries[user_id]
    history.append({
        "role": "user",
        "content": message
    })

    history[:] = history[-5:]

    response = await client.responses.create(
        model="gpt-5.6",
        input=history
    )

    answer = response.output_text

    history.append({
        "role": "assistant",
        "content": answer
    })

    history[:] = history[-5:]

    return answer
