import re
from Entry import Entry


class PasswordManager:
    entries: dict

    def __init__(self):
        self.entries = {}

    def create_entry(self, site: str, username: str, password: str):
        # input validation
        if not all([site, username, password]):
            raise ValueError("All fields are required.")
        if not re.match(r"^https?://", site):
            raise ValueError("Site must be a valid URL.")

        self.entries[site] = Entry(site=site, username=username, password=password)

    def generate_password(self, length: int, complexity: int):
        # implement password generator here
        pass

    def search(self, keyword: str):
        results = []
        for site, entry in self.entries.items():
            if keyword in site or keyword in entry.username:
                results.append(entry)
        return results
