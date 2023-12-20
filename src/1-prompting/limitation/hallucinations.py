# Prompting Principles
# Limitation
# Hallucination:
#   - Makes statements that sound reasonable but are not true
#
# Reducing hallucinations:
#   - First find relevant information
#   - Then answer the question
#   - Based on the relevant information.
from src.utils import get_completion

# Noted: Coca-Cola is a real company, the product name is not real.
prompt = f"""
Tell me about Spanish Smart Drink by Coca-Cola
"""
response = get_completion(prompt)
print(response)
