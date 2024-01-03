# Extract product and company name from customer reviews
from src.utils import get_completion

prompt = f"""
Translate the following English text to Spanish:
```Hi, I would like to order a blender```
"""
response = get_completion(prompt)
print(response)

prompt = f"""
Tell me which language this is: 
```Combien coûte le lampadaire?```
"""
response = get_completion(prompt)
print(response)

prompt = f"""
Translate the following  text to French and Spanish and English pirate:
```I want to order a basketball```
"""
response = get_completion(prompt)
print(response)

prompt = f"""
Translate the following text to Spanish in both the formal and informal forms: 
'Would you like to order a pillow?'
"""
response = get_completion(prompt)
print(response)
