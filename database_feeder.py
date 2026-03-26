import os
import weaviate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_weaviate.vectorstores import WeaviateVectorStore

try: 
    # Extracting Data
    pdf_path = "docs/Escola de Verão 2026 - Minicurso de Agentes.pdf"

    if not os.path.exists(pdf_path):
        print("Erro: Documento {pdf_path} não encontrado")
        exit()
    
    print("Lendo o PDF...")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Chunking
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    # Embedding
    embeddings = HuggingFaceEmbeddings(
        model_name = "all-MiniLM-L6-v2",
        model_kwargs = {'device': 'cpu'}
    )

    # Database connection
    weaviate_client = weaviate.connect_to_local()
    vector_store = WeaviateVectorStore.from_documents(
        chunks,
        embeddings,
        client=weaviate_client,
        index_name="StudyMaterials"
    )
    print("PDF está no banco!")

finally:
    weaviate_client.close()