from openai_base import client
from zelda.intent import IntentService


class ResponseService:
    def __init__(self):
        pass

    def generate_response(self, facts, user_question: str):
        print(f"facts: {facts}")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": f"based on the facts, answer the question. facts: {facts}. question: {user_question}",
                }
            ],
        )
        return response.choices[0].message.content
