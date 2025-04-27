import json

from openai import OpenAI

from openai_base import client


# 假设一个产品库，定义一个搜索数据库的函数
def find_product(sql_query: str):
    results = [
        {"name": "pen", "price": 1, "color": "red"},
        {"name": "pen", "price": 1, "color": "red"},
    ]
    return results


functions = [
    {
        "name": "find_product",
        "description": "get a list of products from a sql query",
        "parameters": {
            "type": "object",
            "properties": {
                "sql_query": {
                    "type": "string",
                    "description": "a sql query",
                }
            },
            "required": ["sql_query"],
        },
    }
]
question = "I need the top 2 products where the price is lower than 50"
messages = [{"role": "user", "content": question}]
response = client.chat.completions.create(
    messages=messages, functions=functions, model="gpt-4o-mini"
)
print(response.to_json())
function_args = json.loads(response.choices[0].message.function_call.arguments)
messages.append(json.loads(response.choices[0].message.to_json()))
products = find_product(function_args["sql_query"])
messages.append(
    {
        "role": "function",
        "content": json.dumps(products),
        "name": "find_product",
    }
)
response1 = client.chat.completions.create(messages=messages, model="gpt-4o-mini")
print(response1.to_json())
