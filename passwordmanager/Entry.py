class Entry:
    domain: str
    username: str
    password: hash

    def __init__(self, code, domain: "", username: "", password):
        self.code = code
        self.domain = domain
        self.username = username
        self.password = password
