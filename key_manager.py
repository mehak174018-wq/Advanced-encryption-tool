from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64

def generate_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def generate_salt():
    return os.urandom(16)

def save_key(key, filename="key.key"):
    with open(filename, "wb") as f:
        f.write(key)

def load_key(filename="key.key"):
    with open(filename, "rb") as f:
        return f.read()