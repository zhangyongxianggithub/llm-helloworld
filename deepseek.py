from ds_base import client

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Hello World!",
        }
    ],
    model="deepseek-chat",
)
print(chat_completion.to_json())
