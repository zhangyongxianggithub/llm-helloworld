import numpy as np
from redis import Redis
from pypdf import PdfReader
from redis.commands.search.query import Query

from openai_base import client

PREFIX = "rag"
INDEX_NAME = "documents"


# 信息检索服务
class DataService:
    def __init__(self):
        """
        构造函数
        """
        self.redis_client = Redis(host="localhost", port=6379, db=0, password="163766")

    def pdf_to_embeddings(self, pdf_path: str, chunk_size: int = 1000):
        """
        从pdf中读取数据并将其拆分为块
        """
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
                "id": embedding.index,
                "vector": embedding.embedding,
                "text": chunks[embedding.index],
            }
            for embedding in response.data
        ]

    def load_data_to_redis(self, embeddings):
        """
        写入向量数据到redis
        """
        for embedding in embeddings:
            key = f'{PREFIX}:{str(embedding["id"])}'
            embedding["vector"] = np.array(
                embedding["vector"], dtype=np.float32
            ).tobytes()
            self.redis_client.hset(key, mapping=embedding)

    def search_redis(self, user_query: str):
        """
        根据用户的输入来创建一个嵌入向量，并来查询redis
        """
        embedding = (
            client.embeddings.create(model="text-embedding-3-large", input=user_query)
            .data[0]
            .embedding
        )
        embedding_bytes = np.array(embedding, dtype=np.float32).tobytes()
        query = (
            Query(f"*=>[KNN 3 @vector $vec AS score]")
            .sort_by("score", asc=False)
            .return_fields("id", "text", "score")
            .dialect(4)
        )
        results = self.redis_client.ft(index_name=INDEX_NAME).search(
            query=query, query_params={"vec": embedding_bytes}
        )
        return [
            {"id": doc["id"], "text": doc["text"], "score": doc["score"]}
            for doc in results.docs
        ]


if __name__ == "__main__":
    service = DataService()
    # embeddings = service.pdf_to_embeddings(
    #     pdf_path="/Users/zyx/Documents/jetbra/README.pdf"
    # )
    # service.load_data_to_redis(embeddings)
    results = service.search_redis(user_query="WARNING")
    print(results)
