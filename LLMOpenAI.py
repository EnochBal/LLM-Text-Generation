"""This code allows you to import any OpenAI model and adjust its parameters to generate text"""

# Import necessary modules
import os
from openai import OpenAI  # Import the OpenAI module
from dotenv import load_dotenv  # Import the load_dotenv function from the dotenv module

# Load environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="Insert your key here")

# Generate text using the OpenAI model
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",  # Specify the model to use
    prompt="Create a short story",  # Provide a prompt for text generation
    max_tokens=100  # Set the maximum number of tokens for the generated text
)

# Extract the generated text from the response
generated_text = response.choices[0].text.strip()

# Print the generated text
print(generated_text)
