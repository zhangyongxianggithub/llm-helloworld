import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

template = """Question: {question}
            think step by step
            Answer: 
         """
# 负责构建模型的输入
prompt = PromptTemplate(template=template, input_variables=["question"])
llm = ChatOpenAI(
    base_url="https://api.openai-proxy.org/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-5.5",
    temperature=0.8,
)
# 新版 LCEL 写法：用管道运算符组合，提示词与模型访问用管道形成一个链
llm_chain = prompt | llm

# 调用时，输入一个字典（key 对应模板中的变量名）
response = llm_chain.invoke(
    {
        "question": "What is the population of the capital of the country where the Olympic Games were held in 2028"
    }
)
print(response.content)  # 注意新版返回的是 AIMessage 对象
