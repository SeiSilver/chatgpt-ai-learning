
import os

import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI()


def get_completion(prompt_input, model="gpt-3.5-turbo-1106"):
    messages = [
        {"role": "user", "content": prompt_input}
    ]
    data = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return data.choices[0].message.content