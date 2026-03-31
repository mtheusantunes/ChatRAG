# ChatRAG 🤖📚

[Português](#português) | [English](#english)

<a name="português"></a>
## Versão em Português

O **ChatRAG** é um sistema de Inteligência Artificial baseado na arquitetura RAG (*Retrieval-Augmented Generation*). Ele permite que os usuários façam perguntas sobre documentos em PDF e obtenham respostas precisas, geradas localmente por uma LLM, utilizando estritamente o contexto extraído do documento original.

Este projeto foi desenvolvido como objeto de estudo para aprofundar conhecimentos em orquestração de Agentes Inteligentes, Bancos de Dados Vetoriais e Modelos de Linguagem de Grande Escala (LLMs).

## 🚀 Tecnologias Utilizadas

*   **Linguagem:** Python
*   **Framework de Orquestração:** [LangChain](https://python.langchain.com/)
*   **LLM Local:** [Ollama](https://ollama.com/) (Modelo: `llama3` com temperature `0.1`)
*   **Banco de Dados Vetorial:** [Weaviate](https://weaviate.io/) (Conteinerizado via Docker)
*   **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
*   **Processamento de Documentos:** `PyPDFLoader` e `RecursiveCharacterTextSplitter`

## 🧠 Como Funciona

1.  **Ingestão de Dados:** O sistema lê um documento PDF local, divide o texto em fragmentos menores (*chunks* de 1000 caracteres com *overlap* de 200) mantendo a coerência semântica.
2.  **Vetorização:** Os fragmentos de texto são convertidos em vetores (*embeddings*) usando um modelo do HuggingFace (processamento em CPU).
3.  **Armazenamento:** Esses vetores são armazenados em um banco de dados Weaviate rodando localmente em um contêiner Docker.
4.  **Recuperação e Geração (RAG):** Quando o usuário faz uma pergunta, o sistema busca os 3 fragmentos mais relevantes (`k=3`) no banco de dados e os envia, junto com a pergunta e um prompt otimizado, para o Llama 3 formular uma resposta em português brasileiro de forma simples e direta.

## 📋 Pré-requisitos

Para rodar este projeto na sua máquina, você precisará de:

*   [Python 3.8+](https://www.python.org/downloads/)
*   [Docker e Docker Compose](https://docs.docker.com/get-docker/) (para rodar o Weaviate)
*   [Ollama](https://ollama.com/download) instalado e rodando.

Além disso, é necessário baixar o modelo `llama3` no Ollama. No seu terminal, execute:
```bash
ollama run llama3
```

## 🛠️ Instalação e Execução

**1. Clone o repositório:**
```bash
git clone [https://github.com/mtheusantunes/ChatRAG.git](https://github.com/mtheusantunes/ChatRAG.git)
cd ChatRAG
```

**2. Instale as dependências:**
*(Recomenda-se o uso de um ambiente virtual)*
```bash
pip install langchain langchain-community langchain-huggingface langchain-weaviate langchain-ollama weaviate-client pypdf
```

**3. Suba o Banco de Dados Vetorial (Weaviate):**
Na raiz do projeto, execute o Docker Compose para iniciar o banco na porta 8080:
```bash
docker-compose up -d
```

**4. Prepare o Documento e Popule o Banco:**
Coloque o seu documento PDF na pasta `docs/` e certifique-se de que o caminho no código Python database_feeder (no bloco de extração de dados) aponta para o arquivo correto. Em seguida, execute o script de ingestão.
*(Aguarde até ver a mensagem "PDF está no banco!")*

**5. Inicie o Chat:**
Execute o script principal que inicializa a chain RAG e comece a interagir com a IA pelo terminal.

## 👤 Autor

**Matheus Antunes**
* Estudante de Ciência da Computação | Desenvolvedor Full Stack
* LinkedIn: [linkedin.com/in/mtheusantunes](https://www.linkedin.com/in/mtheusantunes)
* GitHub: [github.com/mtheusantunes](https://github.com/mtheusantunes)

---

<a name="english"></a>
## English Version

**ChatRAG** is an Artificial Intelligence system based on the RAG (Retrieval-Augmented Generation) architecture. It allows users to ask questions about PDF documents and get accurate answers, generated locally by an LLM, strictly using the context extracted from the original document.

## 🚀 Technologies Used

*   **Language:** Python
*   **Orchestration Framework:** LangChain
*   **Local LLM:** Ollama (Model: `llama3` with temperature `0.1`)
*   **Vector Database:** Weaviate (Dockerized)
*   **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)

## 🧠 How it Works

1.  **Data Ingestion:** Reads a local PDF and splits it into chunks.
2.  **Vectorization:** Converts chunks into embeddings using HuggingFace.
3.  **Storage:** Stores vectors in a local Weaviate Docker container.
4.  **RAG:** Retrieves the top 3 most relevant context chunks and prompts the Llama 3 model to answer the user's question.

## 📋 Prerequisites

*   Python 3.8+
*   Docker & Docker Compose
*   Ollama with the `llama3` model downloaded (`ollama run llama3`).

## 🛠️ Setup

1.  Clone the repository and install the required dependencies via `pip`.
2.  Run `docker-compose up -d` to start the Weaviate vector database.
3.  Place your target PDF in the `docs/` folder and adjust the path in the script database_feeder.
4.  Run the ingestion logic to populate the database.
5.  Run the chat logic to start interacting with the local AI.
