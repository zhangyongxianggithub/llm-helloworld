from openai_base import client


def ask_chatgpt(messages):
    response = client.chat.completions.create(model="gpt-4", messages=messages)
    return response.choices[0].message.content


with open("transcript.txt", "r") as f:
    content = f.read()
    print(content)

with open("transcript.txt", "r") as f:
    transcript = f.read()
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Summerize the following text"},
        {"role": "assistant", "content": "Yes"},
        {"role": "user", "content": transcript},
    ]
    print(ask_chatgpt(messages))
