from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3", temperature=0.1)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente de estudos prestativo especialista em Deep Learning,"
     "LLMs, LangChain e LangGraph. Responda de forma clara, didática e sempre em português."),
    ("human", "{pergunta}")
])
