# Fergus Haak - 31/07/2023 - main - Password Manager Program

# main.py

from passwordmanager.passwordmanager import PasswordManager
from passwordmanager.encryption import generate_key


def main():
    # Generate a random encryption key (for demonstration purposes)
    encryption_key = generate_key()

    # Create an instance of the PasswordManager class
    password_manager = PasswordManager()

    while True:
        choice = get_choice()

        if choice == 0:
            print("Exiting the program.")
            break
        elif choice == 1:
            create_entry(password_manager)
        elif choice == 2:
            delete_entry(password_manager)
        elif choice == 3:
            edit_entry(password_manager)
        elif choice == 4:
            search_entries(password_manager)
        elif choice == 5:
            save_entries(password_manager, encryption_key)
        elif choice == 6:
            load_entries(password_manager, encryption_key)
        else:
            print("Invalid choice. Please try again.")


def get_choice():
    print("\nMenu:")
    print("1. Create Entry")
    print("2. Delete Entry")
    print("3. Edit Entry")
    print("4. Search Entries")
    print("5. Save Entries")
    print("6. Load Entries")
    print("0. Exit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid choice. Please enter a number.")


def create_entry(password_manager):
    entry_data = {}
    entry_data["type"] = input("Enter entry type (Login/Credit Card): ").title()
    entry_data["id"] = int(input("Enter entry ID: "))
    entry_data["username"] = input("Enter username: ")
    entry_data["password"] = input("Enter password: ")

    if entry_data["type"] == "Login":
        entry_data["website"] = input("Enter website: ")
    elif entry_data["type"] == "Credit Card":
        entry_data["cardholder_name"] = input("Enter cardholder name: ")
        entry_data["card_number"] = input("Enter card number: ")
        entry_data["expiration_date"] = input("Enter expiration date: ")
        entry_data["cvv"] = input("Enter CVV: ")

    password_manager.create_entry(entry_data)


def delete_entry(password_manager):
    entry_id = int(input("Enter the ID of the entry to delete: "))
    password_manager.delete_entry(entry_id)


def edit_entry(password_manager):
    entry_id = int(input("Enter the ID of the entry to edit: "))
    entry = password_manager.find_id(entry_id)
    if entry:
        new_data = {}
        new_data["username"] = input("Enter new username (leave empty to keep the same): ")
        new_data["password"] = input("Enter new password (leave empty to keep the same): ")

        if entry.get_type() == "Login":
            new_data["website"] = input("Enter new website (leave empty to keep the same): ")
        elif entry.get_type() == "Credit Card":
            new_data["cardholder_name"] = input("Enter new cardholder name (leave empty to keep the same): ")
            new_data["card_number"] = input("Enter new card number (leave empty to keep the same): ")
            new_data["expiration_date"] = input("Enter new expiration date (leave empty to keep the same): ")
            new_data["cvv"] = input("Enter new CVV (leave empty to keep the same): ")

        password_manager.edit_entry(entry_id, new_data)
    else:
        print(f"Entry with ID {entry_id} not found.")


def search_entries(password_manager):
    query = input("Enter the search query: ")
    results = password_manager.search(query)
    if results:
        print("\nSearch Results:")
        for entry in results:
            print(entry.get_credentials())
    else:
        print("No matching entries found.")


def save_entries(password_manager, encryption_key):
    password_manager.save_entries("\\data\\passwords.pkl", encryption_key)
    print("Entries saved successfully.")


def load_entries(password_manager, encryption_key):
    password_manager.load_entries("\\data\\passwords.pkl", encryption_key)
    print("Entries loaded successfully.")


if __name__ == "__main__":
    main()
