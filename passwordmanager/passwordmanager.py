from passwordmanager.entry import EntryFactory


class PasswordManager:

    def __init__(self):
        self.entries = []

    def create_entry(self, entry_type, **kwargs):
        entry = EntryFactory.create_entry(entry_type, **kwargs)
        self.entries.append(entry)

    def delete_entry(self, entry_id):
        for entry in self.entries:
            if entry.id == entry_id:
                self.entries.remove(entry)

    def edit_entry(self, entry_id, **kwargs):
        for entry in self.entries:
            if entry.id == entry_id:
                entry.update(**kwargs)

    def search(self, query):
        results = []
        for entry in self.entries:
            if entry.matches_query(query):
                results.append(entry)
        return results

    def save_entries(self):
        with open("data\\PasswordData.txt", "w") as file:
            for entry in self.entries:
                file.write(f"{entry.id}/t{entry.get_type()}/t{entry.get_credentials()}")
        file.close()
