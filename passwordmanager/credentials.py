from passwordmanager.password import generate_password


class Credentials:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __str__(self):
        return f"Username: {self.username}\nPassword: {self.password}"

    def update(self, username=None, password=None):
        if username:
            self.username = username
        if password:
            self.password = password

    def generate_password(self):
        self.password = generate_password(length=16, complexity=1)
