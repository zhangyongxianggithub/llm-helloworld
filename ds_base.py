import os

from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI

client = OpenAI(
    base_url='https://api.deepseek.com/v1',
    api_key=os.getenv('DEEPSEEK_API_KEY'),
)
