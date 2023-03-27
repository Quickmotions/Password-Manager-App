from password import Password

class Entry:
    domain: str
    username: str
    password: Password

    def __init__(self, code, domain: "", username: "", password):
        self.sortCode = code
        self.domain = domain
        self.username = username
        self.password = password
