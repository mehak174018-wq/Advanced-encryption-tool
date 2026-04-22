import os

def get_file_metadata(file_path):
    return {
        "filename": os.path.basename(file_path),
        "size": os.path.getsize(file_path)
    }

def get_encrypted_filename(file_path):
    return file_path + ".enc"

def prevent_overwrite(file_path):
    if os.path.exists(file_path):
        raise FileExistsError("File already exists! Rename or delete it.")