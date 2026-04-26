import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent, AgentType

load_dotenv()

template = """Question: {question}
            think step by step
            Answer: 
         """
llm = ChatOpenAI(
    base_url="https://api.openai-proxy.org/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo",
    temperature=0,
)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(
    tools=tools, llm=llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

question = "What is the square root of the population of the capital of the country where the Olympic Games were held in 2028"
response = agent.invoke(question)
print(response)
