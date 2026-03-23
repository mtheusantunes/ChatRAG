from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3", temperature=0.1)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente de estudos prestativo especialista em Deep Learning,"
     "LLMs, LangChain e LangGraph. Responda de forma clara, didática e sempre em português."),
    ("human", "{pergunta}")
])

parser = StrOutputParser()

chain = prompt | llm | parser

user_question = input("Digite sua pergunta: ")
print("Pensando...")

for chunk in chain.stream({"pergunta":  user_question}):
    print(chunk, end="", flush=True)