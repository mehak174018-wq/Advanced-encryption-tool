from cryptography.fernet import Fernet
import json
from key_manager import generate_key
from logger import log_info, log_error

def decrypt_file(file_path, password):
    try:
        with open(file_path, "r") as f:
            package = json.load(f)

        salt = bytes.fromhex(package["salt"])
        key = generate_key(password, salt)
        cipher = Fernet(key)

        decrypted_data = cipher.decrypt(package["data"].encode())

        original_name = package["metadata"]["filename"]

        with open(original_name, "wb") as f:
            f.write(decrypted_data)

        log_info(f"Decrypted: {file_path}")

        print("✅ File decrypted successfully!")

    except Exception as e:
        log_error(str(e))
        print("❌ Error:", e)