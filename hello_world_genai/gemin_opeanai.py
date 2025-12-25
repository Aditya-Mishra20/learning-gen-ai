import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")


client = OpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model = 'gemini-2.5-flash',
    messages = [
        {"role": "system", "content": "You are a Mathematician. You help users in solving maths queries. You only response to maths related queries and nothing else. If the query is not related to maths then say sorry and ask for maths related query."},
        {"role": "user", "content": "write me python script to solve the sum of first 10 natural numbers." }
    ]
)

print('-'*30)
print(response.choices[0].message.content)
print('-'*30)