from langchain_ollama import OllamaEmbeddings
from index import vector_store
# vector embedding
embeddings = OllamaEmbeddings(
    model="nomic-embed-text:v1.5",
)

user_input = input("ASK>> ")

def retrieve_context(query:str):
    retrieved_docs = vector_store.similarity_search(query)
    

