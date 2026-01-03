from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
# from langchain_core.vectorstores import InMemoryVectorStore
from qdrant_client.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

#initialize
pdf_path = Path(__file__).parent / "API Questions.pdf"
loader = PyPDFLoader(pdf_path)

#load
docs = loader.load()

# print(docs[0])
# print(type(docs[0]))
# print(docs[0].page_content)

#split the docs into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=40)
chunks = text_splitter.split_documents(documents=docs)
# print(chunks)
# print(type(chunks))
text = "LangChain is the framework for building context-aware reasoning applications"

# vector embedding
embeddings = OllamaEmbeddings(
    model="nomic-embed-text:v1.5",
)

# qdrant vector store connection
# client = QdrantClient(":memory:")

# vector_size = len(embeddings.embed_query("sample text"))

# if not client.collection_exists("test"):
#     client.create_collection(
#         collection_name="test",
#         vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
#     )
vector_store = QdrantVectorStore.from_documents(
    documents = chunks,
    embedding=embeddings,
    url= "http://localhost:6333",
    collection_name = "learning_rag"
)



print("indexing of document is completed")
