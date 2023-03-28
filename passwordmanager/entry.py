import uuid
from abc import abstractmethod, ABC
from credentials import Credentials


class EntryFactory:
    @staticmethod
    def create_entry(entry_type, **kwargs):
        if entry_type == "website":
            return WebsiteLogin(**kwargs)
        elif entry_type == "bank_account":
            return BankAccountLogin(**kwargs)
        else:
            raise ValueError("Invalid entry type")


class Entry(ABC):
    def __init__(self, **kwargs):
        self.id = uuid.uuid4()
        self.credentials = Credentials()

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_credentials(self):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    def matches_query(self, query):
        return str(self.id) == query or self.get_type() == query


class WebsiteLogin(Entry):
    def __init__(self, website, **kwargs):
        super().__init__(**kwargs)
        self.website = website

    def get_type(self):
        return "Website Login"

    def get_credentials(self):
        return f"Website: {self.website}\n{self.credentials}"

    def update(self, website=None, **kwargs):
        if website:
            self.website = website
        if kwargs:
            self.credentials.update(**kwargs)


class BankAccountLogin(Entry):
    def __init__(self, bank_name, account_number, routing_number, **kwargs):
        super().__init__(**kwargs)
        self.bank_name = bank_name
        self.account_number = account_number
        self.routing_number = routing_number

    def get_type(self):
        return "Bank Account Login"

    def get_credentials(self):
        return f"Bank: {self.bank_name}\nAccount Number: {self.account_number}\nRouting Number: {self.routing_number}\n{self.credentials}"

    def update(self, bank_name=None, account_number=None, routing_number=None, **kwargs):
        if bank_name:
            self.bank_name = bank_name
        if account_number:
            self.account_number = account_number
        if routing_number:
            self.routing_number = routing_number
        if kwargs:
            self.credentials.update(**kwargs)


