import sys

from openai_base import client

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Hello World!",
        }
    ],
    model="gpt-3.5-turbo",
)
print(chat_completion.to_json())

print(sys.path)
