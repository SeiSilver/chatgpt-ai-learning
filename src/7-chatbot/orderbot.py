# We can automate the collection of user prompts and assistant responses to build a OrderBot.
# The OrderBot will take orders at a pizza restaurant.
import json

from src.utils import get_completion_from_messages

context = [
    {
        'role': 'system', 'content': """
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collects the order, and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final 
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style, the response must in JSON format. \
Example Json:
{
    "isGoodBye": false,  # required, this field is used to identify if the order is successful, payment is completed, \
    or the customer has taken the order and is leaving the store 
    "content": "response" # required
}
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""}
]


def order_bot():
    print("Hello! Welcome to PizzaBot. I'm here to help you place your order.")

    # Main loop
    while True:
        user_input = input("You: ").lower().strip()

        context.append({
            'role': "user",
            'content': user_input
        })

        response = get_completion_from_messages(context, temperature=1)
        json_response = json.loads(response)

        print(f"Bot: {json_response["content"]}")
        context.append({
            'role': "assistant",
            'content': response.strip()
        })

        if json_response["isGoodBye"]:
            break

    print("\nThank you for ordering from PizzaBot! Have a great day.")


# Run the OrderBot
order_bot()
