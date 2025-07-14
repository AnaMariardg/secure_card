import hashlib
from utils.helpers import load_card_data

def generate_token():
    data = load_card_data()
    card_string = f"{data['card_number']}{data['card_holder']}{data['cvv']}{data['expiration']}"
    token = hashlib.sha256(card_string.encode()).hexdigest()
    return token
