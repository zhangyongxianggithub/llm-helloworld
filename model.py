from openai_base import client

print(client.models.list().to_json())
