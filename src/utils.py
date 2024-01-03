import os

import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI()


def get_completion(prompt_input, model="gpt-3.5-turbo-1106", temperature=0):
    messages = [
        {"role": "user", "content": prompt_input}
    ]
    data = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return data.choices[0].message.content


def get_completion_from_messages(messages, model="gpt-3.5-turbo-1106", temperature=0):
    data = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    response = data.choices[0].message.content
    return response
