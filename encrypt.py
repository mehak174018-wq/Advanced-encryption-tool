from cryptography.fernet import Fernet
import json
from key_manager import generate_key, generate_salt
from utils import get_file_metadata, get_encrypted_filename, prevent_overwrite
from logger import log_info, log_error

def encrypt_file(file_path, password):
    try:
        salt = generate_salt()
        key = generate_key(password, salt)
        cipher = Fernet(key)

        with open(file_path, "rb") as f:
            data = f.read()

        encrypted_data = cipher.encrypt(data)

        metadata = get_file_metadata(file_path)

        package = {
            "salt": salt.hex(),
            "metadata": metadata,
            "data": encrypted_data.decode()
        }

        output_file = get_encrypted_filename(file_path)
        prevent_overwrite(output_file)

        with open(output_file, "w") as f:
            json.dump(package, f)

        log_info(f"Encrypted: {file_path}")

        print("✅ File encrypted successfully!")

    except Exception as e:
        log_error(str(e))
        print("❌ Error:", e)