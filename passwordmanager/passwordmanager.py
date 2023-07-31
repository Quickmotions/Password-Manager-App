# Fergus Haak - 31/07/2023 - password manager- Password Manager Program

from passwordmanager.entry import Entry, EntryFactory
from passwordmanager.encryption import encrypt, decrypt
from passwordmanager.storage import save_entries, load_entries
from passwordmanager.input_validation import validate_input

class PasswordManager:
    def __init__(self):
        self.entries = []

    def create_entry(self, entry_data) -> None:
        # Create a new entry using the EntryFactory and add it to the entries list
        if validate_input(entry_data):
            entry_type = entry_data.get("type")  # Assuming the 'type' key indicates the entry type
            if entry_type == "Login":
                entry = EntryFactory.create_login_entry(
                    entry_data.get("id"),
                    entry_data.get("username"),
                    entry_data.get("password"),
                    entry_data.get("website"),
                )
            elif entry_type == "Credit Card":
                entry = EntryFactory.create_credit_card_entry(
                    entry_data.get("id"),
                    entry_data.get("cardholder_name"),
                    entry_data.get("card_number"),
                    entry_data.get("expiration_date"),
                    entry_data.get("cvv"),
                )
            else:
                # Handle other entry types if needed
                return

            self.entries.append(entry)

    def delete_entry(self, entry_id) -> None:
        # Find and delete an entry based on the given entry_id
        for entry in self.entries:
            if entry.entry_id == entry_id:
                self.entries.remove(entry)
                return

    def edit_entry(self, entry_id, new_data) -> None:
        # Find and edit an entry based on the given entry_id and new_data
        for entry in self.entries:
            if entry.entry_id == entry_id:
                entry_type = entry.get_type()
                if entry_type == "Login" and "website" in new_data:
                    entry.update(
                        new_data.get("username", entry.username),
                        new_data.get("password", entry.password),
                        new_data.get("website", entry.website),
                    )
                elif entry_type == "Credit Card":
                    entry.update(
                        new_data.get("cardholder_name", entry.username),
                        new_data.get("card_number", entry.password),
                        new_data.get("expiration_date", entry.expiration_date),
                        new_data.get("cvv", entry.cvv),
                    )
                # Handle other entry types if needed
                return

    def search(self, query) -> list[Entry]:
        # Search for entries based on the given query and return matching entries
        results = []
        for entry in self.entries:
            if entry.matches_query(query):
                results.append(entry)
        return results

    def find_id(self, id) -> Entry:
        for entry in self.entries:
            if id == entry.entry_id:
                return entry

    def save_entries(self, file_path, encryption_key) -> None:
        # Save the list of entries to a file using encryption for security
        # You can use the encryption functions from encryption.py
        encrypted_entries = encrypt(self.entries, encryption_key)
        save_entries(file_path, encrypted_entries)

    def load_entries(self, file_path, encryption_key) -> None:
        # Load the list of entries from a file and decrypt the data if needed
        # You can use the decryption functions from encryption.py
        encrypted_entries = load_entries(file_path)
        self.entries = decrypt(encrypted_entries, encryption_key)


# Additional helper functions (if needed) can be defined outside the class
