from openai_base import client


class IntentService:
    def __init__(self):
        pass

    def get_intent(self, user_question: str):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": f"Extract the keyworlds from the following question: {user_question}",
                }
            ],
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    intent = IntentService()
    print(
        intent.get_intent("CDP客户数据平台是什么?具有哪些功能?应该如何开发一个CDP服务?")
    )
