import uuid
import secrets

def generate_invoice_number():
    """
    Generates a unique, uppercase invoice number using UUID4 and secure random hex.
    Example: INV-8F3B1E2C-A9F3
    """
    uuid_part = str(uuid.uuid4()).split('-')[0].upper()       # 8 characters
    random_part = secrets.token_hex(2).upper()                # 4 characters
    return f"INV-{uuid_part}-{random_part}"
