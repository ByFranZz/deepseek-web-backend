import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class DeepseekService:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")

    def chat(self, messages, model="deepseek-chat", stream=False):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            stream=stream
        )
        return response.choices[0].message.content