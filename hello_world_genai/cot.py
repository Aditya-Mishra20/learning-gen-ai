import os
from openai import OpenAI
from dotenv import load_dotenv
import json
# Chain of thaught prompting 
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")


client = OpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """

You're an expert AI Assistant in resolving user queries using chain of thought.
You work on START, PLAN and OUPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:

- Strictly Follow the given JSON output format
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

Output JSON Format:
{ "step": "START" | "PLAN" | "OUTPUT", "content": "string" }
Example:
START: Hey, Can you solve 2 + 3 * 5 / 10
PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem.
PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS
method" }
PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }  
PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
PLAN: { "step": "PLAN": "content": "now we must divide 15 / 10 which is 1.5" }
PLAN: { "step": "PLAN": "content": "now we must add 2 + 1.5 which is 3.5" }
OUTPUT: { "step": "OUTPUT", "content": "The final answer is 3.5" }

"""
response = client.chat.completions.create(
    model = 'gemini-2.5-flash',
    response_format={"type": "json_object"},
    messages = [
        {"role": "system" , "content" : SYSTEM_PROMPT },
        {"role": "user", "content": "write a program for first 10 prime numbers in python" },
        {"role": "assistant", "content": json.dumps("") }
    ]
)

print('-'*30)
print(response.choices[0].message.content)
print('-'*30)

# MANUAL INTERVENTION REQUIRED
# you run the program first , you get an output which goes in the assistent's content and then you run again to get the next step.
# repeat until you get the final OUTPUT step.
# it is a stateless connection
# all the messages need to be passed. 