import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key="Insert you key here")

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Create a short story",
    max_tokens=100
)
generated_text = response.choices[0].text.strip()
print(generated_text)