# ChatGPT can translate between formats.
# The prompt should describe the input and output formats.

from src.utils import get_completion

data_json = {
    "resturant employees": [
        {"name": "Shyam", "email": "shyamjaiswal@gmail.com"},
        {"name": "Bob", "email": "bob32@gmail.com"},
        {"name": "Jai", "email": "jai87@gmail.com"}
    ]
}

prompt = f"""
Translate the following python dictionary from JSON to an HTML \
table with column headers and title: {data_json}
"""
response = get_completion(prompt)
print(response)
