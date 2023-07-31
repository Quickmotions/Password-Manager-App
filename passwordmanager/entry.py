import uuid
from abc import abstractmethod, ABC
from passwordmanager.credentials import Credentials


class EntryFactory:
    @staticmethod
    def create_entry(entry_type, *args):
        if entry_type == "website":
            return WebsiteLogin(*args)
        elif entry_type == "bank_account":
            return BankAccountLogin(*args)
        else:
            raise ValueError("Invalid entry type")


class Entry(ABC):
    def __init__(self, *args):
        self.id = uuid.uuid4()
        self.credentials = Credentials()

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_credentials(self):
        pass

    @abstractmethod
    def update(self, *args):
        pass

    def matches_query(self, query):
        return str(self.id) == query or self.get_type() == query


class WebsiteLogin(Entry):
    def __init__(self, website, *args):
        super().__init__(*args)
        self.website = website

    def get_type(self):
        return "Website Login"

    def get_credentials(self):
        return f"Website: {self.website}\t{self.credentials}"

    def update(self, website=None, *args):
        if website:
            self.website = website
        if args:
            self.credentials.update(*args)


class BankAccountLogin(Entry):
    def __init__(self, bank_name, account_number, routing_number, *args):
        super().__init__(*args)
        self.bank_name = bank_name
        self.account_number = account_number
        self.routing_number = routing_number

    def get_type(self):
        return "Bank Account Login"

    def get_credentials(self):
        return f"{self.bank_name}\t{self.account_number}\t{self.routing_number}\t{self.credentials}"

    def update(self, bank_name=None, account_number=None, routing_number=None, *args):
        if bank_name:
            self.bank_name = bank_name
        if account_number:
            self.account_number = account_number
        if routing_number:
            self.routing_number = routing_number
        if args:
            self.credentials.update(*args)


