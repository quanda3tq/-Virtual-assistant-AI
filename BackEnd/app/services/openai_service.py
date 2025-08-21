from openai import OpenAI
from app.utils.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def ask_chatgpt(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
