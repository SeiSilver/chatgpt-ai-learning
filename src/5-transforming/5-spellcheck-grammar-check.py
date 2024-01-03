# Here are some examples of common grammar and spelling problems and the LLM's response.
# To signal to the LLM that you want it to proofread your text,
# you instruct the model to 'proofread' or 'proofread and correct'.

from src.utils import get_completion
from redlines import Redlines
import markdown

print("Example 1: ")

text = [
    "The girl with the black and white puppies have a ball.",  # The girl has a ball.
    "Yolanda has her notebook.",  # ok
    "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
    "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
    "Your going to need you’re notebook.",  # Homonyms
    "That medicine effects my ability to sleep. Have you heard of the butterfly affect?",  # Homonyms
    "This phrase is to cherck chatGPT for speling abilitty"  # spelling
]
for t in text:
    prompt = f"""Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    and errors, just say "No errors found". Don't use 
    any punctuation around the text:
    ```{t}```"""
    response = get_completion(prompt)
    print(response)

print("Example 2: ")

text = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""
prompt = f"proofread and correct this review: ```{text}```"
response = get_completion(prompt)
print(response)

diff = Redlines(text, response)
html = markdown.markdown(diff.output_markdown)

print(html)

