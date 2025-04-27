from redis import Redis
from pypdf import PdfReader
from openai_base import client


# 信息检索服务
class DataService:
    def __init__(self):
        self.redis_client = Redis(
            host="dev.bestzyx.com", port=6379, db=0, password="163766"
        )

    def pdf_to_embeddings(self, pdf_path: str, chunk_size: int = 1000):
        reader = PdfReader(pdf_path)
        chunks = []
        for page in reader.pages:
            text_page = page.extract_text()
            chunks.extend(
                [
                    text_page[i : i + chunk_size]
                    for i in range(0, len(text_page), chunk_size)
                ]
            )
        response = client.embeddings.create(
            model="text-embedding-3-large", input=chunks
        )
        return [
            {
                "id": value["index"],
                "vector": value["embedding"],
                "text": chunks[value["index"]],
            }
            for value in response.data
        ]

    def load_data_to_redis(self, embeddings):
        pass
