from google import genai
from dotenv import load_dotenv

load_dotenv()


client = genai.Client()

response = client.models.generate_content(
    model = 'gemini-2.5-flash', contents = 'hi, how are you?' 
)

print(response)
print(response.text)
# print(response.prompt_token_count)
# print(response.total_token_count)