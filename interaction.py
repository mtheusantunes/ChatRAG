from langchain_huggingface import HuggingFaceEmbeddings
from langchain_weaviate.vectorstores import WeaviateVectorStore
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import weaviate

# Embedding
embeddings = HuggingFaceEmbeddings(
    model_name = "all-MiniLM-L6-v2",
    model_kwargs = {'device': 'cpu'}
)

# Database connection
weaviate_client = weaviate.connect_to_local()
vector_store = WeaviateVectorStore(
    embedding=embeddings,
    client=weaviate_client,
    index_name="StudyMaterials",
    text_key="text"
)

retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# LLM settings
llm = ChatOllama(model="llama3", temperature=0.1)

# Prompt Engineering
prompt = ChatPromptTemplate.from_messages([
    ("system", "Use os contextos abaixo para responder a questão no fim. Se não souber a resposta, "
     "apenas diga que não sabe, não tente inventar uma resposta. Use no máximo três sentenças para "
     "manter a resposta mais simples o possível. Responda sempre em português brasileiro."
     "Sempre diga 'obrigado por perguntar' no fim da resposta. Contexto: {context} Pergunta: {question} "
     "Resposta útil:"),
    ("human", "{question}")
])

# Chain RAG
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Test
user_question = input("Usuário: ")
print("Thinking...")
for chunk in rag_chain.stream(user_question):
    print(chunk, end="", flush=True)

weaviate_client.close()