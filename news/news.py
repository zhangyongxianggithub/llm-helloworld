from typing import List

from openai_base import client


def ask_chatgpt(messages):
    response = client.chat.completions.create(model="gpt-4", messages=messages)
    return response.choices[0].message.content


prompt_role = ('You are an assistant of journalists. '
               ' Your task is to write articles,'
               ' base on facts that are given you,'
               ' you should respect the instructions: the TONE, the LENGTH, the STYLE')


def assist_journalist(facts: List[str], tone: str, length_words: int, style: str):
    facts = ','.join(facts)
    prompt = f'{prompt_role} \
             FACTS: {facts} \
             TONE: {tone} \
             LENGTH: {length_words} words \
             STYLE: {style} '
    return ask_chatgpt([{"role": "user", "content": prompt}])


print(assist_journalist(["The sky is blue", "The grass is green"],
                        "informal", 100, "blogpost"))

print(assist_journalist(["A book on ChatGPT has been published last week",
                         "The title is developing Apps with GPT-4 and ChatGPT",
                         "the publisher is O'Reilly"],
                        "informal", 100, "blogpost"))
