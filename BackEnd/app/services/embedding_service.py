from openai import OpenAI
from app.utils.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def get_embedding(text: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",  # hoặc 3-large
        input=text
    )
    return response.data[0].embedding
