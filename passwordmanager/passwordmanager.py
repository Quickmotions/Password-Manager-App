# Fergus Haak - 31/07/2023 - password manager- Password Manager Program

from passwordmanager.entry import Entry, EntryFactory
from passwordmanager.encryption import encrypt, decrypt
from passwordmanager.storage import save_entries, load_entries
from passwordmanager.input_validation import validate_input

import csv

class PasswordManager:
    def __init__(self):
        self.entries = []

    def create_entry(self, entry_data) -> None:
        # Create a new entry using the EntryFactory and add it to the entries list
        if validate_input(entry_data, self.entries):
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

    def save_encryption_key(self, file_path, encryption_key):
        save_entries(file_path, encryption_key)

    def load_encryption_key(self, file_path):
        return load_entries(file_path)

    def export_to_csv(self, file_path):
        # Define the field names for the CSV file
        field_names = ["Entry ID", "Type", "Username", "Password", "Website", "Cardholder Name", "Card Number",
                       "Expiration Date", "CVV"]

        # Prepare the data to write to the CSV file
        data_to_write = []
        for entry in self.entries:
            entry_data = {
                "Entry ID": entry.entry_id,
                "Type": entry.get_type(),
                "Username": entry.username,
                "Password": entry.password,
                "Website": getattr(entry, "website", ""),  # Using getattr to handle optional attributes
                "Cardholder Name": getattr(entry, "username", ""),  # Using getattr to handle optional attributes
                "Card Number": getattr(entry, "password", ""),  # Using getattr to handle optional attributes
                "Expiration Date": getattr(entry, "expiration_date", ""),  # Using getattr to handle optional attributes
                "CVV": getattr(entry, "cvv", ""),  # Using getattr to handle optional attributes
            }
            data_to_write.append(entry_data)

        # Write data to the CSV file
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data_to_write)

# Additional helper functions (if needed) can be defined outside the class
