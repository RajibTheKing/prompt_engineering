import openai
import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env
openai.api_key = os.environ["OPEN_ROUTER_API_KEY"]

# client = openai.OpenAI(api_key=openai.api_key)
client = openai.OpenAI(base_url="https://openrouter.ai/api/v1", api_key=openai.api_key)
# model_name = "gpt-3.5-turbo"  # or any other model you want to use
model_name = "deepseek/deepseek-r1:free"

# Define your app metadata (required by OpenRouter)
app_headers = {
    "HTTP-Referer": "https://rtsys-lab.de",  # Your app's website (optional)
    "X-Title": "RTSYS Lab - Prompt Engineering",                 # Your app's name (required)
    "X-Description": "A personal LLM playground",      # Short description (optional)
    "X-Author": "Rajib Chandra Das",                    # Your name or org (optional)
}

def get_completion(prompt, model=model_name):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        extra_headers=app_headers  # <-- Use extra_headers instead of headers
    )
    return response.choices[0].message.content

def print_llm_response(promt):
    response = get_completion(promt)
    print(f"Prompt: {promt}\nResponse: {response}\n")

def get_llm_response(prompt):
    response = get_completion(prompt)
    return response