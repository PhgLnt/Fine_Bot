import random
import requests
import json

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

xich = ['xich', 'xích']

starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot!"
]


def handle_response(message) -> str:
    f_message = message.lower()

    if f_message == 'hello':
        return 'Hey there!'

    if f_message == 'bye':
        return 'Good bye!'

    if f_message == 'roll':
        return str(random.randint(1, 6))

    if f_message == 'fhelp':
        return "`Google is free.`"

    if any(word in f_message for word in xich):
        return "Xích cái gì mà Xích. Xích là đồ tồi"

    if f_message.startswith('fquote'):
        quote = get_quote()
        return (quote)

    if any(word in f_message for word in sad_words):
        return (random.choice(starter_encouragements))

    return None


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)




