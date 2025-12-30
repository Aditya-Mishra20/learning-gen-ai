import os
from openai import OpenAI
from dotenv import load_dotenv
import json
import requests
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")


client = OpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def get_weather(city: str) :
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in city {city} is {response.text}."


SYSTEM_PROMPT = """

    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    For every tool call wait for OBSERVE step to get the tool output.
    You can use tools if required from the list of tools below:

    Available Tools:
    - get_weather(city: str) : Returns the current weather information for the specified city.


    Rules:

    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

    Example 1:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem.
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS
    method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }  
    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN": "content": "now we must divide 15 / 10 which is 1.5" }
    PLAN: { "step": "PLAN": "content": "now we must add 2 + 1.5 which is 3.5" }
    OUTPUT: { "step": "OUTPUT", "content": "The final answer is 3.5" }

    Example 1:
    START: Hey,What is the current weather of Jaipur?
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in current weather of a city called Jaipur.
    PLAN: { "step": "PLAN": "content": "This query requires real time information. Let's see if relevant tool is available." }
    PLAN: { "step": "PLAN": "content": "Yes, Tool is available i.e get weather. I will use this tool." }  
    PLAN: { "step": "TOOL": "tool": "get_weather", "input": "Jaipur" }
    PLAN: { "step": "OBSERVE": "tool": "get_weather", "output": "The weather in city Jaipur is 20°C." }
    PLAN: { "step": "TOOL": "content": "I have received the weather information for Jaipur." }

    OUTPUT: { "step": "OUTPUT", "content": "The weather in city Jaipur is cloudy 20 C." }

    """

class OUTPUTFORMAT(BaseModel):
    step:str = Field(
        ...,
        description = "The ID of the step. It can be START, PLAN, OUTPUT, TOOL,OBSERVE etc."
    )
    content : Optional[str] = Field(
        None, 
        description = "The optional content of the step."
    )
    tool : Optional[str] = Field(
        None,
        description = "The ID of the tool to be used."
    )
    input : Optional[str] = Field(
        None,
        description = "The input to be given to the tool."
    )
    

available_tools = {    "get_weather": get_weather
}

message_history = [
    {"role": "system" , "content" : SYSTEM_PROMPT },
]

user_input = input("Enter your query: ")
message_history.append({"role": "user", "content": user_input})

while True:
    response = client.chat.completions.parse(
    model = 'gemini-2.5-flash',
    response_format=OUTPUTFORMAT,
    messages =message_history
    )
    
    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = response.choices[0].message.parsed
 
    
    if parsed_result.step == "START":
        print(f"🔥", parsed_result.content)
    elif parsed_result.step == "TOOL":
        tool_to_call = parsed_result.tool
        input_to_call = parsed_result.input
        print(f"🛠️ ", tool_to_call, input_to_call)
        tool_response = available_tools[tool_to_call](input_to_call)
        print(f"🛠️, {tool_to_call}, ({input_to_call}) = {tool_response}")
    
        message_history.append({"role": "developer", "content": json.dumps({ "step": "OBSERVE", "tool": tool_to_call, "output": tool_response })})  
        
    elif parsed_result.step == "PLAN":
        print(f"📝", parsed_result.content)
    elif parsed_result.step == "OUTPUT":
        print(f"✅", parsed_result.content)
        break