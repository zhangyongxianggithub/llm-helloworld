import os

from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains import ConversationChain

load_dotenv()
chatbot_llm = OpenAI(
    base_url="https://api.openai-proxy.org/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-3.5-turbo-instruct",
)
chatbot = ConversationChain(llm=chatbot_llm, verbose=True)
result = chatbot.predict(input="Hello")
print(result)
result = chatbot.predict(input="What is your name?")
print(result)
