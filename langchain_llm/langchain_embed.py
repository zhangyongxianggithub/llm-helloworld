import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain import OpenAI

load_dotenv()
# 下面的代码加载文件内容并按页划分
loader = PyPDFLoader(file_path="305966.pdf")
pages = loader.load_and_split()
# 使用open ai的嵌入技术
embeddings = OpenAIEmbeddings(
    base_url="https://api.openai-proxy.org/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)
# 使用向量数据库保存索引
db = FAISS.from_documents(pages, embeddings)
q = "中海油"
# 使用相似度查找
document = db.similarity_search(q)[0]
print(document)
llm = OpenAI(
    base_url="https://api.openai-proxy.org/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo-instruct",
    temperature=0.8,
)
# 使用检索到的信息作为上下文发送给LLM，回答用户的问题
chain = RetrievalQA.from_llm(llm=llm, retriever=db.as_retriever())
q = "中海油的主要业务"
result = chain.invoke(q, return_only_outputs=True)
print(result)
