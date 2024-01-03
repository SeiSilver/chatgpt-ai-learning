# Writing can vary based on the intended audience.
# ChatGPT can produce different tones.

from src.utils import get_completion

prompt = f"""
Translate the following from slang to a business letter: 
'Dude, This is Joe, check out this spec on this standing lamp.'
"""
response = get_completion(prompt)
print(response)
