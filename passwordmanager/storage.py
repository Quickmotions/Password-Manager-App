# Fergus Haak - 31/07/2023 - storage - Password Manager Program

import pickle

def save_entries(file_path, entries):
    # Save the list of entries to a file using serialization (pickle)
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(entries, file)
        print("Entries saved successfully.")
    except IOError as e:
        print(f"Error: Unable to save entries to the file.\n{e}")

def load_entries(file_path):
    # Load the list of entries from a file using deserialization (pickle)
    try:
        with open(file_path, 'rb') as file:
            entries = pickle.load(file)
        print("Entries loaded successfully.")
        return entries
    except (IOError, pickle.UnpicklingError) as e:
        print(f"Error: Unable to save entries to the file.\n{e}")
        return []
