from entry import Entry
from sortcode import SortCode


class PasswordManager:
    entries: dict

    def __init__(self):
        self.entries: dict[SortCode, Entry]

    def create_entry(self, domain: str, username: str, password: str):
        # input validation
        if not all([domain, username, password]):
            raise ValueError("All fields are required.")

        sort_code = SortCode()
        self.entries[sort_code] = Entry(domain=domain, username=username, password=password, code=sort_code)


    def edit_entry(self):
        ...

    def delete_entry(self, sortCode: str):
        if sortCode in self.entries:
            self.entries.pop(sortCode)
