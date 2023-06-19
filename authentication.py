import json
from datetime import datetime
import random
import os
import getpass
from cryptography.fernet import Fernet

# Load encryption key
with open("key.key", "rb") as key_file:
    encryption_key = key_file.read()

# Create Fernet cipher using the encryption key
cipher = Fernet(encryption_key)

# Authenticate user with username and PIN
def authenticate_user():
    username = input("Enter your username: ")
    pin = getpass.getpass("Enter your PIN: ")

    # Load user credentials from JSON file
    with open("credentials.json", "r") as credentials_file:
        credentials = json.load(credentials_file)

    if username in credentials and pin == decrypt(credentials[username]):
        return True

    return False

# Encrypt data using Fernet cipher
def encrypt(data):
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data.decode()

# Decrypt data using Fernet cipher
def decrypt(encrypted_data):
    decrypted_data = cipher.decrypt(encrypted_data.encode())
    return decrypted_data.decode()

# Generate encryption key if not already generated
if not os.path.exists("key.key"):
    encryption_key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(encryption_key)

# If encryption key is available, prompt for authentication
if os.path.exists("key.key"):
    authenticated = False
    while not authenticated:
        authenticated = authenticate_user()
        if not authenticated:
            print("Invalid username or PIN. Please try again.")

    print("Authentication successful.\n")

# ATM operations can be performed after successful authentication

# ... Rest of the code ...
