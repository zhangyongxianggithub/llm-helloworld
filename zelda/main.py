from zelda.intent import IntentService
from zelda.rag import DataService
from zelda.response import ResponseService


def init(file: str):
    data_service = DataService()
    embeddings = data_service.pdf_to_embeddings(pdf_path=file)
    data_service.load_data_to_redis(embeddings=embeddings)


if __name__ == "__main__":
    # init(
    #     file="/Users/zyx/Documents/book-notes/Architecture/调用链技术分享.pdf",
    # )
    user_question = "最好的调用链技术是哪个，如果其中没有就抛开facts，那么请给出你觉得最好的技术方案"
    data_service = DataService()
    intent_service = IntentService()
    keyworlds = intent_service.get_intent(user_question=user_question)
    docs = data_service.search_redis(keyworlds)
    response_service = ResponseService()
    result = response_service.generate_response(
        facts=[doc["text"] for doc in docs], user_question=user_question
    )
    print(result)
