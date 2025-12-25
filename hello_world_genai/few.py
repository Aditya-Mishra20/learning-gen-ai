import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")


client = OpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = "Classify the sentiment of the following text as positive, negative, or neutral.Text: The product is terrible. Sentiment: Negative Text: Super helpful, worth it Sentiment: Positive"
response = client.chat.completions.create(
    model = 'gemini-2.5-flash',
    messages = [
        {"role": "system" , "content" : SYSTEM_PROMPT },
        {"role": "user", "content": "Text: i eat cake! Sentiment:" }
    ]
)

print('-'*30)
print(response.choices[0].message.content)
print('-'*30)