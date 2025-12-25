from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()


client = InferenceClient(
    model = "google/gemma-2b-it", 
    token = os.getenv("HUGGINGFACE_API_KEY")
)

response = client.text_generation(
    prompt = "explain quantum computing in simple terms",
    max_new_tokens = 100
)

print('-'*30)
print(response)
print(response.generated_text)
print('-'*30)

