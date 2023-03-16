class Entry:
    site: str
    username: str
    password: hash

    def __init__(self, site: "", username: "", password):
        self.site = site
        self.username = username
        self.password = password
