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
    '''
        query: users' query 
    '''
    print(f"Searching Chunks...")
    #return relevent chunks from vector db
    search_results = vector_db.similarity_search(query)
    
    context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
    for result in search_results])
    return context

    SYSTEM_PROMPT = '''
   You are a helpfull AI Assistant who answeres user query based on the available context retrieved from a PDF file along with page_contents and page number.
    You should only answer the user based on the following context and navigate the user to open the right page number to know more.
    
    Context:
    {context_result}
    '''
    payload_to_model = {
            "model": "gemma2:2b",
            "stream": False,
            "format": "",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": query},
                ],
        }
    
    raw_response =  requests.post(model_url, json = payload_to_model)

    print(f"🤖 {raw_response.json()["message"]["content"]}")
    return (f"🤖 {raw_response.json()["message"]["content"]}")