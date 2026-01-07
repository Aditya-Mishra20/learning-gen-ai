from langchain_ollama import OllamaEmbeddings
from index import vector_store
from langchain_qdrant import QdrantVectorStore
# vector embedding
embeddings = OllamaEmbeddings(
    model="nomic-embed-text:v1.5",
)

vector_db = QdrantVectorStore.from_existing_collection(
    
)

# user_input = input("ASK>> ")

# def retrieve_context(query:str):
#     retrieved_docs = vector_store.similarity_search(query)
    
# context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
# for result in search_results])

# SYSTEM_PROMPT = '''
#    You are a helpfull AI Assistant who answeres user query based on the available context retrieved from a PDF file along with page_contents and page number.
#     You should only ans the user based on the following context and navigate the user to open the right page number to know more.
    
# Context:
# '''

