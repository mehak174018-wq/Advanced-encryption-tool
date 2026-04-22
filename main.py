import os
from encrypt import encrypt_file

def encrypt_folder(folder_path, password):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            encrypt_file(full_path, password)