from langchain_ollama import OllamaEmbeddings
import requests
from langchain_qdrant import QdrantVectorStore

# vector embedding
embeddings = OllamaEmbeddings(
    model="nomic-embed-text:v1.5",
)

model_url = "http://localhost:11434/api/chat"


vector_db = QdrantVectorStore.from_existing_collection(

    url= "http://localhost:6333",
    collection_name = "learning_rag",
    embedding=embeddings
)

def process_query(query:str):
    print(f"Searching Chunks...")
    #return relevent chunks from vector db
    search_results = vector_db.similarity_search(query)
    
    context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
    for result in search_results])
    return context