import secrets
import string

ALPHABET = string.ascii_letters + string.digits

def get_code(length = 10):
    return "".join(secrets.choice(ALPHABET) for _ in range(length))