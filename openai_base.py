import os

from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI

client = OpenAI(
    base_url='https://api.openai-proxy.org/v1',
    api_key=os.getenv('OPENAI_API_KEY'),
)
