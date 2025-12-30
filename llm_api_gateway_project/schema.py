from pydantic import BaseModel, Field
from typing import List
import requests
import json

class SummaryRequest(BaseModel):
    text: str 
    max_bullets: int = Field(
        ..., 
        description="Maximum number of bullet points to generate.", 
        ge=1, 
        le=20)
    

class SummaryResponse(BaseModel):
    text:str
    bullets: List[str] = Field(
        ...,
        description="List of bullet points summarizing the input text.",
        max_length = 1
    )
    
SYSTEMPROMPT = """
    You are a system that strictly returns JSON format.
    Schema for output is as follows:
    {{
        text: string,
        bullet_points:string[]
    }}
    Rules to follow:
    - Output only valid json.
    - No markdown
    - No explanations
    - Max bullet points should be specified by user.
    
    Example : 
    Input:
    {{
      "text": "TCP is a connection-oriented protocol that ensures reliable data transfer using acknowledgements and retransmissions. It starts with a three-way handshake.",
      "max_bullets": 3
    }}
    Output:
    {{
      "text": "TCP is a reliable, connection-oriented protocol that uses a three-way handshake to establish connections.",
      "bullet_points": [
        "Connection-oriented protocol",
        "Ensures reliable data transfer",
        "Uses three-way handshake"
      ]
    }}
    """
    
model_url = "http://localhost:11434/api/chat"

message_history = [{
    "role": "system",
    "content": SYSTEMPROMPT
}]

user_input = {
  "text": "I have two friends. The first is Ollama 22 years old busy saving the world, and the second is Alonso 23 years old and wants to hang out. Return a list of friends",
  "max_bullets": 3
}

message_history.append(
    {"role": "user", "content": str(user_input)})



payload_to_model = {
    "model": "gemma2:2b",
    "stream": False,
    "format": SummaryResponse.model_json_schema(),
    "messages": message_history,
}


raw_response =  requests.post(model_url, json = payload_to_model)

print("raw response >>", raw_response.json()['message']['content'])

result_in_text= raw_response.json()['message']['content']

# print("result ", type(result_in_text))


def json_extractor_and_schema_validation( text:str, retries = 2)-> SummaryResponse:
    if not text or not text.strip():
        raise ValueError("Empty response from model")
    #validation
    try:
        parsed = json.loads(text)
        validated_result = SummaryResponse.model_validate(parsed)
        return validated_result
    except Exception as e:
        if retries==0:
            print("Error validating response:", e)
            raise e
        CORRECTION_PROMPT = f""" 
                The previous output failed validation.
                Error:
                {e}
                Return corrected JSON ONLY.
        """
        message_history.append(
        {"role": "user", "content": str(CORRECTION_PROMPT)})
        payload_to_model["messages"] = message_history
        corrected_raw_response = requests.post(model_url, json = payload_to_model)
        corrected_text = corrected_raw_response.json()['message']['content']
        return json_extractor_and_schema_validation(corrected_text, retries -1)
        
        
    
    

res = json_extractor_and_schema_validation(result_in_text)
print("Final structured response >>", res)
