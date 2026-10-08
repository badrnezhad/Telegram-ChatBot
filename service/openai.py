from openai import AsyncOpenAI

from config import OPENAI_API_KEY

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

hisotries = {}


async def ask_chatgpt(user_id: int, message: str):
    if user_id not in hisotries:
        hisotries[user_id] = []

    history = hisotries[user_id]
    user_turn = {
        "role": "user",
        "content": message
    }

    response = await client.responses.create(
        model="gpt-5.6",
        input=[*history[-4:], user_turn]
    )

    answer = response.output_text

    history.append(user_turn)
    history.append({
        "role": "assistant",
        "content": answer
    })

    history[:] = history[-6:]

    return answer
