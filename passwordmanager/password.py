import random
import string


class Password:
    def __init__(self):
        ...

    def generate_password(self, length: int, complexity: int = 0):
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
        print(password)
