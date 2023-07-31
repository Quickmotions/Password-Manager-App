# Fergus Haak - 31/07/2023 - entry - Password Manager Program

from fuzzywuzzy import fuzz

class Entry:
    def __init__(self, entry_id, username, password):
        self.entry_id = entry_id
        self.username = username
        self.password = password

    def get_type(self) -> str:
        # Return the type of entry (e.g., "Login", "Credit Card", etc.)
        pass

    def get_credentials(self) -> str:
        # Return the username and password for this entry
        pass

    def update(self, username, password) -> None:
        # Update the username and password for this entry
        if username != "":
            self.username = username
        if password != "":
            self.password = password

    def matches_query(self, query, threshold=60) -> bool:
        # Check if this entry matches the given query
        pass


# Define subclasses of Entry for different types of login entries
class LoginEntry(Entry):
    def __init__(self, entry_id, username, password, website):
        super().__init__(entry_id, username, password)
        self.website = website

    def get_type(self) -> str:
        return "Login"

    def get_credentials(self) -> str:
        return f"Website: {self.website}\nUsername: {self.username}\nPassword: {self.password}"

    def update(self, username, password, website) -> None:
        super().update(username, password)

        if website != "":
            self.website = website

    def matches_query(self, query, threshold=60) -> bool:
        # Check if this entry matches the given query with a similarity threshold
        # The threshold determines the minimum similarity required for a match (default: 60)

        # Initialize the maximum similarity score to 0
        max_similarity_score = 0
        # Attributes to compare for fuzzy matching (customize as needed)
        attributes_to_compare = [self.username, self.website]

        # Loop through the attributes and calculate the maximum similarity score
        for entry_data in attributes_to_compare:
            similarity_score = fuzz.partial_ratio(entry_data.lower(), query.lower())
            if similarity_score > max_similarity_score:
                max_similarity_score = similarity_score

        # Return True if the similarity score is greater than or equal to the threshold
        return max_similarity_score >= threshold


class CreditCardEntry(Entry):
    def __init__(self, entry_id, cardholder_name, card_number, expiration_date, cvv):
        super().__init__(entry_id, cardholder_name, card_number)
        self.expiration_date = expiration_date
        self.cvv = cvv

    def get_type(self) -> str:
        return "Credit Card"

    def get_credentials(self) -> str:
        return f"Cardholder Name: {self.username}\nCard Number: {self.password}\nExpiration Date: {self.expiration_date}\nCVV: {self.cvv}"

    def update(self, cardholder_name, card_number, expiration_date, cvv):
        super().update(cardholder_name, card_number)
        if expiration_date != "":
            self.expiration_date = expiration_date
        if cvv != "":
            self.cvv = cvv

    def matches_query(self, query, threshold=60) -> bool:
        # Check if this entry matches the given query with a similarity threshold
        # The threshold determines the minimum similarity required for a match (default: 60)

        # Initialize the maximum similarity score to 0
        max_similarity_score = 0
        # Attributes to compare for fuzzy matching (customize as needed)
        attributes_to_compare = [self.username]

        # Loop through the attributes and calculate the maximum similarity score
        for entry_data in attributes_to_compare:
            similarity_score = fuzz.partial_ratio(entry_data.lower(), query.lower())
            if similarity_score > max_similarity_score:
                max_similarity_score = similarity_score

        # Return True if the similarity score is greater than or equal to the threshold
        return max_similarity_score >= threshold


# Define the EntryFactory class using the Factory Design Pattern
class EntryFactory:
    @staticmethod
    def create_login_entry(entry_id, username, password, website):
        # Create and return a new LoginEntry instance
        return LoginEntry(entry_id, username, password, website)

    @staticmethod
    def create_credit_card_entry(entry_id, cardholder_name, card_number, expiration_date, cvv):
        # Create and return a new CreditCardEntry instance
        return CreditCardEntry(entry_id, cardholder_name, card_number, expiration_date, cvv)
