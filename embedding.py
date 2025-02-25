from openai import OpenAI

from openai_base import client

response = client.embeddings.create(model="text-embedding-3-large", input='张永祥概念股')
print(response.to_json())
