# Fergus Haak - 31/07/2023 - input validation - Password Manager Program

def validate_input(entry_data, entries):
    # Validate the provided entry data before creating an entry
    # You can add specific validation rules based on the entry type and requirements
    # For simplicity, this implementation checks for the presence of required fields.

    entry_type = entry_data.get("type")
    if entry_type is None:
        print("Error: Entry type is missing.")
        return False

    if entry_type == "Login":
        required_fields = ["id", "username", "password", "website"]
    elif entry_type == "Credit Card":
        required_fields = ["id", "cardholder_name", "card_number", "expiration_date", "cvv"]
    else:
        # Handle other entry types if needed
        print(f"Error: Unknown entry type '{entry_type}'.")
        return False

    for entry in entries:
        if entry_data.get("id") == entry.entry_id:
            print(f"Error: ID {entry.entry_id}' already exists in the entry data.")
            return False

    for field in required_fields:
        if field not in entry_data:
            print(f"Error: Missing '{field}' in the entry data.")
            return False

    return True
