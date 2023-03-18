import random
import string
from Entry import Entry


class PasswordManager:
    entries: dict

    def __init__(self):
        self.entries: dict[str, Entry]

    def create_entry(self, domain: str, username: str, password: str):
        # input validation
        if not all([domain, username, password]):
            raise ValueError("All fields are required.")

        code = self.generate_id()
        self.entries[code] = Entry(domain=domain, username=username, password=password, id=code)

    def generate_id(self) -> str:
        return f"{'0'*(4-len(self.entries)+1)}{(len(self.entries)+1)}"

    def generate_password(self, id: str, length: int, complexity: int = 0):
        # implement password generator here
        password = ""
        for _ in range(length):
            if complexity == 0:
                password += random.choice(string.ascii_letters)
            if complexity == 1:
                if random.randint(0, 1) == 0:
                    password += random.choice(string.punctuation)
                else:
                    password += random.choice(string.ascii_letters)
        self.entries[]
    def search(self, keyword: str):
        results = []
        for site, entry in self.entries.items():
            if keyword in site or keyword in entry.username:
                results.append(entry)
        return results


pm = PasswordManager()
pm.generate_password(10, 1)
