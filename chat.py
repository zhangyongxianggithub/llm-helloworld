from openai_base import client as openai_client
from ds_base import client as ds_client


def chat_completion(prompt, model="gpt-4", temperature=0):
    res = openai_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
        temperature=temperature,
    )
    print(res.choices[0].message.content)


def chat_completion_ds(prompt, model="deepseek-chat", temperature=0):
    res = ds_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
        temperature=temperature,
    )
    print(res.choices[0].message.content)


if __name__ == "__main__":
    # chat_completion("As Descartes said, I think therefore")
    chat_completion("How much is 3695*123548?Let's thing step by step")
    chat_completion_ds("How much is 3695*123548")
