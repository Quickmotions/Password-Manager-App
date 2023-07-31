# Fergus Haak - 31/07/2023 - encryption - Password Manager Program

from cryptography.fernet import Fernet
import pickle

def generate_key():
    # Generate a random encryption key
    return Fernet.generate_key()

def encrypt(entries, encryption_key):
    # Encrypt the list of entries using the encryption key
    try:
        cipher_suite = Fernet(encryption_key)
        serialized_entries = pickle.dumps(entries)
        encrypted_entries = cipher_suite.encrypt(serialized_entries)
        return encrypted_entries
    except Exception as e:
        print(f"Error during encryption: {e}")
        return None

def decrypt(encrypted_entries, encryption_key):
    # Decrypt and deserialize the encrypted entries using the encryption key
    try:
        cipher_suite = Fernet(encryption_key)
        decrypted_entries = cipher_suite.decrypt(encrypted_entries)
        entries = pickle.loads(decrypted_entries)
        return entries
    except Exception as e:
        print(f"Error during decryption: {e}")
        return None
