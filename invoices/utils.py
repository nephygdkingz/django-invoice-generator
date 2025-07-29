import uuid
import secrets
import os
from django.core.files import File
from django.core.files.storage import default_storage

def generate_invoice_number():
    """
    Generates a unique, uppercase invoice number using UUID4 and secure random hex.
    Example: INV-8F3B1E2C-A9F3
    """
    uuid_part = str(uuid.uuid4()).split('-')[0].upper()       # 8 characters
    random_part = secrets.token_hex(2).upper()                # 4 characters
    return f"INV-{uuid_part}-{random_part}"


def save_temp_uploaded_file(file_obj, folder="tmp"):
    """
    Saves an uploaded file to a temporary location using Django's storage system.
    Returns the relative path (to be saved in session).
    """
    filename = file_obj.name
    path = os.path.join(folder, filename)
    saved_path = default_storage.save(path, file_obj)
    return saved_path  


def load_temp_uploaded_file(path):
    """
    Loads a file from the given relative path and returns a Django File object.
    """
    if not path:
        return None
    try:
        file = default_storage.open(path, 'rb')
        return File(file)
    except FileNotFoundError:
        return None