from openai_base import client

response = client.moderations.create(model="text-moderation-latest", input='I want to kill my neighbor')
print(response.to_json())
