
class SortCode:

    def generate_id(self) -> str:
        return f"{'0' * (4 - len(self.entries) + 1)}{(len(self.entries) + 1)}"
